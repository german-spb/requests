#========================== 1-й способ решения ============================
import requests
response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
res = response.json()
names = []
intelligence = []
for i in range(len(res)):
     if res[i]['name'] == 'Hulk' or res[i]['name'] == 'Thanos' or res[i]['name'] == 'Captain America':
        names.append(res[i]['name'])
        intelligence.append(res[i]['powerstats']['intelligence'])
names_dic = dict(zip(names, intelligence))
#print(names_dic)
if names_dic['Captain America'] > names_dic['Hulk'] and names_dic['Captain America'] > names_dic['Thanos']:
    print('Captain America')
if names_dic['Hulk'] > names_dic['Thanos'] and names_dic['Hulk'] > names_dic['Captain America']:
    print('Hulk')
else:
    print('Самый умный из трёх супергероев - Thanos')

#========================== 2-й способ решения ============================

import requests
class Intelligence:
    def __init__(self, name):
        self.name = name

    def find_intelligence(self, name):
        response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
        res = response.json()
        for i in range(len(res)):
            if res[i]['name'] == self.name:
               intelligence = res[i]['powerstats']['intelligence']
               return f'IQ {self.name} составляет {intelligence}'
    def __gt__(self, other):
        if not isinstance(other, Intelligence):
               print('нет в списке!')
               return
        return self.find_intelligence(self.name) > other.find_intelligence(self.name)

if __name__ == '__main__':
    hulk = Intelligence("Hulk")
    thanos = Intelligence("Thanos")
    captain_america = Intelligence("Captain America")
    print(hulk.find_intelligence("Hulk"))
    print(thanos.find_intelligence("Thanos"))
    print(captain_america.find_intelligence("Captain America"))
    if hulk > thanos and hulk > captain_america:
        print("Hulk самый умный супергерой")
    if captain_america > hulk and captain_america > thanos:
        print("Captain America самый умный супергерой ")
    else:
        print("Thanos самый умный супергерой")
