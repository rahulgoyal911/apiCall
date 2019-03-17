import sys, psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "namespace1", hostaddr="35.198.246.100", port = "5432")
print ('Opened database successfully')
cur = conn.cursor()

str1 = "\COPY metgis TO 'a.csv' DELIMITER ',' CSV HEADER;"
print(str1)
cur.execute(str1)
cur.close()