from requests_html import HTMLSession
import json

s = HTMLSession()

url = ''

r = s.get(url)

table = r.html.find('table')[1]

tabledata = [[c.text for c in row.find('td')[1:]] for row in table.find('tr')][1:]
tableheader = [[c.text for c in row.find('th')[1:]] for row in table.find('tr')][0]

res = [dict(zip(tableheader, t)) for t in tabledata]

with open('*.json', 'w') as f:
    json.dump(res, f)