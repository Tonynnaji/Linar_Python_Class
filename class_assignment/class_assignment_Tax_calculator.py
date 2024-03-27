#You are hired to build a Tax calculator using user details,monthly salary,and monthly expense.
#Project Tax Calculator


print("Project_Tax_Calculator")
user_name = input("what is your name? ") #name = Ade
user_age = input("Enter your age ") #user_age = 40 years
user_place_of_work = input("where is your place_of_work? ") #place_of_work = Unilever
user_level = input("Enter your_level ") #level = G 15
local_government_area = input("local_government_area ") #local_government_area = Apapa
no_of_family = input("no_of_family ") #no_of_family = 3
Monthly_salary = int(input("what is your monthly salary? ")) #salary = N500,000
Monthly_expenditure = int(input("what is your monthly expenditure? ")) #expenditure = N445.000
Leftover = Monthly_salary - Monthly_expenditure 
Tax = (Leftover * (35/100))
print("Welcome, Mr  "+ str(user_name))
print("my age is  " + str(user_age))
print("my work address is  " + str(user_place_of_work))
print("my level is  " + str(user_level))
print("my monthly local government area is  " + str(local_government_area))
print("My family size is  "+ str(no_of_family))
print("my monthly salary is  " + str(Monthly_salary))
print("my monthly expenditure is  " + str(Monthly_expenditure))
print("my leftover is  " + str(Leftover))
print("my tax is  " + str(Tax))
