# The data of score is from https://stats.nba.com/scores/01/04/2020
# since team name abbreviation is used, we will first generate a map between short name and full name
# found at https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations

import os
import json
from datetime import date, timedelta
import time
import logging

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver


log = logging.getLogger('game_score_scraper')
log.setLevel(logging.INFO)
# Create handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
# Add handlers to the logger
log.addHandler(c_handler)

# Create handlers
f_handler = logging.FileHandler('../logs/scraper.log')
f_handler.setLevel(logging.INFO)
# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
# Add handlers to the logger
log.addHandler(f_handler)



def get_team_abbr():
    log.info('get team abbr starts...')
    filename = '../nbadata/team_abbreviation.json'
    if os.path.isfile(filename):
        log.info(f'{filename} exists!')
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    url = "https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations"
    log.info('read the url')
    response = requests.get(url)
    html = bs(response.content, 'html.parser')
    table = html.find('table')
    data = {}
    for row in table.find('tbody').find_all('tr')[1:]:
        names = row.find_all('td')
        abbr = names[0].get_text().strip()
        full = names[1].get_text().strip()

        if full == 'Los Angeles Clippers':
            full = 'LA Clippers' # this name is used for LA Clippers throughout this project

        data[abbr] = full
    with open(filename, 'w') as f:
        json.dump(data, f)

    return data


def scrape_score(url, team_abbr):
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element_by_css_selector('#scoresPage > div.row.collapse > div.scores__inner.large-9.medium-8.columns > div > div')

    data = []
    for row in element.find_elements_by_class_name('linescores-table'):
        teams = row.find_elements_by_class_name('team-name')
        scores = row.find_elements_by_class_name('final')

        away_team = team_abbr[teams[0].text.strip()]
        home_team = team_abbr[teams[1].text.strip()]
        away_score = scores[1].text.strip()
        home_score = scores[2].text.strip()
        data.append([away_team, home_team, away_score, home_score])
    driver.close()
    return data


def get_game_score():
    filename = '../nbadata/score.json'
    if not os.path.isfile(filename):
        data = {}
    else:
        with open(filename, 'r') as f:
            data = json.load(f)

    url_prefix = 'https://stats.nba.com/scores/'
    first_day = date(2019, 10, 22)  # 2019-2020 NBA season started on 2019-10-22
    delta_day = timedelta(days=1)
    day = first_day
    team_abbr = get_team_abbr()
    while day < date.today():
        s = day.strftime('%Y-%m-%d')
        if s not in data:
            url = url_prefix + day.strftime('%m/%d/%Y')
            data[s] = scrape_score(url, team_abbr)
            log.info(f'Getting the scores on {s} successfully')
            log.info(data[s])
        day += delta_day
        time.sleep(10)

    with open(filename, 'w') as f:
        json.dump(data, f)


def main():
    get_game_score()


if __name__ == '__main__':
    main()