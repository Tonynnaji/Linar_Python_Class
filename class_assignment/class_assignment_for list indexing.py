#class assignment on 5 coding examples of List Indexing and List Slicing

#List Indexing
#1. 
#each element in the list corresponds to index number 0 - 4
fruits = ['apples','mangoes', 'oranges', 'pear','grapes'] #element in the list corresponding to index number 1
prices = ['20','45','35','50','70']
print('fruits: ',prices)
fruits.append('avocado') #adding an element to the end of an existing fruits
print(fruits)
index = fruits.index('grapes') #element in the list corresponding to element'grape'
print(fruits[1])
print(index)



#2. 
#each element in the list corresponds to negative index number -1 to -5
fruits = ['apples','mangoes', 'oranges', 'pear','grapes'] 
print(fruits[-2]) #element in the list corresponding to negative index number -2
prices = ['20','45','35','50','70']
fruits.insert(0,prices) #inserting an element at a specific index 0
print(fruits)


#3. 
#each element in the list corresponds to index number 0 - 9
list_numbers = [1,2,3,4,5,6,7,8,9,10] 
print(list_numbers[0]) #element in the list corresponding to index number 0

#4. 
list_numbers = [1,2,3,4,5,6,7,8,9,10] 
print(list_numbers[9]) #element in the list corresponding to index number 

#5. 
#each element in the list corresponds to negative index number -1 to -10
list_numbers = [1,2,3,4,5,6,7,8,9,10] 
print(list_numbers[-9]) #element in the list corresponding to index number -9


#List slicing
#1.
#each element in the list corresponds to index number 0 - 4
animals = ['lion','Bear', 'Monkey', 'Tiger','Antelope'] 
anew = animals[4:] #it will slice element of index 4
print(anew[4:])



#2.
#each element in the list corresponds to negative index number -1 to -5
animals = ['lion','Bear', 'Monkey', 'Tiger','Antelope'] 
anew1 = animals[-3] #it will slice element from index -3 to the end 
print(anew1[-3:])
animals.remove('lion') #removing an element from the list of animals
print(animals)
animals.pop(2) #using pop to remove an element from the list of animals
print(animals)



#3. 
#each element in the list corresponds to index number 0 - 4
animals = ['lion','Bear', 'Monkey', 'Tiger','Antelope'] 
anew3 = animals[:3] #it will slice element from the beginning to index 3
print(anew3[:3])


#4.
#each element in the list corresponds to index number 0 - 4
animals = ['lion','Bear', 'Monkey', 'Tiger','Antelope'] 
list_numbers = [1,2,3,4,5,6,7,8,9,10] 
anew4 = animals[4] #it will slice element of index 4
print(anew4[4])
print(list_numbers) #list before deleting the element
del list_numbers[0:3]
print(list_numbers) #list afeter deleting the element 0 - 3

#5.
#each element in the list corresponds to index number 0 - 4
animals = ['lion','Bear', 'Monkey', 'Tiger','Antelope'] 
print(animals[1:4]) #it will slice element of index from 1 to 4
list_numbers = [1,10,3,9,5,7,2,8,4,6]
print(list_numbers) #list before sorting the element
list_numbers.sort() #decending sort
print(list_numbers) #list after sorting the element