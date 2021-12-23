import os
import json
import argparse
from abc import ABC, abstractmethod
from pyspark.sql import SparkSession


class SparkBaseJob(ABC):

    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.spark = self.__get_spark_session()
        log4jLogger = self.spark.sparkContext._jvm.org.apache.log4j
        self.logger = log4jLogger.LogManager.getLogger(self.args.app_name)
        self.logger.setLevel(log4jLogger.Level.INFO)
        self.spark.sparkContext.setCheckpointDir("/tmp")
        self.logger.info(f"starting... {type(self).__name__}")
        self.json_conf = json.load(open(args.config_file))

    def __get_spark_session(self):
        return SparkSession \
            .builder \
            .master("local") \
            .appName(self.args.app_name) \
            .config("spark.jars", os.getenv('POSTGRESQL_DRIVER_PATH')) \
            .config("spark.driver.memory", "4g") \
            .config("spark.executor.memory", "4g") \
            .getOrCreate()

    def get_df_postgresql_query(self, query):
        url = os.environ['POSTGRES_URL_DB']
        username = os.environ["POSTGRES_USER"]
        password = os.environ["POSTGRES_PASSWORD"]
        self.logger.info(f"Pulling data from Postgres, query:")
        self.logger.info(query)
        return self.spark.read \
            .format("jdbc") \
            .option("url", url) \
            .option("user", username) \
            .option("password", password) \
            .option("driver", "org.postgresql.Driver") \
            .option("query", query) \
            .load()

    def write_df_into_postgre(self, df, db_table, mode="append"):
        url = os.environ['POSTGRES_URL_DB']
        username = os.environ["POSTGRES_USER"]
        password = os.environ["POSTGRES_PASSWORD"]
        self.logger.info(f"writing table={db_table} to Postgres")
        df.write.format('jdbc').options(
            url=url,
            dbtable=db_table,
            user=username,
            password=password,
            driver="org.postgresql.Driver"
        ).mode(mode).save()

    @abstractmethod
    def process(self):
        """Start a Spark Job"""
        raise NotImplementedError
