def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("enter + for addition")
print("enter - for subtraction")
print("enter * for multiplication")
print("enter / for division")
num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
operation=input("enter operation: ")
if operation=='+':
    result = add(num1,num2)
    print (result)
elif operation=='-':
    result = sub(num1,num2)
    print (result)
elif operation=='*':
    result = mul(num1,num2)
    print (result)
elif operation=='/':
    result = div(num1,num2)
    print (result)
else:
    print ("invalid operation")
