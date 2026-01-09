student=[]
def student_create(name,age,grade):
    student_data={"name":name,"age":age,"grade":grade}
    student.append(student_data)
def student_view():
     for stu in student:
        print(f"Name: {stu['name']}, Age: {stu['age']}, Grade: {stu['grade']}")
def student_delete():
    delname=input("which students record do you want to delete?")
    for stu in student:
        if stu['name']==delname:
            student.remove(stu)
            print("record deleted successfully")

def student_update(name,age,grade):
   upname = input("which students record do you want to update?")
   for stu in student:
        if stu['name']==upname:
            ques = input("do you want to update age,name or grade?")
            if ques=="name":
                newname=input("enter new name: ")
                stu['name']=newname
            elif ques=="age":
                newage=int(input("enter new age: "))
                stu['age']=newage
            elif ques=="grade":
                newgrade=input("enter new grade: ")
                stu['grade']=newgrade
            else:
                print("invalid input")
 
def student_delete():
    delname=input("which students record do you want to delete?")
    for stu in student:
        if stu['name']==delname:
            print ("hello")
            student.remove(stu)
            print("record deleted successfully") 

def student_search():
    searchname=input("enter student name to search: ")
    for stu in student:
        if stu['name']==searchname:
            print(f"Name: {stu['name']}, Age: {stu['age']}, Grade: {stu['grade']}")
            return
    print("student not found")
   
def greet():
    """welcome to school management system"""
    print("Welcome to School Management System")
    print("Enter 0 for exit, 1 for create, 2 for view, 3 for update, 4 for delete and 5 to search student profile")
    user_choice=input("Enter your choice: ")
    return user_choice
while True:
    a=greet()
    if a=="0":
        break
    elif a=="1":
        name=input("enter student name: ")
        age=int(input("enter student age: "))
        grade=input("enter student grade: ")
        student_create(name,age,grade)
        print("student profile created successfully!")
    elif a=="2":
        student_view()
    elif a=="3":
        student_update(name,age,grade)
    elif a=="4":
        student_delete()
    elif a=="5":
        student_search()
    else:
        print("invalid choice")