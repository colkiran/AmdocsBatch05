
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(10, 101, 10))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
emp1 = {'ename': 'Smith', 'age': 29, 'dept': 'IT', 'desig': 'SE'},
print(f"emp1 :{emp1}")
print(type(emp1))

print("-" * 40)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
# print(f"t5 :{t5}")
# print(f"t5[0] :{t5[0]}")
# t5[0] = 100

# print(dir(t1))

t1 = tuple(range(1, 11))
print(f"t1 :{t1}")
print(type(t1))

l1 = list(t1)
print(f"l1 :{l1}")
print(type(l1))

t1 = tuple(l1)
print(f"t1 :{t1}")
print(type(t1))

