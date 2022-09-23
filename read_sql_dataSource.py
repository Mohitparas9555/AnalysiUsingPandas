import pandas as pd
import sqlalchemy
import pymysql
# conn_engine=sqlalchemy.create_engine("mysql+pymysql://username:@host_name/db_name")
conn_engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/customer")
df = pd.read_sql_query("SELECT * FROM customer", conn_engine)
