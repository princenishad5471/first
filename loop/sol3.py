num=int(input("give the number you want mulplication table:"))

for i in range(1,11):
    if i==5:
        continue

    print(num, "X",i,"=", num*i)
    
