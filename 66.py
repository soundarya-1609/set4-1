drs=int(input())
if(drs>1):
   for i in range(2,drs):
      if(drs%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
