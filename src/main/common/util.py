class Util:
    """
        Utilities methods
    """

    @staticmethod
    def ingestion_exception_handler(function):
        """
            Function to handle error in write in postgres or redshift
        """
        def inner_function(*args, **kwargs):
            try:
                function(*args, **kwargs)
                print(f"{function.__name__}: ingested data complete.")
            except TypeError:
                print(f"{function.__name__}: can't ingest data, occurred an error.")

        return inner_function
