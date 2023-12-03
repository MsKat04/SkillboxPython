import requests
import json

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")

def fetch_pilot_info(pilot_url):
    pilot_data = get_data(pilot_url)
    homeworld_data = get_data(pilot_data['homeworld'])

    return {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': homeworld_data['name'],
        'homeworld_url': pilot_data['homeworld']
    }

url = 'https://swapi.dev/api/starships/10'
starship_data = get_data(url)

pilots = [fetch_pilot_info(pilot) for pilot in starship_data['pilots']]

ship_info = {
    'ship_name': starship_data['name'],
    'starship_class': starship_data['starship_class'],
    'max_atmosphering_speed': starship_data['max_atmosphering_speed'],
    'pilots': pilots,
}

print(json.dumps(ship_info, indent=4))

with open('inf.json', 'w') as f:
    json.dump(ship_info, f, indent=4)