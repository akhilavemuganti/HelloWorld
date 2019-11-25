import psycopg2 as pg
import pandas as pd

hostname="aws-directaccess-postgres-db-dev.ckb7bg8wp0kq.us-east-1.rds.amazonaws.com"
username="directaccessread"
password="d1r3ct4cc3ssr34d"
database="directaccess"

# hostname="localhost"
# username="postgres"
# password="postgres"
# database="postgres"
query = "SELECT * FROM da.packerext WHERE entl_state='CO' AND deletedDate IS NULL"
try:
    conn = pg.connect(user=username,password=password, host=hostname,port=5432, dbname=database)
    cur = conn.cursor()
    print ("Connected to DB!")
    cur.execute(query)
    count=0
    for rows in cur.fetchall():
        results = pd.read_sql_query(query, conn)
        results.to_csv("Packers.csv", index=False)
        count=count+1
    print (count)

except (Exception, pg.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
cur.close()
conn.close()