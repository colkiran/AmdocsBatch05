
print("extend".center(40, "-"))
l1 = list(range(1, 5))
print(f"l1 :{l1}")

l1.extend([6, 7, 8])
l1.extend([9, 10, 11])
print(f"l1 :{l1}")

print("insert".center(40, "-"))
l2 = list(range(1, 6))
print(f"l2 :{l2}")

l2.insert(1, 1.5)
l2.insert(3, 2.5)
l2.insert(5, 3.5)
l2.insert(7, 4.5)
print(f"l2 :{l2}")

# remove elements from the list - pop, remove, clear
print("clear".center(40, "-"))

l1 = list(range(1, 11))
print(f"l1: {l1}")

l1.clear()
print(f"l1 :{l1}")

print("pop".center(40, "-"))
l2 = list(range(1, 11))
print(f"l2 :{l2}")

res = l2.pop(6)
print(f"res :{res}")

res = l2.pop(3)
print(f"res :{res}")

# res = l2.pop(10)
# print(f"res :{res}")

print(f"l2 :{l2}")

print("remove".center(40, "-"))
l3 = [1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  2]
print(f"l3 :{l3}")

print("-" * 40)
l3.remove(3)
l3.remove(3)
l3.remove(3)
print(f'l3 :{l3}')

# remove all 1's
while l3.count(1):
    l3.remove(1)

print(f"l3 :{l3}")

print("count".center(40, "-"))
l3 = [1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  2]
print(f"l3 :{l3}")

print("1 :", l3.count(1))
print("2 :", l3.count(2))
print("3 :", l3.count(3))
print("5 :", l3.count(5))

