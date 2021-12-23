from pyspark.sql.functions import col
from pyspark.sql.types import DateType, IntegerType
from job.spark_job_base import SparkBaseJob


class IngestionJob(SparkBaseJob):
    def process(self):
        """
        Ingest the data into Postgres using Spark
        :return:
        """
        df_subscriptions = self.spark.read.load(path=self.json_conf["ingestion"]["subscriptions"]["path"],
                                                format="csv", header="true")

        df_subscription_states = self.spark.read.load(path=self.json_conf["ingestion"]["subscription_states"]["path"],
                                                     format="csv", header="true")

        df_payment_methods = self.spark.read.load(path=self.json_conf["ingestion"]["payment_methods"]["path"],
                                                  format="csv", header="true")

        df_students = self.spark.read.load(path=self.json_conf["ingestion"]["students"]["path"],
                                           format="csv", header="true")

        df_students_classes = self.spark.read.load(path=self.json_conf["ingestion"]["students_classes"]["path"],
                                                   format="csv", header="true")

        df_students_courses = self.spark.read.load(path=self.json_conf["ingestion"]["students_courses"]["path"],
                                                   format="csv", header="true")

        df_students_schools = self.spark.read.load(path=self.json_conf["ingestion"]["students_schools"]["path"],
                                                format="csv", header="true")

        df_students_extra_events = self.spark.read.load(path=self.json_conf["ingestion"]["students_extra_events"]["path"],
                                                        format="csv", header="true")

        df_extra_events = self.spark.read.load(path=self.json_conf["ingestion"]["extra_events"]["path"],
                                               format="csv", header="true")

        df_schools = self.spark.read.load(path=self.json_conf["ingestion"]["schools"]["path"],
                                          format="csv", header="true")

        df_courses = self.spark.read.load(path=self.json_conf["ingestion"]["courses"]["path"],
                                          format="csv", header="true")

        df_classes = self.spark.read.load(path=self.json_conf["ingestion"]["classes"]["path"],
                                          format="csv", header="true")

        df_subscription_states = df_subscription_states.withColumn("start_date", col("start_date").cast(DateType()))
        df_subscription_states = df_subscription_states.withColumn("end_date", col("end_date").cast(DateType()))
        df_subscription_states = df_subscription_states.withColumn("created_at", col("created_at").cast(DateType()))
        df_payment_methods = df_payment_methods.withColumn("payment_date", col("payment_date").cast(DateType()))
        df_students_classes = df_students_classes.withColumn("percentage_completed", col("percentage_completed").cast(IntegerType()))

        self.write_df_into_postgre(df=df_students,
                                   db_table=self.json_conf["ingestion"]["students"]["table_name"])

        self.write_df_into_postgre(df=df_subscriptions,
                                   db_table=self.json_conf["ingestion"]["subscriptions"]["table_name"])

        self.write_df_into_postgre(df=df_extra_events,
                                   db_table=self.json_conf["ingestion"]["extra_events"]["table_name"])

        self.write_df_into_postgre(df=df_schools,
                                   db_table=self.json_conf["ingestion"]["schools"]["table_name"])

        self.write_df_into_postgre(df=df_courses,
                                   db_table=self.json_conf["ingestion"]["courses"]["table_name"])

        self.write_df_into_postgre(df=df_classes,
                                   db_table=self.json_conf["ingestion"]["classes"]["table_name"])

        self.write_df_into_postgre(df=df_students_classes,
                                   db_table=self.json_conf["ingestion"]["students_classes"]["table_name"])

        self.write_df_into_postgre(df=df_students_courses,
                                   db_table=self.json_conf["ingestion"]["students_courses"]["table_name"])

        self.write_df_into_postgre(df=df_students_extra_events,
                                   db_table=self.json_conf["ingestion"]["students_extra_events"]["table_name"])

        self.write_df_into_postgre(df=df_students_schools,
                                   db_table=self.json_conf["ingestion"]["students_schools"]["table_name"])

        self.write_df_into_postgre(df=df_subscription_states,
                                   db_table=self.json_conf["ingestion"]["subscription_states"]["table_name"])

        self.write_df_into_postgre(df=df_payment_methods,
                                   db_table=self.json_conf["ingestion"]["payment_methods"]["table_name"])

