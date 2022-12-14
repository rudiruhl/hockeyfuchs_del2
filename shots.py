from requests_html import HTMLSession
import json

s = HTMLSession()
url = 'https://www.del-2.org/statistik/schuesse/133/'

r = s.get(url)

table = r.html.find('table')[0]

tabledata = [[c.text for c in row.find('td')] for row in table.find('tr')][2:]
tableheader = [[c.text for c in row.find('th')] for row in table.find('tr')][1]

data = [dict(zip(tableheader, t)) for t in tabledata]

with open('data/stats/shot_goals_all.json', 'w') as f:
        json.dump(data, f)