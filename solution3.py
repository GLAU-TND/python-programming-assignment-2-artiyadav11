def bignumber(arr):
  a,ans=[],''
  l=len(str(max(arr)))+l
  for i in arr:
    temp=str(i)*l
    a.append((temp[:1:],i))
  a.sort(reverse==true)
  for i in a:
    ans+=str(i[l])
  return ans
b=list(map(int,input().split()))
print(bignumber(b))
    
