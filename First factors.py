def prime_check(a):
    for j in range(2,a):
        if(a%j==0):
            return False
    return True
def showlst(lst):
    sum=str(lst[0])
    j=lst[0]
    k=1
    lst1=list()
    for i in lst[1:]:
        if(i==j):
            k=k+1
        else:
            if(len(lst1)!=0):
                sum=sum+'^'+str(lst1[-1])
            sum=sum+'*'+str(i)
            k=1
            
        if(k!=1):
                lst1.append(k)
        
        
        j=i
    return sum
n=int(input())
lst=list()
i=2
while(True):
    if(n%i==0):
        lst.append(i)
        n=n//i
        i=2
        if(prime_check(n) and n!=1 ):
            lst.append(n)
            break
        elif(n==1):
            break
        continue
    i=i+1
        
print(lst)

