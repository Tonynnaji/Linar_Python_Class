# write 4 examples of code implementing while loop

#1. #using while loop to count numbers
i = 0
while i < 5:
    print(i)
    i +=1


#2. #using while loop with a list
cities = ["London", "Istanbul", "Houston", "Rome"]
i = 0
while i < len(cities):
    print(cities[i])
    i += 1


#3. #using while loop to print a number series
n = 10
while n <= 100:
    print(n, end = " ," )
    n = n + 10


##4. using while loop to break a statement
n = 1
while n < 5:
    print("Hello Class")
    n = n + 1
    if n == 3:
        break
    

