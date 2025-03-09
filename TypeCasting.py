
# str(),int(),float() and bool()

name ="Narendra"
age =30
gpa=3.2
is_alive=True


print(type(name))
name=bool(name)
print(type(name))
print(name)

age =float(age)
print(age)

gpa=int(gpa)
print(gpa)

is_alive=str(is_alive)+" it is a string"
print(f"Its a string {is_alive}")