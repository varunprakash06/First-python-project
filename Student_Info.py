import csv
def write_info(info_list):
    with open('student_inf.csv', 'a',newline='')as csv_file:
        writer =csv.writer(csv_file)
        if csv_file.tell()==0: 
            writer.writerow(["Name","Age","Contact no","mail id"])
        writer.writerow(info_list)
condition = True
student_num =1
while(condition):
    Student_info = input("Enter the student information for student#{}(name age contactno email)".format(student_num))
    Student_info_list = Student_info.split(' ')
    print("\n The entered information is \n Name: {}\nAge: {} \ncontactno: {}\nemail: {}".format(Student_info_list[0],Student_info_list[1],Student_info_list[2],Student_info_list[3]))
    c_check = str(input("Is the entered information is correct? (yes/no): "))
    if c_check == "yes":
        write_info(Student_info_list)
        condition_chk = input("enter yes/no if need to add more student details")
        if condition_chk == "yes":
            condition = True
            student_name = student_name + 1
        elif condition_chk =="no":
            condition = False
    elif c_check  == "no":
        print("please enter the correct info")
