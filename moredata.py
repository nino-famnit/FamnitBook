import requests
import re

# git reset --hard <funny string>
# git pull origin master

def get_picture(s):
    url = 'https://www.famnit.upr.si' + s
    r = requests.get(url)
    allowed_extensions = ['jpg', 'png']
    img_pattern = r'http://www\.famnit\.upr\.si/sl/resources/images/o-fakulteti/osebje/(.*\.({0}))'.format(
        '|'.join(allowed_extensions)
    )
    m = re.search(img_pattern, r.text)
    url_picture = m.group(0)
    picture_name = m.group(1)
    r = requests.get(url_picture)
    with open('pictures/{0}'.format(picture_name), 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

with open('staff.csv') as f:
    for person in f:
        info = person.split(';')
        url = info[3]
        print('Downloading {0} {1} ...'.format(info[0], info[1]))
        get_picture(url)

