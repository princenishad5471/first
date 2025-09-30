num=int(input("check prime numbers : "))

prime_num=True
if num>1:
    for i in range(2,num):
        if (num %i)==0:
            prime_num=False
            break

print(prime_num)