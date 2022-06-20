import psycopg2
from locust import Locust, User, between, TaskSet, task, events
import time


def create_conn():
    conn = psycopg2.connect(database="test", user='', password='', host='localhost', port= '5432' )
    if None != conn:
        print("Connection successful")

    return conn


class dbconnection(User):

    @task(1)
    def execute_query(self):
        connection=create_conn()
        cursor = connection.cursor()
        try:
            cursor.execute('''select * from tirth''')
            result = cursor.fetchall()
            print(result)
        except Exception as e:
            print(format(e))
       







