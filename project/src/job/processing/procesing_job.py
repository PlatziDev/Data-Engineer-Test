from pyspark.sql.functions import *

from job.spark_job_base import SparkBaseJob


class ProcessingJob(SparkBaseJob):
    def process(self):
        """
        Create an OLAP design for analyzing Platzi's payments
        It writes it on parquet format(columnar way)
        :return:
        """
        schema_name = "platzi"
        df_subscriptions = self.get_df_postgresql_query(f"select * from {schema_name}.{self.json_conf['ingestion']['subscriptions']['table_name']}")

        df_subscription_states = self.get_df_postgresql_query(f"select * from {schema_name}.{self.json_conf['ingestion']['subscription_states']['table_name']}")

        df_payment_methods = self.get_df_postgresql_query(f"select * from {schema_name}.{self.json_conf['ingestion']['payment_methods']['table_name']}")

        df_students = self.get_df_postgresql_query(f"select * from {schema_name}.{self.json_conf['ingestion']['students']['table_name']}")

        df_payment_methods_with_time = df_payment_methods \
            .withColumn("time_info_id", monotonically_increasing_id())\
            .withColumn("_day", dayofmonth(col("payment_date")).cast("string"))\
            .withColumn("_week", weekofyear(col("payment_date")).cast("string")) \
            .withColumn("_month", month(col("payment_date")).cast("string")) \
            .withColumn("_year", year(col("payment_date")).cast("string")) \
            .withColumn("_dt",  date_format(col("payment_date"), "yyyy-MM-dd"))

        df_payment_events = df_payment_methods_with_time.alias("df_payment_methods_with_time").join(df_subscription_states.alias("df_subscription_states"),
                                                        (df_payment_methods_with_time["student_id"] == df_subscription_states["student_id"]) &
                                                        (df_payment_methods_with_time["subscription_id"] == df_subscription_states["subscription_id"]),
                                                        how="left")

        df_payment_events = df_payment_events.withColumn("payment_event_id", monotonically_increasing_id())

        df_payment_methods = df_payment_methods.select(
                                             col("payment_method_id"),
                                             col("payment_method_type"),
                                             col("description"))

        df_payment_methods_with_time = df_payment_methods_with_time.select(
                                             col("time_info_id"),
                                             col("_day"),
                                             col("_week"),
                                             col("_month"),
                                             col("_year"),
                                             col("_dt"))

        df_payment_events = df_payment_events.select(
                                             col("payment_event_id"),
                                             col("df_payment_methods_with_time.student_id"),
                                             col("df_payment_methods_with_time.time_info_id"),
                                             col("df_subscription_states.subscription_id"),
                                             col("df_subscription_states.subscription_type"),
                                             col("df_subscription_states.subscription_state_value"),
                                             col("df_payment_methods_with_time.currency_price"),
                                             col("df_payment_methods_with_time.usd_price"),
                                             col("df_payment_methods_with_time.currency"),
                                             col("df_subscription_states.start_date").alias("subscription_start_date"),
                                             col("df_subscription_states.end_date").alias("subscription_end_date"))

        df_students.write.mode("overwrite")\
            .parquet(self.json_conf["processing"]["students_output_path"])

        df_subscriptions.write.mode("overwrite")\
            .parquet(self.json_conf["processing"]["subscriptions_output_path"])

        df_payment_methods.write.mode("overwrite")\
            .parquet(self.json_conf["processing"]["payment_methods_output_path"])

        df_payment_methods_with_time.write.mode("overwrite")\
            .parquet(self.json_conf["processing"]["time_info_output_path"])

        df_payment_events.write.mode("overwrite")\
            .parquet(self.json_conf["processing"]["payment_events_output_path"])
