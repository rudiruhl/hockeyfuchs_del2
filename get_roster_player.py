from requests_html import AsyncHTMLSession
import asyncio
import json
import os

urls = []
filename = []
x = 'esv_kaufbeuren'
filename.append(f'roster_player_{x}.json')
urls.append(f'https://www.del-2.org/team/{x}/kader/')
print(urls)
print(filename)

async def player(s, url):
    r = await s.get(url)
    table = r.html.find('table')[1]

    tabledata = [[c.text for c in row.find('td')[1:]] for row in table.find('tr')][1:]
    tableheader = [[c.text for c in row.find('th')[1:]] for row in table.find('tr')][0]

    res = [dict(zip(tableheader, t)) for t in tabledata]
    return res

async def main(urls):
    s = AsyncHTMLSession()
    tasks = (player(s, url) for url in urls)
    return await asyncio.gather(*tasks)

results = asyncio.run(main(urls))

with open('data/roster/roster_player_esv_kaufbeuren.json', 'w') as f:
        json.dump(results, f)