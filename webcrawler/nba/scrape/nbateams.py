### This script gets the list of NBA teams with their division info from NBA official website

import requests
import re
import json
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession


def get_team_list():
    session = HTMLSession()
    url = "https://stats.nba.com/teams/"
    r = session.get(url)
    r.html.render()
    team_list = r.html.find('.stats-team-list', first=True)

    html = bs(team_list.html, 'html.parser')
    divisions = html.find_all('section', class_='landing__leaders-category')
    data = {}
    for division in divisions:
        division_name = division.find(class_='category-header__name stats-team-list__header').get_text()
        teamnames = division.find_all('a', class_='stats-team-list__link')
        for teamname in teamnames:
            team_name = teamname.get_text().strip()
            data[team_name] = {'division': division_name}
    with open('./nbadata/team.json', 'w') as f:
        json.dump(data, f)

    return data

def get_arena_address(url):
    url = 'https://en.hispanosnba.com' + url
    response = requests.get(url)
    # Form1 > div.main.block > div.content.block > ul > li:nth-child(1)
    html = bs(response.content, 'html.parser')
    content = html.find('form').find(class_='main').find('ul').findAll('li')
    s = content[0].get_text()
    addr = re.findall('^Address: (.+)Capacity \(basketball\):', s)[0]

    return addr

def get_arena():
    url = 'https://en.hispanosnba.com/nba-arenas'

    response = requests.get(url)
    html = bs(response.content, 'html.parser')
    rows = html.find('tbody').find_all('tr')
    data = {}
    for row in rows:
        td = row.find_all('td')
        team = td[0].find('a').get_text()
        if team == 'Los Angeles Clippers':
            team = 'LA Clippers'
        arena = td[1].find('a').get_text()
        arena_link = td[1].find('a').get('href')
        address = get_arena_address(arena_link)
        data[team] = {'arena_name': arena, 'address': address}
        print(team, ' - ', arena, ' - ', address)

    with open('./nbadata/arena.json', 'w') as f:
        json.dump(data, f)

    return data




data1 = get_arena()
data2 = get_team_list()
s1 = set(data1)
s2 = set(data2)
assert len(s1) == 30
assert len(s2) == 30
assert len(s1 - s2) == 0, s1 - s2