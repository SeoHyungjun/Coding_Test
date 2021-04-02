import requests

BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
X_AUTH_TOKEN = 'c541d130d72f6292c0f63ed640c72906'

headers = {'X-Auth-Token': X_AUTH_TOKEN}#, 'Content-Type': 'application/json'}
datas = {'problem':1}
response = requests.post(BASE_URL+'/start', data=datas, headers=headers)
print(response, response.json())
print()

AUTH_KEY = response.json()['auth_key']
print(AUTH_KEY)
print()

headers2 = {'Authorization': AUTH_KEY, 'Content-Type': 'application/json'}
Locations_API = requests.get(BASE_URL+'/locations', headers=headers2)
print(Locations_API, Locations_API.json()['locations'])
print()

print('\ntrucks')
Trucks_API = requests.get(BASE_URL+'/trucks', headers=headers2)
print(Trucks_API, Trucks_API.json()['trucks'])

print('\nsimulate')
for i in range(720):
    #datas = {'commands' : [{ "truck_id": 0, "command": [2, 5, 4, 1, 6] },{ "truck_id": 1, "command": [2, 5, 4, 1, 6] },{ "truck_id": 2, "command": [2, 5, 4, 1, 6] }, { "truck_id": 3, "command": [2, 5, 4, 1, 6] }, { "truck_id": 4, "command": [2, 5, 4, 1, 6] }]}
    #datas = {'commands' : [{ "truck_id": 0, "command": [2, 5, 4, 1, 6] }]}
    datas = {'commands':[{'truck_id':0, 'command':[]}, {'truck_id':1, 'command':[]}, {'truck_id':2, 'command':[]}, {'truck_id':3, 'command':[]}, {'truck_id':4, 'command':[]}]}
    Simulate_API = requests.put(BASE_URL+'/simulate', json=datas, headers=headers2)
    print(Simulate_API, Simulate_API.json())#, Simulate_API.json()['status'])

print('\nscores')
Score_API = requests.get(BASE_URL+'/score', headers=headers2)
print(Simulate_API, Simulate_API.json())