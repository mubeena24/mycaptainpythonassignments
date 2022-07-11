print("enter the value upto which the fibonacci numbers are supoosed to be printed")
n =int(input())
f1=0
f2=1
count=0
if n <=0 :
    print("enter only positive numbers")
elif n==1:
    print(f1)
else:
    while count<n:
        print(f1)
        f3 = f1+f2
        f1=f2
        f2=f3
        count+=1
        
  
      