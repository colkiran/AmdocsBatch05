
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 'four', 'five', 'six', 7.8, 8.4, 9.0, 10+5j, 10-5j, True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s4 = {1, 2, 3}

# add, update
print("add".center(40, "-"))
print(f"s4 :{s4}")

s4.add(3)
s4.add(5)
s4.add(2)
s4.add(6)
s4.add(7)
print(f"s4 :{s4}")

print("update".center(40, "-"))
s4.update([2, 3, 4])
s4.update([4, 5, 6])
s4.update([1, 2, 3])
s4.update([7, 8, 9])
s4.update([10, 1, 2])

print(f"s4 :{s4}")

# delete values - pop, remove, discard

print("pop".center(40, "-"))
print(f"s4 :{s4}")

res = s4.pop()
print(f"res :{res}")

res = s4.pop()
print(f"res :{res}")

print("remove".center(40, "-"))
s4.remove(8)
s4.remove(4)
# s4.remove(1)
print(f"s4 :{s4}")

print("discard".center(40, "-"))
s4.discard(6)
s4.discard(10)
s4.discard(1)
print(f"s4 :{s4}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print(f"A union B :{A | B}")
print(f"B union B :{B.union(A)}")

print("-" * 40)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 40)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 40)
print(f"A symmetric_difference B :{A ^ B}")
print(f"B symmetric_difference A :{B.symmetric_difference(A)}")

print("-" * 40)
# frozensets are immutable
x = frozenset([1, 2, 3, 4, 5])
print(f"x :{x}")
print(type(x))
