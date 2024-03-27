#Class assignment on dictionary methods

#1. #clear()
my_dict = {'1':'Ade', '2':'Sani','3':'Musa'}
my_dict.clear() #clear removes all the elements from the dictionary
print(my_dict)

#2. #get()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
print(d.get('Name')) #Return the value for key if key is in the dictionary, else default.
print(d.get('Gender'))

#3. #items()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
print(list(d.items())[1][0]) #this is a convinent way to access both the keys and values of a dictionary simultaneously.
print(list(d.items())[1][1])

#4. #keys()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
print(list(d.keys())) #Returns a veiw object with dictionary keys, allowing efficient access and iteration

#5. #values()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
print(list(d.values())) #Returns a veiw object with dictionary values, allowing efficient access and iteration

#6. #values()
d1 = {'Name':'Ade','Age':'19','Country':'Nigeria'}
d2 = {'Name':'Bayo','Age':'25'}
d1.update(d2) #
print(d1)

#7. #pop()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
d.pop('Age') #remove specified key and return the corresponding value.
print(d)

#8. #popitem()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
d.popitem() #eliminates and returnsa random (key,value) pair from the dictionary
print(d)

d.popitem() #Eliminates and returnsa random (key,value) pair from the dictionary
print(d)

#9. #keys()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
print(d.keys()) #Returns a list containing the dictionary's keys 

#10. #fromkeys()
d = {'Name':'Ade','Age':'19','Country':'Nigeria'}
print(d.fromkeys(d,None)) #Create a new dictionary with keys from iterable and values set to value.

#11 #sum()
my_dict = {'a':10,'b':20,'c':30}
total = sum(my_dict.values())
print(total)











9
