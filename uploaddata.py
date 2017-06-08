import psycopg2

# pip3 install psycopg2

dbname = 'nino_basic'
user = 'nino_basic'
host = 'www.studenti.famnit.upr.si'
password = 'burek'

conn = psycopg2.connect("dbname='{0}' user='{1}' host='{2}' password='{3}'".format(
    dbname, user, host, password))

query = """INSERT INTO professor (name, surname, email, homepage, url)
    VALUES ('{1}', '{2}', '{3}', '{4}', '{5}')"""

cur = conn.cursor()

with open('staff.csv') as f:
    for i, line in enumerate(f):
        name, family_name, phone_numbers, url, email, homepage = line.strip().split(';')
        cur.execute(query.format(i + 1, name, family_name, email, homepage, url))

conn.commit()  # If this line is missing, changes are not saved.

cur.close()
conn.close()

