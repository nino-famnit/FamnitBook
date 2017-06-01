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

def get_more_data(s):
    url = 'https://www.famnit.upr.si' + s
    r = requests.get(url)
    full_name_pattern = r"<h1 style='.*?' itemprop=\"name\">(.*?)</h1>"
    m = re.search(full_name_pattern, r.text)
    full_name = m.group(1).strip()
    title_pattern = r"<h2 style='.*?' class='pedagoska'  itemprop=\"title\">\s*(.*?) / <span style='.*?'>(.*?)</span>\s*</h2>"
    m = re.search(title_pattern, r.text)
    title_slo = m.group(1).strip()
    title_eng = m.group(2).strip()
    return {'full_name': full_name, 'title_eng': title_eng, 'title_slo': title_slo} 

print(get_more_data('/en/about-faculty/staff/vito.vitrih/'))    

"""
<td class='kabinet' itemprop="address">II/14 (Kettejeva 1, Koper)</td>
	
<td class='departments' itemprop="affiliation">
<div class='field'>Oddelek za matematiko<br><span style='display: none;'> / </span>
<span style='color:gray'>Department of Mathematics</span><br></div></td>
	</tr>
	
<td class='research' itemprop="role">
<div class='field'>Numerična matematika <br><span style='color:gray'> Numerical Mathematics</span><br></div><div class='field'>Polinomska interpolacija v več dimenzijah <br><span style='color:gray'> Multivariate Polynomial Interpolation</span><br></div><div class='field'>Računalniško podprto geometrijsko načrtovanje (CAGD) <br><span style='color:gray'> Computer Aided Geometric Design (CAGD)</span><br></div><div class='field'>Geometrijska interpolacija krivulj in ploskev <br><span style='color:gray'> Geometric Interpolation of Curves and Surfaces</span><br></div><div class='field'>Večdimenzionalna numerična integracija <br><span style='color:gray'> Multidimensional Numerical Integration</span><br></div><div class='field'>Zlepki <br><span style='color:gray'> Splines</span><br></div></td>

<td class='subjects' itemprop="role">
<div class='field'>Izbrana poglavja iz numeričnih metod<br><span style='display: none;'> / </span>
<span style='color:gray'>Selected Topics in Numerical Mathematics</span><br></div>
<span style='display: none;'>, </span>		</td>
"""
