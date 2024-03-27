#list 2 examples of tuple method

#1. count()
tuple1 = (0,1,2,3,2,3,1,3,2)
tuple2 = ('python', 'java','python','for','java','python')
res = tuple1.count(2) #Return number of occurrences of value
res = tuple2.count('python') #Return number of occurrences of value
print('Count of 2 in tuple1 is : ', res)
print('Count of python in tuple2 is : ', res)


#2. 
tuple = (0,1,2,3,2,3,1,3,2)
res = tuple.index(3) #Return first index of value
print('First occurance of 3 is', res)
res = tuple.index(3,4) #Return first index of value of 3 after 4th index
print('First occurance of 3 after 4th index is:', res)

