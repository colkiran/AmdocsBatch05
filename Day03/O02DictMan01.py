
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'Michael', 'age': 35, 'desig': 'MGR', 'dept': 'finance'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('age', 32), ('runs', 82), ('oppn', 'Aus')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='Bob', age=28, desig="Mkt Exe" ,dept='MKT')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
player = {'name': 'sachin', 'age': 32, 'runs': 98, 'oppn':'Aus'}
print(f"player :{player}")

print("-" * 40)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 40)
# iterate
for x in player:
    print(x, "=>", player[x])

print("-" * 40)
# modify
print(f"player :{player}")

player['runs'] = 105
player['oppn'] = 'Sri lanka'
player['venue'] = "Gale"

print(f"player :{player}")

print("-" * 40)
# delete
del player['age']
del player['venue']

print(f"player :{player}")

print("-" * 40)
print(dir(player))
