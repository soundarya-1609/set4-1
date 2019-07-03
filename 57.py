zs,ks=map(int,input().split())
l=list(map(int,input().split()[:zs]))
count=0
for i in l:
   if(i==ks):
      count=count+1
print(count)      
