    
ssk=str(input())
d=list(ssk)
r=len(ssk)
p=""
if r%2==0:
  d[int(r/2)]="*"
  d[int(r/2-1)]="*"
else:
   d[int(r/2)]="*"
p=p.join(d)
print(p)
