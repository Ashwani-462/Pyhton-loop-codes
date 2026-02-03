#prime_with_append
n=int(input("Enter a number: "))
i=1
j=1
lis=[]
if(n>1):
    while(j<=n):
        i=n%j
        if(i==0):
            lis.append(i)
        j+=1
    a=len(lis)
    if(a==2):
        print(n,"is prime number.")
    else:
        print(n,"is not prime number.")
else:
    print(n,"is not prime.")
