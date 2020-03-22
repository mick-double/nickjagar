""" 
posgresqlに接続する
"""

import psycopg2 as pg2



sql01 = 'select * from staff ;'
# sql02 = "insert into staff(name,bust,weist,hip) values('藍色しあん',90,62,83);"
sql02 = "insert into staff(name,tall,bust,weist,hip) values('tomono',156,76,56,86);"

conn = pg2.connect("dbname = omanko user=mick password=mickysan0 ")
conn.autocommit = True
cur = conn.cursor()
# cur.execute(sql02)
cur.execute(sql01)
results = cur.fetchall()
for r in results:
    print(r)
cur.close()
conn.close()
