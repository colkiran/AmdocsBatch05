
print("Keys".center(40, "-"))

player = {'name': 'sachin', 'age': 32, 'runs': 105, 'oppn': 'Sri lanka', 'venue': 'Gale'}
print(f"player :{player}")

k = player.keys()
print(f"k :{k}")

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'sachin', 'age': 32, 'runs': 105, 'oppn': 'Sri lanka', 'venue': 'Gale'}
print(f"player :{player}")

print("-" * 40)
v = player.values()
print(f"v :{v}")

print("get".center(40, "-"))

player = {'name': 'sachin', 'age': 32, 'runs': 105, 'oppn': 'Sri lanka', 'venue': 'Gale'}
print(f"player :{player}")

print("-" * 40)
print(f"Name :{player.get('name', 'Invalid key, please enter a valid one')}")
print(f"year :{player.get('year', 'Invalid key, please enter a valid one')}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd']
print(f"cities :{cities}")

# convert cities into dictionary
res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 24)
print(f"res :{res}")

print("setdefault".center(40, "-"))

player = {'name': 'sachin', 'age': 32, 'runs': 105}
print(f"player :{player}")

player.setdefault('name', 'Sachin Tendulkar')
player.setdefault('runs', 145)
player.setdefault('oppn', 'Australia')

print(f"player :{player}")

print("pop".center(40, "-"))
player = {'name': 'sachin', 'age': 32, 'runs': 105, 'oppn': 'Sri lanka', 'venue': 'Gale'}
print(f"player :{player}")

res1 = player.pop('age')
print(f"res1 :{res1}")

res2 = player.pop('oppn')
print(f"res2 :{res2}")

# res2 = player.pop()
# print(f"res2 :{res2}")

print(f"player :{player}")
