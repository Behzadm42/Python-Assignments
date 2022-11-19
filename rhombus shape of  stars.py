n=int(input())

for i in range(1,n+1,2):
    s=((n-i)//2)*' '+i*'*'+(n-i)*' '+i*'*'
    print(s)
y=list(range(1,n,2))
y.reverse()
for i in y:
    s=((n-i)//2)*' '+i*'*'+(n-i)*' '+i*'*'
    print(s)