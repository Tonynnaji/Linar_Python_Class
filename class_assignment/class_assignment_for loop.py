# write 4 examples of code implementing for loop


#1. #using for loop to find the sum of all numbers in a list
numbers = [2, 10, 20, 5, 15]
sum = 0
for n in numbers:
    sum += n
    print(sum)


#2. #using for loop to print the muliples of 3 using range() function
#print multiples of 3 till 20
for i in range(3,20,3):
    print(i)


#3 #using for loop in range() function
#iterating over a string
for j in range(5):
    print(j)

#4 #using zip() to iterate over two lists(fruits and colors)
fruits =["apple","banana","cherry"]
colors = ["red","yellow","green"]
for fruit, color in zip(fruits,colors):
    print(fruit, 'is', color)



