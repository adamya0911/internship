sname= input("enter your name")
sroll= int(input("enter your roll number"))
maths= int(input("enter marks in maths"))
english=int(input("enter marks in english"))
science=int(input("enter marks in science"))
total=maths+science+english
avg= (maths+science+english)/3
print(f"total marks is {total}")
print(f"average marks is {avg:.2f}")
if avg>=90 and 100>=avg:
    print ("Your grade is A+")
elif avg<90 and avg>=80:
    print ("Your grade is A")
elif avg<80 and avg>=70:
    print ("Your grade is B")
elif avg<70 and avg>=60:
    print ("Your grade is C")
elif avg<60:
    print ("Your grade is F")
    
    
