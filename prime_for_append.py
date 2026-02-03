n=int(input("Enter a number: "))
j=1
lis=[]
if(n>1):
    for i in range(1,n+1):
        j=n%i
        if(j==0):
            lis.append(j)
    a=lis.count(0)
    if(a==2):
        print(n,"is prime number")
    else:
        print(n,"is not prime number")
else:
    print(n,"is not prime number.")