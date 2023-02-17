
# formatting
print("formatting".center(40, "-"))

# c style
print("Welcome %s, what a %s player")
print("Welcome %s, what a %s player" % ("Messi", "superb"))
print("Welcome %s, with a rating of %d what a %s player" % ("Messi", 4,  "superb"))
print("Welcome %s, with a rating of %d what a %s player" % ("Messi", 4.8,  "superb"))
print("Welcome %s, with a rating of %.3f what a %s player" % ("Messi", 4.8,  "superb"))
print("Welcome %s, with a rating of %.2f what a %s player" % ("Messi", 4.8,  "superb"))

print("-" * 40)
# interpolation
gname= "Messi"
rating = 4.8
adj = "class"
print(f"Welcome {gname}, with a rating of {rating}, what a {adj} player")

# format of python
print("-" * 40)
print("Welcome {}, with a rating of {}, what a {} player".format("Messi", 4.8, "class"))
print("Welcome {0}, with a rating of {1}, what a {2} player".format("Messi", 4.8, "class"))
print("Welcome {1}, with a rating of {2}, what a {0} player".format("Messi", 4.8, "class"))
print("Welcome {gname}, with a rating of {rating}, what a {adj} player".format(gname="Messi", rating=4.8, adj="class"))
print("Welcome {gname}, with a rating of {rating:.3f}, what a {adj} player".format(gname="Messi", rating=4.8, adj="class"))

print("-" * 40)
print("{fname} {sname}".format(fname = "Sachin", sname = "Tendulkar"))
print("{fname} Tendulkar".format(fname = "Sachin"))
print("{fname:15} Tendulkar".format(fname = "Sachin"))
print("{fname:15} Tendulkar".format(fname = 100))

print("{fname:^15} Tendulkar".format(fname = "Sachin"))          # center aligned
print("{fname:>15} Tendulkar".format(fname = "Sachin"))          # center aligned
print("{fname:<15} Tendulkar".format(fname = "Sachin"))          # center aligned

print("-" * 40)
print("{fname:-^15} Tendulkar".format(fname = "Sachin"))          # center aligned
print("{fname:*>15} Tendulkar".format(fname = "Sachin"))          # center aligned
print("{fname:#<15} Tendulkar".format(fname = "Sachin"))          # center aligned
