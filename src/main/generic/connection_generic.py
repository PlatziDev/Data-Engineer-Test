class ConnectionGeneric:
    """
        Generate a generic connection to data source
    """

    def __init__(self, host, port, user, password, driver, format_type, protocol, database):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__driver = driver
        self.__format_type = format_type
        self.__protocol = protocol
        self.__database = database

    def reader(self, spark, table):
        """
            Retrieve a dataframe with data of the source
        """
        return spark.read.format(self.__format_type). \
            option('url', f"{self.__format_type}:{self.__protocol}://{self.__host}:{self.__port}/{self.__database}"). \
            option('dbtable', table). \
            option('user', self.__user). \
            option('password', self.__password). \
            option("driver", self.__driver). \
            load()

    def writer(self, data_frame, write_mode, table):
        """
            Send dataframe to the source to persist the information
        """
        properties = {"user": self.__user, "password": self.__password, "driver": self.__driver}
        data_frame.write.jdbc(url=f"{self.__format_type}:{self.__protocol}://{self.__host}:{self.__port}/{self.__database}",
                              table=table,
                              mode=write_mode,
                              properties=properties)
