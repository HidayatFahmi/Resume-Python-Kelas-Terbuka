# Operator komparasi <, >, <=, >=, ==, !=, is, is not
# %%

a = 20 
x = 20
y = 100000
z = 100000
b = 21
c = [1, 2, 3]
d = c
e = [1, 2, 3]

print(f"a id = {id(a)}")
print(f"x id = {id(x)}")
print(f"c id = {id(c)}")
print(f"e id = {id(e)}")
print(f"id of y = {id(y)}")
print(f"id of z = {id(z)}")

print("< : ",a<b)
print("> : ",a>b)
print("<= : ",a<=b)
print(">= : ",a>b)
print("== : ",a==b)
print("is : ",c is d)
print("is : ",c is e)
print(f"y is z {y is z}")
print(f"is id y == z : {id(y) == id(z)}")
print("is not : ",c is not e)