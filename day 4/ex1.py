'''
#positional arguements
def add(a, b):
    print(a + b)

add(10, 20)
#Keyword Arguments
#add(b=20, a=10)
#default arguements
def greet(name="User"):
    print("Hello", name)

greet()
greet("triral")
#variable length arguements
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))
#kwargs (Keyword)
def info(**details):
    print(details)

info(name="triral", age=17, country="Nepal")
#Docstring 
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

print(add.__doc__)

def add(name,age):
    print(name,age)
add(age=17,name="adamya")

def total(*numbers):
    numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]+numbers[5]
total(1,2,3,4,5,6)
print (total(1,2,3,4,5,6))

def evod(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
evod(4)
print(evod(4))


p=int(input("enter principal amount: "))
t=int(input("enter time in years: "))
r=int(input("enter rate of interest: "))
def calc_si(principal,time,rate):
    si=(principal*time*rate)/100
    return si
calc_si(p,t,r)
print("simple interest is",calc_si(p,t,r))


#pw length
password=input("enter your password ")
def pwcheck(pw):
    if len(pw)>=8:
        return "true"
    else:
        return "false"
print (pwcheck(password))

#greatest number

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))   
def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1,num2,num3
    elif num2>num1 and num2>num3:
        return num2,num1,num3
    else:
        return num3,num1,num2
result,num1,num2=greatest(a,b,c)
print(f"greatest number is {result} amongst {num1} and {num2}")


a=int(input("enter first number: "))
b=int(input("enter second number: "))

if a>b:
    print(f"greatest number is {a}")
elif b>a:
    print(f"greatest number is {b}")
else:
    print ("both are equal")

number=[1,2,3,4,5,6,7,8,9,10]
for num in number:
        if num%2==0:
            print(f"{num} is even")
            break

number=[1,2,3,4,5,6,7,8,9,10]
for num in number:
        if num%2==0:
            print (num)
'''       
