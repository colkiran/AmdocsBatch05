
n = 0
for i in range(150, 49, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        n += 1
print("\nThere are" , n ,"prime numbers between 150 and 50")





"""
lower = 50
upper = 150
ctr = 0
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:               
                break
        else:
            print(num)
            ctr += 1

print("count of prime number is :",ctr)

"""
print("\n", "=" * 40, "\n")

for i in range(2, 21, 2):
    print(i, end=" ")
