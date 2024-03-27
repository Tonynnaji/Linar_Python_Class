 #class assignment using age in decision making 

print("hello")
name = input("Enter your name ")
print("welcome  " + str(name) )
user_age = int(input("user_age: ")) 
if user_age >= 0 and user_age <= 2:
    print("You are an infant")
elif user_age >= 3 and user_age <= 12:
    print("You should be in kiddergatten")
elif user_age >= 3 and user_age <= 12:
    print("You should be in kiddagatten")
elif user_age >= 13 and user_age <= 19:
    print("You are a teenuser_ager")
elif user_age >= 20 and user_age <= 29:
    print("You should be in the youth class")
elif user_age >= 30 and user_age <= 49:
    print("You are a young adult")
elif user_age >= 50 and user_age <= 60:
    print("Good afternoon Sir you are welcome to the class")
elif user_age >= 61 and user_age <= 99:
    print("As a Senior Citizens you are to be taken care of by the state")
else:
    print("Invalid user_age")
    
    