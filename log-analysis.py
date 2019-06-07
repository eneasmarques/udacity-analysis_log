#!/usr/bin/env python3
import psycopg2

DB_NAME = 'news'
DB_USER = 'vagrant'
DB_PASSWORD = 'vagrant'
DB_HOST = '0.0.0.0'
DB_PORT = '5432'

conn = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT,
    host=DB_HOST
)


def formatText(text=""):
    if text == "":
        return text.rjust(50, "-") + "+"
    else:
        return text.ljust(50, " ") + "|"


cur = conn.cursor()
query = """
SELECT ar.id, ar.title, count(ar.id) as views
FROM log l, articles ar
WHERE '/article/'||ar.slug = l.path and l.status = '200 OK'
GROUP BY ar.id, ar.title
ORDER BY views desc
LIMIT 3;
"""

print(formatText())

cur.execute(query)
results = cur.fetchall()
for result in results:
    title = result[1]
    views = result[2]
    text = formatText(title + " - " + str(views) + "views")
    print(text)

query = """
SELECT au.id, au.name, count(ar.id) as views
FROM log l, articles ar, authors au
WHERE '/article/'||ar.slug = l.path and au.id = ar.author
and l.status = '200 OK'
GROUP BY au.id, ar.id, ar.title
ORDER BY views desc limit 3
"""

print(formatText())

cur.execute(query)
results = cur.fetchall()
for result in results:
    name = result[1]
    views = result[2]
    text = formatText(name+" - "+str(views))
    print(text)

query = """
select time, percent_error::text || '%' as percent_error from (
select TO_CHAR(date(time)::DATE, 'Mon dd, yyyy') as time,
round(CAST((count(status) filter(where status <> '200 OK'))*100/(count(status))
::float as numeric),2) as percent_error
from log group by date(time)) as log_errors
where percent_error > 1;
"""

print(formatText())

cur.execute(query)
results = cur.fetchall()
for result in results:
    time = result[0]
    percent = result[1]
    text = formatText(time+" - "+str(percent))
    print(text)

print(formatText())

cur.close()
conn.close()
