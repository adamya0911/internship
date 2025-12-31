'''
print ("welcome to machhapuchhre bank")
user_input=input ("enter 1 for deposit or enter 2 for withdraw")
total_balance=10000
if user_input=="1":
  a=input ("how much do you want to deposit?")
  total_balance=total_balance+int(a)
elif user_input=="2":
    b=input("how much money do you want to withdraw?")
    total_balance=total_balance-int(b)
else:
    print ("the value you have entered is invalid")
print (f"total balance is {total_balance}")
'''
print ("enter + for addition")
print ("enter - for substraction")
print ("enter * for multiplication")
print ("enter / for division")
num_1= int(input("enter first number" ))
num_2= int(input("enter second number"))
choice=input("enter operator")
if choice=="+":
    result= num_1+num_2
    if num_1==2 and num_2==2:
        result=5
elif choice=="-":
    result= num_1-num_2
elif choice=="*":
    result= num_1*num_2
    if num_1==20 and num_2==20:
        result=500
elif choice=="/":
    result= num_1/num_2
print (f"your answer is {result}")


