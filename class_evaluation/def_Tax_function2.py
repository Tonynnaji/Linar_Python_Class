#class assignment to build a tax functions that the user will use to calculate his tax returns from his leftover

def welcomefunction():
    """
    This function welcomes the user

    Welcome to Lagos State 2023 Annual Tax Returns!
    """
    print("Welcome to Lagos State 2023 Annual Tax Returns!")
    #taxfunction()
    taxfunction(input("Enter your name?\n"),int(input("Enter your monthly salary?\n")),int(input("Enter your monthly expenditure?\n")))



'''
def taxfunction(user_name = input("Enter your name?\n"), monthly_salary = int(input("Enter your monthly salary?\n")),monthly_expenditure = int(input("Enter your monthly expenditure?\n"))):
    leftover = monthly_salary - monthly_expenditure
    tax_value = leftover *(35/100)
    int_taxvalue = int(tax_value)
    print(f"Your tax value is {int(tax_value)}")'''

def taxfunction(user_name, monthly_salary, monthly_expenditure):
    leftover = monthly_salary - monthly_expenditure
    tax_value = leftover *(35/100)
    int_taxvalue = int(tax_value)
    print(f"Your tax value is {int(tax_value)}")


welcomefunction()