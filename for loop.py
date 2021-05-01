collection = {'Alejandro':22, 'Maria':27, 'Jose':62, 'Daniel':51}

for i in collection:
    print(i)

for i in collection:
    print(f'{collection[i]}')

for key,value in collection.items():
    print(f'{key} -> {value}')

collection2 = 'Jean Pierre'

for i in collection2:
    print(f'{i}',end=',')
