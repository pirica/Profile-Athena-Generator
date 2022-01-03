import json
import requests
import time

#print('Profile Athena Generator - by fevers')

with open(f'profile_athena.json', 'w') as x:
    with open('empty.json') as f:
        ting = json.load(f)
    json.dump(ting, x, indent = 4)

a_file = open(f"profile_athena.json", "r")
json_object = json.load(a_file)
a_file.close()

print("1: Load All cosmetics\n2: Load new cosmetics\n3: Load Pak Cosmetics")
ioption = input('>> ')

if ioption == '1':
    response = requests.get('https://fortnite-api.com/v2/cosmetics/br')
elif ioption == '2':
    response = requests.get('https://fortnite-api.com/v2/cosmetics/br/new')
elif ioption == '3':
    print('What pak do u wanna grab?')
    ask = input('>> ')
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?dynamicPakId={ask}')

if ioption == '1': # All items
    start = time.time()
    for i in response.json()['data']:
        id = i['id']
        backendtype = i['type']['backendValue']
        id = f'{backendtype}:{id}'

        json_object['items'][id] = {
            'attributes': {
                "favorite": False,
                "item_seen": True,
                "level": 1,
                "max_level_bonus": 0,
                "rnd_sel_cnt": 0,
                "variants": [],
                "xp": 0
            },
            'templateId': f'{id}'
        }
        try:
            variants = True
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']
        except:
            variants = None

        if variants == True:
            #print(i['id'])
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']

            json_object['items'][id]['attributes']['variants'] = [{
               "active": f"{active}",
               "channel": f"{channel}",
               "owned": []
            }]
            for i in i['variants'][0]['options']:
                tag = i['tag']
                json_object['items'][id]['attributes']['variants'][0]['owned'].append(
                    f'{tag}'
                )

    end = time.time()
    #print(f'Generated in {round(end - start, 2)} seconds')
            

elif ioption == '2': # New items
    for i in response.json()['data']['items']:
        id = i['id']
        backendtype = i['type']['backendValue']
        id = f'{backendtype}:{id}'

        json_object['items'][id] = {
            'attributes': {
                "favorite": False,
                "item_seen": True,
                "level": 1,
                "max_level_bonus": 0,
                "rnd_sel_cnt": 0,
                "variants": [],
                "xp": 0
            },
            'templateId': f'{id}'
        }
        try:
            variants = True
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']
        except:
            variants = None

        if variants == True:
            #print(i['id'])
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']

            json_object['items'][id]['attributes']['variants'] = [{
               "active": f"{active}",
               "channel": f"{channel}",
               "owned": []
            }]
            for i in i['variants'][0]['options']:
                tag = i['tag']
                json_object['items'][id]['attributes']['variants'][0]['owned'].append(
                    f'{tag}'
                )


elif ioption == '3': # Set items
    for i in response.json()['data']:
        id = i['id']
        backendtype = i['type']['backendValue']
        id = f'{backendtype}:{id}'

        json_object['items'][id] = {
            'attributes': {
                "favorite": False,
                "item_seen": True,
                "level": 1,
                "max_level_bonus": 0,
                "rnd_sel_cnt": 0,
                "variants": [],
                "xp": 0
            },
            'templateId': f'{id}'
        }
        try:
            variants = True
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']
        except:
            variants = None

        if variants == True:
            print(i['id'])
            channel = i['variants'][0]['channel']
            active = i['variants'][0]['options'][0]['tag']

            json_object['items'][id]['attributes']['variants'] = [{
               "active": f"{active}",
               "channel": f"{channel}",
               "owned": []
            }]
            for i in i['variants'][0]['options']:
                tag = i['tag']
                json_object['items'][id]['attributes']['variants'][0]['owned'] = [
                    f"{tag}"
                ]

a_file = open(f"profile_athena.json", "w")
json.dump(json_object, a_file, indent = 4)

#print('\nGenerated!')
#time.sleep(5)
