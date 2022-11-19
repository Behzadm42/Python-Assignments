
def prime_check(a):
    for j in range(2,a):
        if(a%j==0):
            return False
    return True
a=int(input())
b=int(input())
if(a==b):
    if(prime_check(a)):
        print(a)
else:
    lst=list()
    if(a>b):
        temp=a
        a=b
        b=temp
    for i in range(a+1,b):
        if(prime_check(i)):
            lst.append(i)
    str1=str(lst[0])
    for i in lst[1:]:
        str1+=','+str(i)
    print(str1)
