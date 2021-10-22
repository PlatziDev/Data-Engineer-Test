import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drop previously created tables before inserting on new trial.
    -------------------
    Param:
        cur: SQL cursor to execute queries
        conn: Connection instance to commit changes
    Return:
        None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create all tables in DW, including staging and dimensional model
    -------------------
    Param:
        cur: SQL cursor to execute queries
        conn: Connection instance to commit changes
    Return:
        None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config['DB'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
