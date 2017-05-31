book = open('famnit.html', 'w')

with open('header.html') as f:
    print(f.read(), file=book)

template = """<div style="position: relative; min-height: 1px; padding-right: 15px; padding-left: 15px; float: left; width: 20%;"><div class="thumbnail">
        <img style="height: 250px;" src="{0}" alt="{1}">
        <div class="caption">
          <p style="font-weight: bold; font-size: 110%;">{1}</p>
        </div>
      </div></div>"""

with open('data.csv') as f:
    for line in f:
        name, family_name, img_name = line.strip().split(';')
        print(template.format('./pictures/' + img_name, name + ' ' + family_name), file=book)

with open('footer.html') as f:
    print(f.read(), file=book)

f.close()
