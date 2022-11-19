x=int(input("Insert the number = "))

# for i in range(1,x+1):
#     print((x-i)*' ',end='')
#     for j in range(1,2*i):
#         print('*',end='')
#     print()
# # y=list(range(1,x))
# # y.reverse()
# # for i in y:
# #     print((x-i)*' ',end='')
# #     for j in range(1,2*i):
# #         print('*',end='')
# #     print()
# for i in range(0,x):
#     print(i*' ',end='')
#     print(((2*(x-i))-1)*'*',end='')
    
#     print()

for i in range(1,x+1):
    l=(x-i)//2
    print(l*' ',end='')
    for j in range(i):
        print('*',end='')
    print()


