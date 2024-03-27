#class assignment on 5 coding examples of String Indexing and String Slicing

#String Indexing
#1. 
#each element in the string corresponds to index number 0 - 24
txt = "hello! welcome to my world."
print(len(txt)) #finding the length of the string
x = txt.islower() #Return True if the string is a lowercase string, False otherwise.
print(x) 
x = txt.isupper() #Return True if the string is an uppercase string, False otherwise.
print(x)
x = txt.isalpha() #Return True if the string is an alphabetic string, False otherwise.
print(x) 
x = txt.isalnum() #Return True if the string is an alpha-numeric string, False otherwise
print(x) 
x = txt.index('e') #finding the index number where the substring is found
print(x)


#2. 
#each element in the string corresponds to index number 0 - 28
txt1 = "Hello! welcome to my World."
txt2 = "to"
result = txt1.index(txt2) #finding the index number where the substring is found
print(result)


#3. 
#each element in the string corresponds to index number 0 - 28
txt1 = "Hello! welcome to my World."
txt2 = " "
result = txt1.index(txt2) #finding the index number where the substring is found
print(result)


#4. 
#each element in the string corresponds to index number 0 - 28
txt1 = "Hello! welcome to my World."
index = 21
txt2 = txt1[index] #finding the element in index number 21
print(txt2)


#5. 
#each element in the string corresponds to index number 0 - 28
txt1 = "Hello! welcome to my World."
index = -2
txt2 = txt1[index] #finding the element in negative index number -2
print(txt2)


#String slicing
#1.
#each element in the string corresponds to index number 0 - 24
txt = "Hello! welcome to my World."
print(txt1[0:6]) #it will slice element of index from 0 to 6


#2.
#each element in the string corresponds to index number 0 - 24
txt = "Hello! welcome to my World."
print(txt1[7:14]) #it will slice element of index from 7 to 14


#3.
#each element in the string corresponds to index number 0 - 24
txt = "Hello! welcome to my World."
print(txt1[15:17]) #it will slice element of index from 15 to 17

#4.
#each element in the string corresponds to index number -1 to 25
txt = "Hello! welcome to my World."
print(txt1[-6:]) #it will slice element from index -6 to the end 


#5.
#each element in the string corresponds to index number -1 to 25
txt = "Hello! welcome to my World."
print(txt1[0:]) #it will slice element from index 0 to the end