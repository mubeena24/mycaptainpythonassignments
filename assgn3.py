import operator
def most_frequent(b):
    d1={}
    
    for key in b:
        if key not in d1:
            d1[key]=1
        else:
            d1[key]+=1
    sort_d1=sorted(d1.items(),key=lambda x :x[1],reverse=True)           
    print(sort_d1)
   
    
             
    

print("enter the string")

a = str(input())
most_frequent(a)



    
    
