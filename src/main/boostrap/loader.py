from src.main.generic.connection_generic import ConnectionGeneric
from src.main.generic.parameter_generic import ParameterGeneric
from dotenv import load_dotenv
from pathlib import Path
from pyspark.sql import SparkSession
import os
import json


class Loader:
    """
        Entry point for initialize components
    """

    __current_path = Path(os.getcwd()).parent.parent

    def __init__(self):
        load_dotenv()
        file_env_path = f"{self.__current_path}/env"
        load_dotenv(dotenv_path=file_env_path)

        self.__generateParameter()
        self.__generateConnection()
        self.__generateSparkSession()

    def __generateConnection(self):
        """
            Generate two connector for postgrest and redshift
        """
        driver_connector = os.getenv('driver_connector')

        self._postgres_connection = ConnectionGeneric(os.getenv('postgres_host'), os.getenv('postgres_port'),
                                                      os.getenv('postgres_user'), os.getenv('postgres_password'),
                                                      driver_connector, self._parameters.connection_type,
                                                      self._parameters.connection_protocol,
                                                      self._parameters.relational_model.get('database'))

        self._redshift_connection = ConnectionGeneric(os.getenv('redshift_host'), os.getenv('redshift_port'),
                                                      os.getenv('redshift_user'), os.getenv('redshift_password'),
                                                      driver_connector, self._parameters.connection_type,
                                                      self._parameters.connection_protocol,
                                                      self._parameters.bi_model.get('database'))

    def __generateParameter(self):
        """
            Generate an object with attributes based on a parameter file (json)
        """
        file_parameters_path = f"{self.__current_path}/conf/parameters.json"

        with open(file_parameters_path, 'r') as json_file:
            data = json.load(json_file)
            self._parameters = ParameterGeneric(data)

    def __generateSparkSession(self):
        """
            Generate a spark session with dependencies
        """
        jars_list = ''

        for jar in self._parameters.external_dependencies:
            jars_list += f"{self.__current_path}/conf/jar/{jar}{'' if jars_list == '' else ','}"

        self._spark_session = SparkSession.builder.appName("ETL PLATZI") \
            .config("spark.jars", jars_list).getOrCreate()

