    
def Pythagorean(x,y,z):
    if(x**2==(y**2+z**2)):
        return True
    else:
        return False
def func(n):
    for i in range(1,(n//2)):
        for j in range(i+1,(n)):
            k=n-(i+j)
            if(k<=j):
                break
            if(Pythagorean(k,i,j)):
                return(k,i,j)
    return (0,0,0)

n=int(input())

x=func(n)
x=tuple(sorted(x))
(a,b,c)=x
if(a==0 and b==0 and c==0):
    print("Impossible")
else:
    print(a,b,c)