# ch=chr(112)
# i=ord('!')
# j=ord('z')
# print(i,j)



def ascicode():
    lstchr=list()
    for j in range(65,91):
        lstchr.append(chr(j))
    return lstchr
def Punctuation():
    
    lstchr=list()
    for j in range(0,65):
        lstchr.append(chr(j))
    for j in range(91,98):
        lstchr.append(chr(j))
    for j in range(123,150):
        lstchr.append(chr(j))

    return lstchr

def check(lst):
    Vowels=['a','e','o','i','u','y']
    lst1=Punctuation()
    lst=list(lst)
    lst.reverse()
    while(lst):
        j=lst.pop()
        if(j in Vowels or j in lst1):
            if(len(lst)<5):
                    return False
    return True

def checkupper(lst):
    lstchr=ascicode()
    for i in lst:
        if( i in lstchr):
             return False
    return True
s=input()
lst=list()
falstlist=list()
for i in s:
    lst.append(i)
    if(i==' 'or i==''):
        lst.pop()
        if(len(lst)>=5):
            if(check(lst)):
                if(checkupper(lst)):
                    s1 = ''.join(x for x in lst)
                    falstlist.append(s1)
        lst=[]

if(len(falstlist)!=0):
    print(falstlist[0],end='')       
    for i in falstlist[1:]:
        print(" ",i,end='')


# for i in range(550):
#     print(chr(i))
