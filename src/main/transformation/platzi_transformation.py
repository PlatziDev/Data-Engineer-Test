from src.main.generic.transformation_generic import TransformationGeneric
from src.main.common.util import Util
from pyspark.sql.functions import col, coalesce, lit


class PlatziTransformation(TransformationGeneric):
    """
        PLATZI - ETL
    """

    def __init__(self):
        super().__init__()
        self.__payment_classification_df = None
        self.__payment_method_df = None
        self.__payment_detail_df = None
        self.__currency_df = None
        self.__event_type_df = None
        self.__subscription_type_df = None
        self.__user_df = None
        self.__subscription_event_df = None
        self.__subscription_df = None

    def __read_inputs(self):
        """
            Retrieve all necessary sources
        """
        self.__payment_classification_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('payment_classification'))
        self.__payment_method_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('payment_method'))
        self.__payment_detail_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('payment_detail'))
        self.__currency_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('currency'))
        self.__event_type_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('event_type'))
        self.__subscription_type_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('subscription_type'))
        self.__user_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('user'))
        self.__subscription_event_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('subscription_event'))
        self.__subscription_df = \
            self._postgres_connection.reader(self._spark_session,
                                             self._parameters.relational_model.get('subscription'))

    @Util.ingestion_exception_handler
    def __generate_dim_event_type(self):
        """
            Generate the event type dimension
        """
        dim_event_df = self.__event_type_df.select(col('id_event_type'), col('description').alias('name'),
                                                   col('status'))
        dim_event_redshift_df = self._redshift_connection.reader(self._spark_session,
                                                                 self._parameters.bi_model.get('event_type'))

        dim_event_df = dim_event_df.join(dim_event_redshift_df, 'id_event_type', 'leftanti')

        self._redshift_connection.writer(dim_event_df, self._parameters.write_mode,
                                         self._parameters.bi_model.get('event_type'))

    @Util.ingestion_exception_handler
    def __generate_dim_subscription_type(self):
        """
            Generate the subscription type
        """
        dim_subscription_type_df = self.__subscription_type_df.select(col('id_subscription_type'), col('name'),
                                                                      col('description'))
        dim_subscription_type_redshift_df = self._redshift_connection.reader(self._spark_session,
                                                                             self._parameters.bi_model
                                                                             .get('subscription_type'))

        dim_subscription_type_df = dim_subscription_type_df.join(dim_subscription_type_redshift_df,
                                                                 'id_subscription_type', 'leftanti')

        self._redshift_connection.writer(dim_subscription_type_df, self._parameters.write_mode,
                                         self._parameters.bi_model.get('subscription_type'))

    @Util.ingestion_exception_handler
    def __generate_dim_user_subscription(self):
        """
            Generate the user subscriptions
        """
        dim_user_subscription_df = self.__subscription_df.join(self.__user_df, 'id_user'). \
            select(col('id_subscription'), col('description'), col('benefits'), col('first_name'), col('middle_name'),
                   col('last_name'), col('bio'), col('email'))

        dim_user_subscription_redshift_df = self._redshift_connection.reader(self._spark_session,
                                                                             self._parameters.bi_model
                                                                             .get('user_subscription'))

        dim_user_subscription_df = dim_user_subscription_df.join(dim_user_subscription_redshift_df,
                                                                 'id_subscription', 'leftanti')

        self._redshift_connection.writer(dim_user_subscription_df, self._parameters.write_mode,
                                         self._parameters.bi_model.get('user_subscription'))

    @Util.ingestion_exception_handler
    def __generate_dim_payment(self):
        """
           Generate the payments
        """
        payment_method_classification_df = \
            self.__payment_method_df.join(self.__payment_classification_df, 'id_payment_classification', 'left'). \
            select(col('id_payment_method'), self.__payment_method_df['name'].alias('payment_method'),
                   self.__payment_classification_df['name'].alias('payment_classification'))

        dim_payment_df = self.__payment_detail_df.join(payment_method_classification_df, 'id_payment_method') \
            .join(self.__currency_df, 'id_currency') \
            .select(col('id_payment_detail').alias('id_payment'), col('payment_method'), col('payment_classification'),
                    col('iso').alias('currency_iso'), col('name').alias('currency_name'), col('identity_card'),
                    col('cardholder_name'), col('card_number'), col('token_transaction'), col('status_code'),
                    col('expiry_date'), col('security_code'))

        dim_payment_redshift_df = self._redshift_connection.reader(self._spark_session,
                                                                   self._parameters.bi_model
                                                                   .get('payment'))

        dim_user_subscription_df = dim_payment_df.join(dim_payment_redshift_df,
                                                       'id_payment', 'leftanti')

        self._redshift_connection.writer(dim_user_subscription_df, self._parameters.write_mode,
                                         self._parameters.bi_model.get('payment'))

    @Util.ingestion_exception_handler
    def __generate_fac_event(self):
        """
           Generate the events facts
        """
        event_detail_df = self.__payment_detail_df.select(col('id_payment_detail'),
                                                          col('amount').alias('amount_payment'))

        fac_events_df = self.__subscription_event_df.join(event_detail_df, 'id_payment_detail', 'left') \
            .select(col('id_subscription_event').alias('id_event_type'),
                    coalesce(col('id_payment_detail'), lit(-1)).alias('id_payment'),
                    col('id_subscription'), col('id_subscription_type'), col('event_timestamp'),
                    col('subscription_start_date'), col('subscription_end_date'), col('status'), col('amount_payment'))

        fac_events_redshift_df = self._redshift_connection.reader(self._spark_session,
                                                                  self._parameters.bi_model
                                                                  .get('event'))

        fac_events_df = fac_events_df.join(fac_events_redshift_df,
                                           ['id_event_type', 'id_payment', 'id_subscription',
                                            'id_subscription_type'], 'leftanti')

        self._redshift_connection.writer(fac_events_df, self._parameters.write_mode,
                                         self._parameters.bi_model.get('event'))

    def __transform(self):
        """
           Execute all of transformations o processes
        """
        self.__generate_dim_event_type()
        self.__generate_dim_subscription_type()
        self.__generate_dim_user_subscription()
        self.__generate_dim_payment()
        self.__generate_fac_event()

    def execute(self):
        """
           Execute the general process
        """
        self.__read_inputs()
        self.__transform()
