year=int(input("which year you want to know ?? "))

if year % 4==0 or year % 400==0 and year % 100 !=0:
    print("leap year")

else:
    print("its not a leap year")
