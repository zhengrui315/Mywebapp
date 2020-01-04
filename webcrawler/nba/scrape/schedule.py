import json
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

session = HTMLSession()
url = "https://stats.nba.com/schedule/#!?Month=4"
r = session.get(url)
r.html.render()
html0 = r.html.find('body > main > div.stats-container__inner > div > div.row > div > div', first=True)

# print(team_list)
html = bs(html0.html, 'html.parser')
schedule = html.find_all('section', class_='schedule-content')

data = {}
for day in schedule:
    date = day.get('data-game-day')
    data[date] = []
    for game in day.find_all(class_='schedule-game__content'):
        tmp = []
        tmp.append(game.find('span').get_text())
        tmp.extend([x.get_text() for x in game.find_all(class_='game_game-url')])
        tmp.extend([x.get_text() for x in game.find_all(class_='schedule-game__arena-name')])
        data[date].append(tmp)
print(data)
with open('../nbadata/schedule_jan.json', 'w') as f:
    json.dump(data, f)