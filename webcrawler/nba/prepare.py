""" prepare full data for NBA teams """
import json
import os
import requests

path = './nbadata'
arena_json = os.path.join(path, 'arena.json')
with open(arena_json, 'r') as f:
    arena = json.load(f)

# print(arena)

team_json = os.path.join(path, 'team.json')
with open(team_json, 'r') as f:
    team = json.load(f)
# print(team)


def get_coordinates(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': 'AIzaSyBOwGNkqldDsRmYimF4EWJH447zeZhSs3I'}
    resp = requests.get(url, params).content
    res = json.loads(resp)
    coordinates = res['results'][0]['geometry']['location']

    return {'latitude': coordinates['lat'], 'longitude': coordinates['lng']}


assert set(arena.keys()) == set(team.keys())
for t in team.keys():
    team[t].update(arena[t])
    coordinates = get_coordinates(team[t]['address'])
    team[t].update(coordinates)
    print(t)
    print(team[t])

team_full = os.path.join(path, 'team_full.json')
with open(team_full, 'w') as f:
    json.dump(team, f)

