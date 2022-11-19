def j(n):
    if(n==1 or n==2):
        return 1
    if(n%2==0):
        return (2*j(n//2))-1
    else:
        return (2*j(n//2))+1

n=int(input())
print(j(n))

