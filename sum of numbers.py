
# import string
# def listToString(s): 
    
#     # initialize an empty string
#     str1 = "" 
    
#     # traverse in the string  
#     for ele in s: 
#         str1 += ele  
    
#     # return string  
#     return str1 


def bigger1(num1,num2):
    answer=''
    carry=0
    while(num1!='' or num2!=''or carry!=0):
        if(num1!='' and num2!=''):
            temp=int(num1[-1])+int(num2[-1])+carry
        if(num1=='' and num2==''):
            temp=carry
        if(num1=='' and num2!=''):
            if(carry==0):
                answer=num2+answer
                break
            temp=int(num2[-1])+carry
        if(num1!='' and num2==''):
            if(carry==0):
                answer=num1+answer
                break
            temp=int(num1[-1])+carry
        d=temp%10
        carry=temp//10
        answer=str(d)+answer
        num1=num1[:-1]
        num2=num2[:-1]
    return answer

n=int(input())
lst=list()
for i in range(n):
    num=input()
    lst.append(num)

for i in range(n-1):
    lst[i+1]=bigger1(lst[i],lst[i+1])
        

print(lst[n-1])




