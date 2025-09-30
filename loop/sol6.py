num=int(input("numbers you want factorial :"))
factorial=1

while num>0:
    factorial*=num
    num-=1

print(factorial)
