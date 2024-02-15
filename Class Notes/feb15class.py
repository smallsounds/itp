print(type(10))
print(type(10.0))
print(type("hello, world"))
print(type(True))

# STATEMENT
x = 1 <= 2
print(x)

# Values, variables, operators into expressions
one = 1
two = 2
cat = one + two
print(cat)

# Python doesn't care if you use single or double quotes
print(len('neil'))

# Indexing
myName = 'neil'
print(myName[1:3])

print('yum'+'my')
print('yum' * 3)

# String with user input
str = input("Name: ")
print("Hello,", str)

str = input("Name: ")
print("Hello,", str, sep=' ')

str = input("Last Name: ")
print(f"Hello, {str}")

# Type Casting
i = int(input("What's your favorite number? "))
print(f"Your favorite number is {i}")

# Rounding errors
z = 3.14159265358979323846264338327950288419716939937510
print(f"{z}")
print(f"{z:.50f}")

# f string math, f=format
bags = 3
bananas = 12
print(f"{bananas} bananas were split into {int(bananas / bags)} groups to fit into {bags} bags.")

# t=tab, n=line
print("col1\tcol2\tcol3\ncol1\tcol2\tcol3\ncol1\tcol2\tcol3")
