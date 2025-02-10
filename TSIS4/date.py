import datetime as d
'''Task1 Subtraction'''
x = d.datetime.now()
delt = d.timedelta(days = 5)
prevX = x - delt
print(prevX.strftime("%d-%m-%Y"))

'''Task2 '''
aaa = d.datetime.now() - d.timedelta(days = 1)
bbb = d.datetime.now() + d.timedelta(days = 1)
print(f' yesterday {aaa.strftime("%d-%m-%Y")}')
print(f' today {d.datetime.now()}')
print(f' tomorrow {bbb.strftime("%d-%m-%Y")}')

'''Task3 '''
print(f'current miliseconds {d.datetime.now().strftime("%f")}')

'''Task4 '''
p = d.datetime.now()
cdate = d.datetime(2025, 2, 10, 9, 48, 34)
print(f'dif {p-d.timedelta(cdate.second)}')