# n=int(input())
# lst=list()
# while(n!=0):
#     r=n%10
#     n=n//10
#     lst.append(r)
# lst.reverse()
# for i in lst:
#     print(i,end=': ')
#     for j in range(i):
#         print(i,end='')
#     print()

n=input()
lst=list(n)
for i in lst:
    print(i,end=': ')
    for j in range(int(i)):
        print(i,end='')
    print()
