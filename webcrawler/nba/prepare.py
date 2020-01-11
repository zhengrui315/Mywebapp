""" prepare full data for NBA teams """
import json
import os
import requests


def read_secrets():
    with open('../../.env', 'r') as f:
        for l in f:
            if len(l.split('=')) == 2:
                k, v = map(lambda x:x.strip(), l.split('='))
                os.environ[k] = v


def get_coordinates(address):
    params = read_secrets()
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': os.environ.get('GOOGLEAPIKEY')}
    resp = requests.get(url, params).content
    res = json.loads(resp)
    coordinates = res['results'][0]['geometry']['location']

    return {'latitude': coordinates['lat'], 'longitude': coordinates['lng']}


def main():
    path = './nbadata'
    arena_json = os.path.join(path, 'arena.json')
    with open(arena_json, 'r') as f:
        arena = json.load(f)

    # print(arena)

    team_json = os.path.join(path, 'team.json')
    with open(team_json, 'r') as f:
        team = json.load(f)
        # print(team)

    assert set(arena.keys()) == set(team.keys())

    read_secrets() # set secrets as environment variables

    for t in team.keys():
        team[t].update(arena[t])
        coordinates = get_coordinates(team[t]['address'])
        team[t].update(coordinates)
        print(t)
        print(team[t])

    team_full = os.path.join(path, 'team_full.json')
    with open(team_full, 'w') as f:
        json.dump(team, f)
    print('success')


if __name__ == '__main__':
    main()