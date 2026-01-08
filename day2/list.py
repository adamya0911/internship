'''
#accessing listed item through index
country=["india", "nepal", "china"]
for element in country:
    print (element)
print (country[2])

country[2]="pakistan"
print (country)

country.append ("bangladesh")
print (country)
item=country.pop(1)
print (country)



#allowing user to add data using append
students=[]
n=0
while n<5:
    sname=input ("enter student name")
    students.append (sname)
    n=n+1
print (students)


games=("football","cricket","basketball","golf")
for element in games:
    print (element)
print(games[2])

games[2]="rugby"
print (games)

games.append ("baseball")
print (games)

#
number={1,2,3,4,5,5}
print (number)
print (number)
print (number)

#dictionary
student={"name": "adamya", "Age": 16, "marks": [80,90,70]}
print (student["name"])
student ["gender"]= "male"
print (student)
student.pop("name")
print (student)

#student list
student_list=[]
print ("Do you want to add records or update records?")
print ("Type 1 for adding records or 2 for updating records")
choice=int(input("press 1 or 2"))
if choice==1:
    n=0
    while n<5:
    sname= input("enter name of student")
    sage= int(input("enter age of student"))
    sgender= input("gender of student")
    n=n+1
    student_obj={"name":sname, "age":sage, "gender":sgender}
    student_list.append(student_obj)
elif choice==2:
    print ("which students record do you want to update?")
   user=input ("enter student name")
'''

    
