#class assignment using def function() to determine the user_name, school,scores,exam type, exam year and signatures 


def greet(name = input('Enter you name? \n'), school = input('Enter the name of your school \n'),year = int(input('Enter year of examination \n')),exam = input('input the type of examination \n (WAEC OR NECO)\n')):
    print(f'Hello {name}, you are a student of {school}! You took {exam} in the {year}. This software hopes to help you calculate your scores')
    if exam.upper() == 'NECO':
        neco_grading(score = int(input("Enter your NECO Score:  ")))
        neco_signatures(year)
    elif exam.upper() == 'WAEC':
        waec_grading(score =int(input("Enter your WAEC Score ")))
        waec_signatures(year)
    else:
        print("Be Sure to input the correct exam type")


def waec_grading(score):
    #score = int(input("Enter your WAEC Score:  "))
    
    """
    This function grade waec scores

    For WAEC
    0 - 39 = Fail
    40 - 44 = Poor
    45 - 49 = Pass
    50 - 59 = Good
    60 - 69 = Very Good
    70 - 100 = Excellent
    """
    if score >= 70 and score <= 100:
        print("Your grade is Excellent")
    elif score >= 60 and score <= 69:
        print("Your grade is Very Good")
    elif score >= 50 and score <= 59:
        print("Your grade is Good")
    elif score >= 45 and score <= 49:
        print("Your grade is Pass")
    elif score >= 40 and score <= 44:
        print("Your grade is Poor")
    elif score >= 0 and score <= 39:
        print("Your grade is Fail")
    else:
        print("Invalid score for WAEC")



def waec_signatures(year):
    """
    This function is used for waec signatures
    for waec_ignatures
    2000 - 2005 = Mr Ade
    2006 - 2010 = Mr Bolu
    2011 - 2015 = Mr Charles
    2016 - 2020 = Mr Deji
    2021 - 2025 = Mr Emeka
    """
    if year >= 2000 and year <= 2005:
        print("Signed by Mr Ade")
    elif year >= 2006 and year <= 2010:
        print("Signed by Mr Bolu")
    elif year >= 2011 and year <= 2015:
        print("Signed by Mr Charles")
    elif year >= 2016 and year <= 2020:
        print("Signed by Mr Deji")
    elif year >= 2021 and year <= 2025:
        print("Signed by Mr Emeka")
    else:
        print("Invalid signature for WAEC")


def neco_grading(score):
    #score = int(input("Enter your NECO Score: "))
    """

    This function grade neco scores
     For NECO
     0 - 10 = Fail
     11 - 29 = Poor
    30 - 39 =Pass
    40 - 59 = Good
    60 - 79 = Very Good
    80 - 100 = Excellent
        """
    
    if score >= 80 and score <= 100:
        print("Your grade is Excellent")
    elif score >= 60 and score <= 79:
        print("Your grade is Very Good")
    elif score >= 40 and score <= 59:
        print("Your grade is Good")
    elif score >= 30 and score <= 49:
        print("Your grade is Pass")
    elif score >= 11 and score <= 29:
        print("Your grade is Poor")
    elif score >= 0 and score <= 10:
        print("Your grade is Fail")
    else:
        print("Invalid score for NECO")

def neco_signatures(year):
    """
    This function is used for neco signatures
    for neco_signatures
    2000 - 2005 = Mr Zaki
    2006 - 2010 = Mr Yinka
    2011 - 2015 = Mr X. Uzoh
    2016 - 2020 = Mr Wale
    2021 - 2025 = Mr Victor
    """

    if year >= 2000 and year <= 2005:
        print("Signed by Mr Zaki")
    elif year >= 2006 and year <= 2010:
        print("Signed by Mr Yinka")
    elif year >= 2011 and year <= 2015:
        print("Signed by Mr X. Uzoh")
    elif year >= 2016 and year <= 2020:
        print("Signed by Mr Wale")
    elif year >= 2021 and year <= 2025:
        print("Signed by Mr Victor")
    else:
        print("Invalid signature for NECO")

greet()