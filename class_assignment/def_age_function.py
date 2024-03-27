#class assignment using age function on voting decision.

def agefunction (user_name = input("Enter your name?\n"),Y_O_B = int(input("Enter your year of birth?\n")), voting_year = int(input("Enter the election year?\n"))):
    """ This function helps to calculate the User_age for Eleectoral purposes """
    print(f'hello {user_name} Welcome to 2023 State Election!')
    voting_age = voting_year - Y_O_B
    print(f"your age is {voting_age}")
    if voting_age <= 18 + voting_year:
        print("You are not eligible to vote")
    else: voting_age >= 18
    print("You are Eligible to vote")
    print("Oh sorry come back in the next election")

agefunction()

def voting_year(election_year = 2023):
        """ this means that function will take election year as parameter when the function is called """
        election_year += 4
        print(f'Next voting_year({election_year})')
        election_year += 4
        print(f'Next voting_year({election_year})')
        election_year += 4
        print(f'Next voting_year({election_year})')
        return election_year

    
    
voting_year() 