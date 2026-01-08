'''
name="adamya"
name[2]="a"
print (name)


 #len
a="adamya" 
print (len(a))

#upper and lower

a="Adamya"
print (a.upper())
print (a.lower())

#capitalize and title

a="adamya raj aryal"
print (a.capitalize())
print (a.title())

#remove extra spaces
a="   adamya   "
print (a.strip())
print (a.lstrip())
print (a.rstrip())

#replace
a="adamya loves football"
print (a.replace("football","cricket"))

#find and index
a="adamya studies in nepal"
print (a.find("studies"))
print (a.find ("india"))

#startswith and endswith
a="adamya studies in nepal"
print (a.startswith("adamya"))
print (a.endswith("nepal"))
print (a.startswith("studies"))
print (a.endswith("india"))

#split
a="adamya raj aryal"
b=a.split()
print (b)


#join
a=["adamya","raj","aryal"]
b=" ".join(a)
print (b)

#count
a="adamya"
print (a.count("a"))

#isalpha and isdigit
a="adamya"
print (a.isalpha())
b="12345"
print (b.isdigit())
c="adamya123"
print (c.isalpha())
print (c.isdigit())
'''