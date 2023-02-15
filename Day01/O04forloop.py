
"""
continue
break
else
for loop is very similar to foreach loop - both depends on a collection
"""

for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 30):
    # if i > 20:
    #     break
    if i % 2 == 1:
        continue        #skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted iteration.....")
