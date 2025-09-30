passord=input("create a password: ")

if len(passord)<6:
    print("password is week")
elif len(passord)<=10:
    print("password is medium")
else:
    print("password is strong")