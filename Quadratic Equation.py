import math

a=float(input())
b=float(input())
c=float(input())

if(a==0 and b!=0):
    x=(-1*c)/b
    print("%.3f"%(x))
elif(a==0 and b==0):
    print("IMPOSSIBLE")
else:
    d=(b**2)-(4*a*c)
    if(d>0):
        x1=(-1*b+math.sqrt(d))/(2*a)
        x2=(-1*b-math.sqrt(d))/(2*a)
        if(x1<x2):
            print("%.3f"%(x1))
            print("%.3f"%(x2))
        else:
            print("%.3f"%(x2))
            print("%.3f"%(x1))
    elif(d==0):
        x=(-1*b)/2*a
        print("%.3f"%(x))
    else:
        print("IMPOSSIBLE")