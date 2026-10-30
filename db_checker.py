import os

import psycopg2
import time


time.sleep(3)

conn = psycopg2.connect(
    dbname=os.environ['POSTGRES_DB'],
    user=os.environ['POSTGRES_USER'],
    password=os.environ['POSTGRES_PASSWORD'],
    host=os.environ['DB_HOST'],
    port=5432
)

print('tests are done')