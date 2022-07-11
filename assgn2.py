l1=[];
n = int(input("enter the number elements in the list: "))
print("enter the list from which u want positive numbers")

for i in range(0,n):
    ele = int(input())
    l1.append(ele);
    
print("the positive numbers in the range are :")

for i in range(0,n):
    if l1[i]>0:
        print(l1[i])    
    
    