import pandas as pd
import psycopg2

conn = psycopg2.connect(database="test", user='', password='', host='localhost', port= '5432' )
cursor = conn.cursor()
query = "select * from tirth"
cursor.execute(query)

myallData = cursor.fetchall()
db_cursor = conn.cursor()
    # Use the COPY function on the SQL we created above.
SQL_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)

    # Set up a variable to store our file path and name.
t_path_n_file = "users.csv"

    # Trap errors for opening the file
try:
    with open(t_path_n_file, 'w') as f_output:
        db_cursor.copy_expert(SQL_for_file_output, f_output)
except Exception as e:
    print(e)
   