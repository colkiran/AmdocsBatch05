
print("popitem".center(40, "-"))

player = {'name': 'sachin', 'age': 32, 'runs': 105, 'oppn': 'Sri lanka', 'venue': 'Gale'}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("items".center(40, "-"))
# combination of keys and values function

emp = {
    'emp1':{'ename': 'Smith', 'age': 29, 'dept': 'IT', 'desig': 'SE', 'sal': 75000},
    'emp2':{'ename': 'Steve', 'age': 32, 'dept': 'MKT', 'desig': 'BDM', 'sal': 63000},
    'emp3':{'ename': 'Tina', 'age': 30, 'dept': 'Procurement', 'desig': 'Manager', 'sal': 85000}
}

print(f"emp :{emp}")

print("-"  * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-"  * 40)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'ename': 'Smith', 'age': 29, 'dept': 'IT', 'desig': 'SE'}
emp2 = {'ename': 'Steve', 'age': 32, 'dept': 'MKT', 'sal': 63000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)

print(f"emp1 :{emp1}")
