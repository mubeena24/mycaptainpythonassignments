import csv

def write_into_csv(info_list):
    with open('student.info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
             writer.writerow(["Name","age","contact number","e-mail id:"])
        
        writer.writerow(info_list)


if __name__=='__main__':
    condition = True
    student_num=1
    
while(condition==True):
    student_info=input("enter info for student #{} of the student in the following format (Name age contact number email id) :".format(student_num))
    
    
    student_info_list=student_info.split(' ')
    print("\nThe entered information is -\nName: {}\nage: {}\ncontact number: {}\nemail-id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    
    choice_check = input("Is the entered information right?(yes/no): ")
    if choice_check=="yes":
       write_into_csv(student_info_list) 
       
       condition_check = input("enter (yes/no) if u want to continue giving info")
       if condition_check=="yes":
             condition=True
             student_num=student_num+1
       elif condition_check=="no":
             condition=False 
    elif choice_check=="no":
        print("\nPlease re-enter the values!")
    
       
