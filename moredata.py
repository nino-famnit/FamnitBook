import requests
import re

def get_picture(s):
    url = 'https://www.famnit.upr.si' + s
    r = requests.get(url)
    img_pattern = r'http://www\.famnit\.upr\.si/sl/resources/images/o-fakulteti/osebje/.*\.jpg'
    m = re.search(img_pattern, r.text)
    url_picture = m.group(0)
    r = requests.get(url_picture)
    with open('pictures/ado.jpg', 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    

print(get_picture('/en/about-faculty/staff/ademir.hujdurovic/'))

