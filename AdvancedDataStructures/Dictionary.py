


dic = {'k1': [2,3,4,5],'k2': (1,2), 'k3': {'key1':'Value1', 'key2':2} , 'k4': 'string', 'k5': 5}

print(dic)

print(dic['k3']['key2'])

dic2 = {i:i**2 for i in range(10)}

print(dic2)

for x in dic2.items():
    print(x)

for x in dic2.keys():
    print(x)

for x in dic2.values():
    print(x)

for x in dic2.keys():
    print(x)

for x,y in dic2.items():
    print(x)

