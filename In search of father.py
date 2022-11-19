def snumber(n):
    num=n
    sum=0
    while(num):
        r=num%10
        num=num//10
        sum=sum+r
    return sum
def prime_check(a):
    for j in range(2,a):
        if(a%j==0):
            return False
    return True
    
def sprimenumber(n):
    lst=set()
    i=2
    while(True):
        if(n%i==0):
            lst.add(i)
            n=n//i
            i=2
            if(prime_check(n) and n!=1 ):
                lst.add(n)
                break
            elif(n==1):
                break
            continue
        i=i+1
    sum=0
    for i in lst:
        sum=sum+i
    return sum
def d_x(n):
    for i in range(3,n):
        sum=sprimenumber(i)+snumber(i)+i
        if(sum==n):
            return True
            break
    return False
        


t=int(input())
lst=list()
for i in range(t):
    lst.append(int(input()))
for i in lst:
    if(d_x(i)):
        print('Yes')
    else:
        print('No')

