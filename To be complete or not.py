def Divisor(n):
    lst=list()
    for i in range(1,n):
        if(n%i==0):
            lst.append(i)
    return lst
n=int(input())
sum=0
for i in Divisor(n):
    sum=sum+i
if(sum==n):
    print("YES")
else:
    print("NO")
