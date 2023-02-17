
"""
35 = 40 - 5
35 // 2 => 17
"""

print("find".center(40, "-"))

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

res1 = st1.find("w")
print(f"res1 :{res1}")

res2 = st1.find("l")
print(f"res2 :{res2}")

res3 = st1.find("l", st1.find("l", st1.find("l")+1)+1)
print(f"res3 :{res3}")

print("-" * 40)

print(f"st2 :{st2}")

res4 = st2.find("fox")
print(f"res4 :{res4}")

res5 = st2.find("the", st2.find("the")+1)
print(f"res5 :{res5}")

print("replace".center(40, "-"))

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1  :{st1}")
res1 = st1.replace("h", "H")
print(f"res1 :{res1}")

res2 = st1.replace("l", "L", 3)
print(f"res2 :{res2}")

print(f"st2 :{st2}")
res3 = st2.replace("brown fox", "white tiger")
print(f"res3 :{res3}")

res4 = st2.replace("the", "The", 1)
print(f"res4 :{res4}")

# maketrans and translate

print("maketrans".center(40,"-"))

st = "hello world"
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'
# the length of a and b should be the same
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st.translate(resTbl)
print(f"res :{res}")
