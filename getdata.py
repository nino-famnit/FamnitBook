import requests
import re

r = requests.get('https://www.famnit.upr.si/en/about-faculty/staff/')
# print(r.text)

p = r"<tr id='person_(\d+)' class='(odd|even) '>(.*?)</tr>"
staff = re.findall(p, r.text, flags=re.DOTALL)

def extract_professor(s):
    p2 = r"<td class='name'><a href='(.*)'>(.*)</a></td>\s*" + \
     r"<td class='name'><a href='.*'>(.*)</a></td>\s*" + \
     r"<td class='phone' nowrap>(.*)</a></td>\s*" + \
     r"<td class='email'>(.*)</td>\s*" + \
     r"<td class='website'>(.*)</td>"
    # print(p2)
    r = re.search(p2, s, flags=re.DOTALL)
    # print(r)
    link = r.group(1)
    name = r.group(3).strip()
    surname = r.group(2).strip()
    phone = r.group(4).strip()
    if phone == '':
        phone = None
    s_email = r.group(5)
    p_email = r"'mailto:(.*)'"
    r_email = re.search(p_email, s_email)
    email = r_email.group(1).strip()
    s_home = r.group(6)
    p_home = r"href='(.*?)'"
    # print(s_home)
    r_home = re.search(p_home, s_home)
    home_page = None if r_home is None else r_home.group(1).strip()
    return (name, surname, phone, link, email, home_page)

with open('staff.csv', 'w') as f:
    for person in staff:
        p = extract_professor(person[2])
        print(';'.join([str(x) for x in p]), file=f)
















