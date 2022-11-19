def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

n=int(input())
mydict=dict()
j=2
k=1
mydict[1]=1
mydict[2]=2
for i in range(3,n+1):
    mydict[i]=mydict[j]+mydict[k]
    k=j
    j=i
    if(mydict[i]>=n):
        break
#mydict.popitem()
lst=list()
mydict2=sort_dict_by_value(mydict,True)

for x,y in mydict2.items():
    if(n>=y):
        n=n-y
        lst.append(x)
        if(n<=0):
            break
print(lst[0],end='')
for i in lst[1:]:
    print(" ",i,end='')