import json 
with open('aboba.json') as f:
    data = json.load(f)
print('-'*19, ' ABOBA ', '-'*19)
print(' '*21, data['totalCount'])
print('°'*47)
print('DN                                                 Description           Speed    MTU ')
print('-------------------------------------------------- --------------------  ------  ------')
for i in data['imdata']:
    item = i["l1PhysIf"][ "attributes"]
    dn = item['dn']
    descript = item['descr']
    spd = item['speed']
    mtuu = item['mtu']
    print(dn, "   ", descript, "                        ", spd, " ", mtuu)