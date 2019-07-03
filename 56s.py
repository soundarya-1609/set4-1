ks=str(input())
p=0
l=0
m=len(k)
for i in range(0,m):
    if(ks[i].isalpha()):
       p=p+1
    if(ks[i].isnumeric()):
       l=l+1
if((p==0) or (l==0)):
    print("No")
else:
    print("Yes")
