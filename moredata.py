import requests
import re

def more_info(s):
    url = 'https://www.famnit.upr.si' + s
    r = requests.get(url)
    print(r.text)

print(more_info('/en/about-faculty/staff/andy'))
