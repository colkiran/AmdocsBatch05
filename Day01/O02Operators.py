
"""
arithmetic
comparison
boolean
augmentor
bitwise
ternary
"""

print("arithmetic".center(40, "-"))
print(f"add : 10 + 3 = {10 + 3}")
print(f"sub : 10 - 3 = {10 - 3}")
print(f"mul : 10 * 3 = {10 * 3}")
print(f"div : 10 / 3 = {10 / 3}")
print(f"flr_div : 10 // 3 = {10 // 3}")
print(f"mod : 10 % 3 = {10 % 3}")
print(f"exp : 10 ** 3 = {10 ** 3}")

print("augmentor".center(40, "-"))
# =, +=, *=, /=, *=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 5
print(f"x :{x}")

print("-" * 40)
print(f"ord('A') :{ord('A')}")     # integer representation of unicode char
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")

print("coparison".center(40, "-"))
# ==, >, >=, <, <=, !=
a = 10
b = 15

print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Boolean".center(40, "-"))
# and, or, not

print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")

print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")

print(f"not(1 == 1 or 2 == 2) :{not(1 == 1 or 2 == 2)}")
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")

print("bitwise operators".center(40, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1: {5 >> 1}")

print("ternary".center(40, "-"))
age = 18
print("Eligible" if age >= 18 else "Not Eligible")
