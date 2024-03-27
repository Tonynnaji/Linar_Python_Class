#List 10 examples of strings methods in Python


#1.  #upper()
message = 'python is fun'
print(message.upper()) #returns copy of the string converted to uppercase

#2. #lower()
string = 'THIS SHOULD BE LOWERCASE!'
print(string.lower()) #returns copy of the string converted to lowercase

#3. #capitalise()
greetings = 'good morning class.'
print(greetings.capitalize()) #returns copy of the string converted to capitalise

#4. #isnumeric()
mystr = 'hello to the world'
print(mystr.isnumeric()) #returns True if the string is a numeric string, False otherwise


#5. #endswith
txt = 'Hello, welcome to my world.'
x = txt.endswith(".") #Return True if the string is a lowercase string, False otherwise.
print(x) 

#6. #isupper()
txt = 'PYTHON IS AWESOME!'
x = txt.isupper() #Return True if the string is an uppercase string, False otherwise.
print(x)

#7. #islower()
txt = 'PYTHON IS AWESOME!'
x = txt.islower() #Return True if the string is a lowercase string, False otherwise.
print(x) 

#8. #isalpha()
txt = '12346890'
x = txt.isalpha() #Return True if the string is an alphabetic string, False otherwise.
print(x) 

#9. #isalnum()
txt = 'PYTHON'
x = txt.isalnum() #Return True if the string is an alpha-numeric string, False otherwise
print(x) 

#10. isdecimal()
txt = '12346890'
x = txt.isdecimal() #Return True if all characters in the string are decimal, False otherwise.
print(x) 

# List 3 examples of integer methods in Python
#1. #bit_length()
int = 3242342093423
print(int.bit_length)

#2. #bit_count()
int = 19
print(int.bit_count)

#3. #as_integer_ratio
int = 600
print(int.as_integer_ratio)



#List 3 examples of float methods in Python
#1. #conjugate()
float = 20.4
print(float.conjugate)

#2. #hex
float = 200.65
print(float.hex)

#3. #fromhex
float = 15.80
print(float.fromhex)

