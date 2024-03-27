#Develop a software that helps to calculate the total amount of Coaster carton a customer orders
#what the software will do;- 
#it takes your order by asking what type of coaster that is bought; 50 naira big or 20 naira small
#what carton size that is bought (small, medium, large) 
#how many cartons that is bought
#calculate the total amount to be paid for the full cartons
#calculate the total amount to be paid for the half carton

import math
math.ceil 
name = 'Ade'
print(f'Hello {name}, we will like to help you calculate the quantity of coaster biscuit and the amount')

#Using type_big_50 naira_Coaster size
big_small_carton = 4000 #45 pieces
big_medium_carton = 5500 #75 pieces
big_large_carton = 7000 #110 pieces
   
#Using type_small_20 naira_Coaster sizes
small_small_carton = 4000 #65 pieces
small_medium_carton = 5500 #100 pieces
small_large_carton = 7000 #140 pieces

#Using type_big_50 naira_Coaster half carton size
big_small_carton_half = big_small_carton/2 #half carton
big_medium_carton_half = big_medium_carton/2 #half carton
big_large_carton_half = big_large_carton/2 #half carton
   
#Using type_small_20 naira_Coaster half carton size
small_small_carton_half = small_small_carton/2 #half carton
small_medium_carton_half = small_medium_carton/2 #half carton
small_large_carton_half = small_large_carton/2 #half carton


#Calculating to the total amount of type_big_50 naira_Coaster biscuit
#Using small carton = 4000 (45 pieces)
coaster_type =input('Enter the type of 50 naira coaster biscuit: ')
carton_size = input('what carton size of type big 50 naira Coaster biscuit do you want: ')
quantity = int(input('how many small cartons of 50 naira coaster biscuit do you want: '))
cost_a = int(quantity)*4000
half_small_type_big = cost_a/2 #half carton of small type_big_Coaster biscuit

#Calculating to the total amount of type_big_50 naira_Coaster biscuit
#Using medium carton = 5500 (75 pieces)
coaster_type =input('Enter the type of 50 naira coaster biscuit: ')
carton_size = input('what carton size of type big 50 naira Coaster biscuit do you want: ')
quantity = int(input('how many medium cartons of 50 naira coaster biscuit do you want: '))
cost_b = int(quantity)*5500
half_medium_type_big = cost_b/2 #half carton of medium type_big_Coaster biscuit


#Calculating to the total amount of type_big_50 naira_Coaster biscuit
#Using large carton = 7000 (110 pieces)
coaster_type =input('Enter the type of 50 naira coaster biscuit: ')
carton_size = input('what carton size of type big 50 naira Coaster biscuit do you want: ')
quantity = int(input('how many large cartons of 50 naira coaster biscuit do you want: '))
cost_c = int(quantity)*7000
half_large_type_big = cost_c/2 #half carton of large type_big_Coaster biscuit



#Calculating to the total amount of type_small_20 naira_Coaster biscuit
#Using small carton = 4000 (65 pieces)
coaster_type =input('Enter the type of 20 naira coaster biscuit: ')
carton_size = input('what carton size of type small 20 naira Coaster biscuit do you want: ')
quantity = int(input('how many small cartons of 20 naira coaster biscuit do you want: '))
cost_d = int(quantity)*4000
half_small_type_small = cost_d/2 #half carton of small type_small_Coaster biscuit

#Calculating to the total amount of type_small_20 naira_Coaster biscuit
#Using medium carton = 5500 (100 pieces)
coaster_type =input('Enter the type of 20 naira coaster biscuit: ')
carton_size = input('what carton size of type small 20 naira Coaster biscuit do you want: ')
quantity = int(input('how many medium cartons of 20 naira coaster biscuit do you want: '))
cost_e = int(quantity)*5500
half_medium_type_small = cost_e/2 #half carton of medium type_small_Coaster biscuit

#Calculating to the total amount of type_small_20 naira_Coaster biscuit
#Using large carton = 7000 (140 pieces)
coaster_type =input('Enter the type of 20 naira coaster biscuit: ')
carton_size = input('what carton size of type big 20 naira Coaster biscuit do you want: ')
quantity = int(input('how many large cartons of 20 naira coaster biscuit do you want: '))
cost_f = int(quantity)*7000
half_large_type_small = cost_f/2 #half carton of large type_small_Coaster biscuit





print(f'The cost of small carton of 50 naira coaster biscuit = N{cost_a}:00')
print(f'The cost of medium carton of 50 naira coaster biscuit = N{cost_b}:00')
print(f'The cost of large carton of 50 naira coaster biscuit = N{cost_c}:00')
print(f'The cost of small carton of 20 naira coaster biscuit = N{cost_d}:00')
print(f'The cost of medium carton of 20 naira coaster biscuit = N{cost_e}:00')
print(f'The cost of large carton of 20 naira coaster biscuit = N{cost_f}:00')
print(f'the cost of the half carton of small_type_big = N{half_small_type_big}0')
print(f'the cost of the half carton of medium_type_big = N{half_medium_type_big}0')
print(f'the cost of the half carton of large_type_big = N{half_large_type_big}0')
print(f'the cost of the half carton of small_type_small = N{half_small_type_small}0')
print(f'the cost of the half carton of medium_type_small= N{half_medium_type_small}0')
print(f'the cost of the half carton of large_type_small= N{half_large_type_small}0')
print(f'The total cost =N{cost_a + cost_b + cost_c + cost_d + cost_e + cost_f + half_small_type_big + half_medium_type_big + half_large_type_big + half_small_type_small + half_medium_type_small + half_large_type_small}0')
print(f'Thank you Mr {name}.')