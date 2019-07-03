ssk2=int(input())
if(ssk2>1):
   for i in range (2,ssk2):
      if(ssk2%i==0):
       print("yes")
       break
   else:
      print("no")
