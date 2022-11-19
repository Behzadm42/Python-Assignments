def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n
def comb(n,m):
    return fact(n)//(fact(n-m)*fact(m))
def calc(n):
    s=0
    for i in range(1,n+1):
        p=1
        for j in range (1,i):
            p=p*comb(i,j)
        s=s+p
    return s


x=int(input())
print(calc(x))