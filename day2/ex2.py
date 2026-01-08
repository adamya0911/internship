name=input("Enter your name")
age=input("Enter your age")
height=float(input("enter height in meters"))
weight=float(input("enter weight in kilograms"))
gender=input("male or female?")
BMI= weight/(height**2)
if BMI<18.5:
    print("underweight")
elif 18.5 <= BMI < 24.9:
    print("normal weight")
elif 25 <= BMI < 29.9:
    print ("overweight")
elif BMI >= 30:
    print("obese")
    
