from cs50 import get_int

def main():
    height = getHeight()
    for i in range(height):
        print("#")

def getHeight():
    while True:
        try:
            n = int(input("Height: "))
            if(n > 0):
                return n
        except ValueError:
            print("Not an integer")
main()
