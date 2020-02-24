list1=[i for i in input().split()]
n=len(list1)
list2=[]
list2.append(list1[0])
str2=list1[0]
for i in range(0,n):
    for j in range(1,n):
    str1=list1[j]
    p=len(str2)
    if str2[p-1]==str1[0]:
       list2.append(list1[j])
       str2=str1
       list1[]='*'
       break
print(list2)
    

