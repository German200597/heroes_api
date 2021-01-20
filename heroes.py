import requests
import operator

def max_intelligence():
    token = input('Введите токен: ')
    token = int(token)
    list_heroes = {}
    for id_number in range(1,10):
        data = requests.get(f'https://superheroapi.com/api/{token}/{id_number}/powerstats/get')
    
        if data.status_code != 200:
            raise Exception('не работает')
        hero_int = data.json()['intelligence']
        if hero_int == 'null':
            continue
        hero_name = data.json()['name']
        list_heroes[hero_int] = hero_name
    list_heroes=sorted(list_heroes.items(), key=operator.itemgetter(1), reverse=True) 
    print(list_heroes[0][1])
max_intelligence()

    





