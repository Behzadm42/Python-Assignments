# m=int(input("insert m = "))
# s=int(input("insert s = "))
def reverse(n):
    
    r1=0
    while(n):
        r=n%10
        r1=r1*10+r
        n=n//10
    return r1

m, s = input().split()
m=int(m)
s=int(s)
if(m>=1 and m<=100 and s>=0 and s<=900):
    min1='1'
    max1='9'
    a=0
    b=0

    for i in range(1,m):
        min1=min1+'0'
        max1=max1+'9'
    max_prime=min1=int(min1)
    min_prime=max1=int(max1)
    for i in range(min1,max1+1):
        sum=0
        r=0
        num=i
        while(num!=0):
            r=num%10 
            sum=sum+r
            num=num//10
            if(sum>s):
                break
        if(sum==s):
            a=i
            b=reverse(a)
            break
    for i in range(b+1,max1+1):
        sum=0
        r=0
        num=i
        while(num!=0):
            r=num%10 
            sum=sum+r
            num=num//10
            if(sum>s):
                break
        if(sum==s):
            b=i
            break
    
    if(a==0 ):
        print(-1,-1)
    
    else:
        min_prime=a
        max_prime=b
        # print(min_prime,max_prime)
        # max_prime=list1[-1]
        # min_prime=list1[0]
        print(min_prime,max_prime)
else:
    print(-1,-1)