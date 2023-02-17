
print("Hello World")
print("Hello World")

'''
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
'''

print("-" * 40)

st1 = "hello world"
print(f"st1 :{st1}")

# print(f"st1[0] :{st1[0]}")          # string are stored like lists
# st1[0] = "H"

print(f"st1[0]  :{st1[0]}")
print(f"st1[6]  :{st1[6]}")
print(f"st1[10] :{st1[10]}")

print("-" * 40)
# slicing
print(f"st1[0:5]  :{st1[0:5]}")
print(f"st1[6:11] :{st1[6:11]}")
print(f"st1[0:11] :{st1[0:11]}")
print(f"st1[0:]   :{st1[0:]}")
print(f"st1[:11]  :{st1[:11]}")
print(f"st1[:]    :{st1[:]}")

print("-" * 40)
print(f"id(st1[0]) :{id(st1[0])}")
print(f"id(st1[1]) :{id(st1[1])}")


print("-" * 40)
# reverse indexing
print(f"st1[-1]  :{st1[-1]}")
print(f"st1[-7]  :{st1[-7]}")
print(f"st1[-11] :{st1[-11]}")

print("-" * 40)
# slicing using reverse indexing
print(f"st1[-1: -6: -1]  :{st1[-1: -6: -1]}")
print(f"st1[-7: -12: -1] :{st1[-7: -12: -1]}")
print(f"st1[-1: -12: -1] :{st1[-1: -12: -1]}")
print(f"st1[-1: :-1]     :{st1[-1: :-1]}")
print(f"st1[:-12:-1]     :{st1[:-12:-1]}")
print(f"st1[::-1]        :{st1[::-1]}")

print("-" * 40)
# find if the given string is palindrome

str = "abbba"
str1 = str[::-1]
if str == str1 :
    print(f"{str} is pallindrome")
else:
    print(f"{str} is not pallindrome")

print("-" * 40)
str1 = "malayalam"
print(f"Palindrome :{str1}" if str1 == str1[::-1] else f"Not a Plalindrome :{str1}")

print("-" * 40)
print(dir(str1))

