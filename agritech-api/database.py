import psycopg2
from flask import Flask

app = Flask(__name__)

class DatabaseConnection():
    def __init__(self):
        """
        This constructor creates a connection to the database
        :param dbname: 
        :param user: 
        :param password: 
        :param host: 
        :param port: 
        """
        self.conn_params = dict(
            user = "postgres",
            password = "viv",
            host = "127.0.0.1",
            port = "5432",
            database = 'agriBid'
            )

        # self.conn_params = dict(
        #     user = "gmwejdgiawxwsn",
        #     password = "d8f6c977ac22e089f08076452526b86ea4d5ce40b338e912ae2b256c50b96819",
        #     host = "ec2-54-204-40-248.compute-1.amazonaws.com",
        #     port = "5432",
        #     database = 'dffbgb2dpdlbm5',
        #     )
        
        self.connection = psycopg2.connect(**self.conn_params)                        
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """ This method creates all tables"""
        create_table_query_for_users = (
                                """CREATE TABLE IF NOT EXISTS
                                users(
                                        users_id SERIAL PRIMARY KEY,
                                        name VARCHAR(50) NOT NULL,
                                        email VARCHAR (50) UNIQUE,
                                        password VARCHAR(100) NOT NULL,
                                        role VARCHAR(50) NOT NULL
                                        ); """
                                )

        create_table_query_for_produce = ( 
                                """ CREATE TABLE IF NOT EXISTS 
                                farmer_produce(
                                        products_id SERIAL PRIMARY KEY,
                                        produce_name VARCHAR (50),
                                        quantity VARCHAR (50),
                                        unit_price INTEGER NOT NULL,
                                        users_id INTEGER,
                                        date_created TIMESTAMP, 
                                        date_modified TIMESTAMP,
                                        FOREIGN KEY (users_id)REFERENCES 
                                        users (users_id) ON DELETE CASCADE ON UPDATE CASCADE
                                        );"""
                                )

        create_table_query_for_client_request = ( 
                        """ CREATE TABLE IF NOT EXISTS 
                        client_request(
                                products_id SERIAL PRIMARY KEY,
                                produce_name VARCHAR (50),
                                quantity VARCHAR (50),
                                price_range VARCHAR (50),
                                users_id INTEGER,
                                date_created TIMESTAMP, 
                                date_modified TIMESTAMP,
                                FOREIGN KEY (users_id)REFERENCES 
                                users (users_id) ON DELETE CASCADE ON UPDATE CASCADE
                                );"""
                        )

        # Execute creating tables
        self.cursor.execute(create_table_query_for_users)
        self.cursor.execute(create_table_query_for_produce)
        self.cursor.execute(create_table_query_for_client_request)

      # Remove all the records from the table
    def drop_table(self, table_name):
        """
        This method truncates a table
        :param table_name: 
        :return: 
        """
        self.cursor.execute("TRUNCATE TABLE {} RESTART IDENTITY CASCADE"
                            .format(table_name))
