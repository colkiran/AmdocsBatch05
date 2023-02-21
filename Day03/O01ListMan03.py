
print("clear".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("index".center(40, "-"))
l2 = [1, 2, 1, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 1, 2, 2]
print(f"l2 :{l2}")

print("3 :", l2.index(3))
print("3 :", l2.index(3, l2.index(3)+1))
print("3 :", l2.index(3, l2.index(3, l2.index(3)+1)+1))

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

l2 = l1             # shallow copy - copies the address along with the data

print(f"l2 before :{l2}")

l2.extend([6, 7, 8])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("\n", "-" * 40, "\n")

l3 = ['a', 'b', 'c', 'd', 'e']
print(f"l3 before :{l2}")

l4 = l3.copy()              # deep copy - copies only the data
print(f"l4 before :{l4}")

print("-" * 40)
l4.append('f')
l4.append('g')
l4.append('h')
l4.append('i')

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("\n", "-" * 40, "\n")

l5 =[1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"l5 before :{l5}")

l6 = l5.copy()
print(f"l6 :{l6}")

print(l6[4])
print("-" * 40)
l6[4].append(66)
l6[4].append(77)
l6[4].append(88)

print("-" * 40)
print(l6[4][6])
del l6[4][6]
print(f"l6 after : {l6}")
print(f"l5 after : {l5}")

print("\n", "-" * 40, "\n")
l7 = [2, 4, 6, 8, [1, 2, 3, 4, 5], 10, 12]
print(f"l7 before :{l7}")
from copy import deepcopy

l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[4].append(6)
l8[4].append(7)
l8[4].append(8)
l8[4].append(9)
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

print("sort".center(40, "-"))
# sort   -  will sort the original list
# sorted -  takes a copy of the list sorts and returns it
l1 = [9, 6, 1, 10, 8, 2, 5, 3, 7, 4, 6]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending order :{res_desc}")

print("-" * 40)

l2 = [9, 'zebra', 6, 'apple',  1,'yellow',  10, 'blue', 8, 'violet', 2, 'green', 5, 'red', 3, 'pink', 7,'cat', 4, 'dog', 6, 198, 1345, 28, 204, 2178]
print(f"l2 :{l2}")

print("-" * 40)
res = sorted(l2, key=ascii)
print(f"res :{res}")

print("-" * 40)

cities  = ['kanyakumari', 'bangalore', 'delhi', 'thiruvananthapuram', 'pune', 'chennai', 'mumbai', 'kolkota', 'hyderabad', 'vishakapatnam']

print(f"cities: {cities}")
# sort it based on the length of their names

print("-" * 40)

res= sorted(cities, key=len)
print(f"res :{res}")

print("-" * 40)

months = ['dec', 'aug', 'apr', 'nov', 'feb', 'oct', 'jan', 'may', 'mar', 'jul', 'sep', 'jun']

print(f"months :{months}")

print("-" * 40)
# sort these months
from calendar import month_abbr
print(list(month_abbr))

l = []
for mth in list(month_abbr):
    l.append(mth.lower())

# print(f"l :{l}")
def sort_months(mon):
    if mon in l:
        return l.index(mon)

print("-" * 40)
res_asc = sorted(months, key=sort_months)
print(f"Ascending :{res_asc}")

print("-" * 40)
res_desc = sorted(months, key=sort_months, reverse=True)
print(f"Descending :{res_desc}")
