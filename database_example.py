import psycopg2

dbname = 'nino_basic'
user = 'nino_basic'
host = 'www.studenti.famnit.upr.si'
password = 'burek'

conn = psycopg2.connect("dbname='{0}' user='{1}' host='{2}' password='{3}'".format(
    dbname, user, host, password))

cur = conn.cursor()

cur.execute("SELECT DISTINCT language FROM countrylanguage")

langs = [x[0] for x in cur.fetchall()]

query = """SELECT ROUND(SUM(countrylanguage.percentage * country.population / 100)) FROM countrylanguage
JOIN country ON countrylanguage.countrycode = country.code
WHERE countrylanguage.language = '{0}'
"""

t = []

for l in langs:
    cur.execute(query.format(l))
    t.append((cur.fetchone()[0], l))

t.sort(reverse=True)

for i in range(100):
    print(t[i])
# print(langs)
