'''
#Ask the user to input numbers until they enter 0, then print the sum of all entered numbers.
numbers=[]
total_sum=0
while True:
    num=int(input("Enter a number (0 to stop): "))
    if num==0:
        break
    total_sum=total_sum+num
print (total_sum)

a=("nepal",)
type(a)
print(type(a))  

a= set()
print(type(a))



even={2,4,6,8,10}
for num in even:
    print(num)
even.add(12)
even.update([14,16,18])
even.discard(20)
even.pop()
even.pop()
even.clear()
print(even)


student={"name":"adamya","age":16, "grade":11, "course":["igcse","alevel","ib"], "pass":True}
for key, value in student.items():
    print(f"{key} is {value}")
'''

user_details={}
create=input("do you want to create a profile (yes/no): ")
if create=="yes":
    name=input("enter your name: ")
    age=int(input("enter your age: "))
    country=input("enter your country: ")
    user_details["name"]=name
    user_details["age"]=age
    user_details["country"]=country
    print("Profile created successfully!")
else:
    print("Profile creation skipped.")
print (user_details)

