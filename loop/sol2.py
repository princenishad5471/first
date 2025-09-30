Num=int(input("Give the numbers you want up to : "))

x=0
for i in range(1,Num+1):
    if i % 2==1:
        x+=1
print(x)