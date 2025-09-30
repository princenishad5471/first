score=int(input("Give your score details :"))

if score>=101:
    print("Please verify your grade again")
    exit()

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")

