#class assignment on Decision making in python

age = int(input("Age: ")) 
if age >= 13 and age <= 19:
    print("you are qualified for teenage class")
elif age >= 20:
    print("you are fully qualified")
else:
    print("you are disqualied")


D_O_B = int(input("DOB"))
age = 2024 - D_O_B
if age >= 18:
    print("You are qualified for python class")
else:
    print("You are best qualified for ICT fundamentals")


Salary = int(input("Salary: "))
Big = Salary*(20/100)
Small = Salary*(12/100)
if Salary >= 50000:
    print("Save  "+ str(int(Big)))
else:
    print("Save  "+(int(Small)))
    