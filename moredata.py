import requests
import re

# git reset --hard HEAD
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
    if picture_name == 'silhueta.png':
        return None
    r = requests.get(url_picture)
    with open('pictures/{0}'.format(picture_name), 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    return picture_name

"""
with open('staff.csv') as f:
    with open('data.csv', 'w') as g:
        for person in f:
            info = person.split(';')
            url = info[3]
            print('Downloading {0} {1} ...'.format(info[0], info[1]))
            picture_name = get_picture(url)
            if picture_name is not None:
                print('{0};{1};{2}'.format(info[0], info[1], picture_name), file=g)
"""

def extract_data(class_, text):
    pattern = r"<td class='{0}' itemprop=\".*?\">(.*?)</td>".format(class_)
    m = re.search(pattern, text, flags=re.DOTALL)
    return m.group(1)
    
def extract_div(text):
    pattern = r"<div class='field'>(.*?)</div>"
    return re.findall(pattern, text, flags=re.DOTALL)
    
def extract_slo_eng(text):
    pattern_slo = r'^(.*?)<br>'
    m = re.search(pattern_slo, text, flags=re.DOTALL)
    pattern_eng = r"<span style='color:gray'>(.*?)</span>"
    m2 = re.search(pattern_eng, text, flags=re.DOTALL)
    return m.group(1).strip(), m2.group(1).strip()

def get_more_data(s):
    url = 'https://www.famnit.upr.si' + s
    r = requests.get(url)
    full_name_pattern = r"<h1 style='.*?' itemprop=\"name\">(.*?)</h1>"
    m = re.search(full_name_pattern, r.text)
    full_name = m.group(1).strip()
    title_pattern = r"<h2 style='.*?' class='pedagoska'  itemprop=\"title\">\s*(.*?) / <span style='.*?'>(.*?)</span>\s*</h2>"
    title_slo = None
    title_eng = None
    try:
        m = re.search(title_pattern, r.text)
        title_slo = m.group(1).strip()
        title_eng = m.group(2).strip()
    except AttributeError:
        pass
    office_pattern = r"<td class='kabinet' itemprop=\"address\">(.*?)</td>"
    m = re.search(office_pattern, r.text)
    office = m.group(1).strip()
    return {'full_name': full_name, 'title_eng': title_eng, 'title_slo': title_slo, 'office': office,
        'departments': [extract_slo_eng(x) for x in extract_div(extract_data('departments', r.text))],
        'research': [extract_slo_eng(x) for x in extract_div(extract_data('research', r.text))],
        'subjects': [extract_slo_eng(x) for x in extract_div(extract_data('subjects', r.text))]
    } 

def get_more_data_ignore_office_people(s):
    try:
        ret = get_more_data(s)
        return ret
    except AttributeError:
        # print(s)
        return None

with open('staff.csv') as f:
    for person in f:
        info = person.split(';')
        url = info[3]
        print('Downloading {0} {1} ...'.format(info[0], info[1]))
        print(get_more_data_ignore_office_people(url))    






