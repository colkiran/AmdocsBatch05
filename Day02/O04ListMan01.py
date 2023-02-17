
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.2, 8.5, 9.0, 10+1j, 10-1j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 {l3}")
print(type(l3))

print("-" * 40)
l4 = list(range(10, 101, 10))
print(f"l4 :{l4}")

# print elements
print(f"l4[4] :{l4[4]}")
print(f"l4[9] :{l4[9]}")

# iterate through the list
for i in l4:
    print(i, end=" ")
print()

print("-" * 40)
# Modification (change the exiting value or add a new value)
print(f"l4 :{l4}")
l4[5] = 600
l4[2] = 300
# l4[10] = 110
print(f"l4 :{l4}")

# delete
print("-" * 40)
del (l4[7])
del (l4[3])
print(f"l4 :{l4}")

# print("-" * 40)
# print(dir(l1))

# functions that can be used to add elements into the list
# append, extend, insert

print("append".center(40,"-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.append(11)
l1.append(12)
l1.append(13)
l1.append(14)
print(f"l1 :{l1}")

l1.append([15, 16, 17, 18, 19])
print(f"l1 :{l1}")
print(l1[14])
print(l1[14][1:4])