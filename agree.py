s = input("Do you agree? ")

s = s.lower()

if(s == 'y'):
    print("User agrees.")
elif(s == 'n'):
    print("User do not agree.")
else:
    print("Not valid input.")
    

if s in ["Yes","yes"]:
    print("User Agrees.")