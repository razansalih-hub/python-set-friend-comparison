#This is my third projet with python
# Today subject is -- Set --

a = set(input("First person friends are : ").split(","))
a = {name.strip() for name in a}
b = set(input("Second person friends are : ").split(","))
b = {name.strip() for name in b}
print("*" *50)

print(f"All friends are: {a.union(b)}" )

print("""
""")

d = a.intersection(b)
print(f"The mutual friends are: {d}")

print("""
""")

e = a.difference(b)
print(f"The friends that only the first person knows: {e}")

print("""
""")

j = b.difference(a)
print("The friends that only the second person knows: {}".format(j)) 

print("""
""")

f = a ^ b 
print(f"The immutual friends are: {f}")

print("""
""")

h = a.issuperset(b)
print(f"Are all the friends of the second person are friends with the first? : {h}")

print("""
""")

k = a.issubset(b)
print(f"Are all the friends of the first person are friends with the second? : {k}")
















