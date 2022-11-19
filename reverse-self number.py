def reverse(n):
    r=0
    while(n):
        r1=n%10
        r=r*10+r1
        n=n//10
        s=r*10
    return r

x=int(input())

y=reverse(x)
if(x==y):
    print("YES")
else:
    print("NO")


