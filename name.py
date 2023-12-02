import sys

names = []

for name in range(5):
    getName = input("Names: ")
    names.append(getName)

findName = input("Finding name: ")

if findName in names:
    print("Name has been found.")
    sys.exit(0)
    
print("Not found.")
sys.exit(1)