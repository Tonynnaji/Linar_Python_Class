#Build a Python structure with four rooms and one toilet with the customer specifying the dimensions of the rooms of the house;
#Rm1 is 8 by 5,#Rm2 is 8 by 3, #Rm3 is 9 by 7, #Rm4 is 10 by 16, #Toilet is 2 by 4 and #Room height is 12ft.
# type1 block price = N600 (size 6x9x15),# type2 block price = N1000 (size 10x12x20),#Find the total number of blocks?, #Find the cost of the building?

import math

name = 'Mr Sani'
print(f'Welcome to Linar Project {name}')
Dimension_rm1 = {'h1':int(input('Enter dimension for room 1\nEnter height:  ')),'b1':int(input('Enter_breadth:  '))}
Dimension_rm2 = {'h2':int(input('Enter dimension for room 2\nEnter height:  ')),'b2':int(input('Enter_breadth:  '))}
Dimension_rm3 = {'h3':int(input('Enter dimension for room 3\nEnter height:  ')),'b3':int(input('Enter_breadth:  '))}
Dimension_rm4 = {'h4':int(input('Enter dimension for room 4\nEnter height:  ')),'b4':int(input('Enter_breadth:  '))}
Dimension_Toilet = {'h5':int(input('Enter dimension for toilet\nEnter height:  ')),'b5':int(input('Enter_breadth:  '))}



room_height = 12

#Calculating for Rm1 using type1 block

type1_block_height = 0.75 #the height of the block have been converted to feet
type1_block_breadth = 1.25 #the breadth of the block have been converted to feet
a1 = room_height/type1_block_height
e1 = Dimension_rm1['h1']/type1_block_height
c1 = math.ceil(e1)
d1 = (c1*a1)*2
e12 = Dimension_rm1['b1']/type1_block_breadth
c12 = math.ceil(e12)
d12 = (c12*a1)*2
no_of_type1_blocks_rm1 = d1 + d12+ int(20)
cost_for_type1_rm1 = no_of_type1_blocks_rm1*600
print(f'The no of blocks Rm1: {no_of_type1_blocks_rm1}')
print(f'The cost for type1 Rm1: {cost_for_type1_rm1}')


#Calculating for Rm1 using type2 block

type2_block_height = 1 #the height of the block have been converted to feet
type2_block_breadth = 1.67 #the breadth of the block have been converted to feet
ab1 = room_height/type2_block_height
eb1 = Dimension_rm1['h1']/type2_block_height
cb1 = math.ceil(eb1)
db1 = (cb1*ab1)*2
eb12 = Dimension_rm1['b1']/type2_block_breadth
cb12 = math.ceil(eb12)
db12 = (cb12*ab1)*2
no_of_type2_blocks_rm1 = db1 + db12+ int(20)
cost_for_type2_rm1 = no_of_type2_blocks_rm1*1000
print(f'The no of blocks for Rm1: {no_of_type2_blocks_rm1}')
print(f'The cost for type2 Rm1: {cost_for_type2_rm1}')


#Calculating for Rm2 using type1 block

type2_block_height = 0.75 #the height of the block have been converted to feet
type2_block_breadth = 1.25 #the breadth of the block have been converted to feet
a2 = room_height/type1_block_height
e2 = Dimension_rm2['h2']/type1_block_height
c2 = math.ceil(e2)
d2 = (c2*a2)*2
e22 = Dimension_rm2['b2']/type1_block_breadth
c22 = math.ceil(e22)
d22 = (c22*a2)*2
no_of_type1_blocks_rm2 = d2 + d22+ int(20)
cost_for_type1_rm2 = no_of_type1_blocks_rm2*600
print(f'The no of blocks for Rm2: {no_of_type1_blocks_rm2}')
print(f'The cost for type1 Rm2: {cost_for_type1_rm2}')


#Calculating for Rm2 using type2 block

type1_block_height = 1 #the height of the block have been converted to feet
type1_block_breadth = 1.67 #the breadth of the block have been converted to feet
ab2 = room_height/type2_block_height
eb2 = Dimension_rm2['h2']/type2_block_height
cb2 = math.ceil(eb2)
db2 = (cb1*ab1)*2
eb22 = Dimension_rm2['b2']/type2_block_breadth
cb22 = math.ceil(eb22)
db22 = (cb22*ab2)*2
no_of_type2_blocks_rm2 = db2 + db22+ int(20)
cost_for_type2_rm2 = no_of_type2_blocks_rm2*1000
print(f'The no of blocks for Rm2: {no_of_type2_blocks_rm2}')
print(f'The cost for type2 Rm2: {cost_for_type2_rm2}')

#Calculating for Rm3 using type1 block

type1_block_height = 0.75 #the height of the block have been converted to feet
type1_block_breadth = 1.25 #the breadth of the block have been converted to feet
a3 = room_height/type1_block_height
e3 = Dimension_rm3['h3']/type1_block_height
c3 = math.ceil(e3)
d3 = (c1*a1)*2
e32 = Dimension_rm3['b3']/type1_block_breadth
c32 = math.ceil(e32)
d32 = (c32*a3)*2
no_of_type1_blocks_rm3 = d3 + d32+ int(20)
cost_for_type1_rm3 = no_of_type1_blocks_rm3*600
print(f'The no of blocks for Rm3: {no_of_type1_blocks_rm3}')
print(f'The cost for type1 Rm3: {cost_for_type1_rm3}')

#Calculating for Rm3 using type2 block

type1_block_height = 1 #the height of the block have been converted to feet
type1_block_breadth = 1.67 #the breadth of the block have been converted to feet
ab3 = room_height/type2_block_height
eb3 = Dimension_rm3['h3']/type2_block_height
cb3 = math.ceil(eb3)
db3 = (cb1*ab1)*2
eb32 = Dimension_rm3['b3']/type2_block_breadth
cb32 = math.ceil(eb32)
db32 = (cb32*ab3)*2
no_of_type2_blocks_rm3 = db3 + db32+ int(20)
cost_for_type2_rm3 = no_of_type2_blocks_rm3*1000
print(f'The no of blocks for Rm3: {no_of_type2_blocks_rm3}')
print(f'The cost for type2 Rm3: {cost_for_type2_rm3}')

#Calculating for Rm4 using type1 block

type1_block_height = 0.75 #the height of the block have been converted to feet
type1_block_breadth = 1.25 #the breadth of the block have been converted to feet
a4 = room_height/type1_block_height
e4 = Dimension_rm4['h4']/type1_block_height
c4 = math.ceil(e4)
d4 = (c4*a4)*2
e42 = Dimension_rm4['b4']/type1_block_breadth
c42 = math.ceil(e42)
d42 = (c42*a4)*2
no_of_type1_blocks_rm4 = d4 + d42+ int(20)
cost_for_type1_rm4 = no_of_type1_blocks_rm4*600
print(f'The no of blocks for Rm4: {no_of_type1_blocks_rm4}')
print(f'The cost for type1 Rm4: {cost_for_type1_rm4}')

#Calculating for Rm4 using type2 block

type2_block_height = 1 #the height of the block have been converted to feet
type2_block_breadth = 1.67 #the breadth of the block have been converted to feet
ab4 = room_height/type2_block_height
eb4 = Dimension_rm4['h4']/type2_block_height
cb4 = math.ceil(eb4)
db4 = (cb4*ab4)*2
eb42 = Dimension_rm4['b4']/type2_block_breadth
cb42 = math.ceil(eb42)
db42 = (cb42*ab4)*2
no_of_type2_blocks_rm4 = db4 + db42+ int(20)
cost_for_type2_rm4 = no_of_type2_blocks_rm4*1000
print(f'the no of blocks for Rm4: {no_of_type2_blocks_rm4}')
print(f'The cost for type2 Rm4: {cost_for_type2_rm4}')

#Calculating for Toilet using type1 block

type1_block_height = 0.75 #the height of the block have been converted to feet
type1_block_breadth = 1.25 #the breadth of the block have been converted to feet
a5 = room_height/type1_block_height
e5 = Dimension_Toilet['h5']/type1_block_height
c5 = math.ceil(e5)
d5 = (c5*a5)*2
e52 = Dimension_Toilet['b5']/type1_block_breadth
c52 = math.ceil(e52)
d52 = (c52*a5)*2
no_of_type1_blocks_toilet = d5 + d52+ int(20)
cost_for_type1_toilet = no_of_type1_blocks_toilet*600
print(f'The no of blocks for the toilet:{no_of_type1_blocks_toilet}')
print(f'The cost for the toilet:{cost_for_type1_toilet}')

#Calculating for Toilet using type2 block

type2_block_height = 1 #the height of the block have been converted to feet
type2_block_breadth = 1.67 #the breadth of the block have been converted to feet
ab5 = room_height/type2_block_height
eb5 = Dimension_Toilet['h5']/type2_block_height
cb5 = math.ceil(eb5)
db5 = (cb5*ab5)*2
eb52 = Dimension_Toilet['b5']/type2_block_breadth
cb52 = math.ceil(eb52)
db52 = (cb52*ab5)*2
no_of_type2_blocks_toilet = db5 + db52 + int(20)
cost_for_type2_toilet = no_of_type2_blocks_toilet*1000
print(f'the no of blocks for the toilet: {no_of_type2_blocks_toilet}')
print(f'The cost for the toilet: {cost_for_type2_toilet}')

total_no_of_type1_blocks = no_of_type1_blocks_rm1 + no_of_type1_blocks_rm2 + no_of_type1_blocks_rm3 + no_of_type1_blocks_rm4 + no_of_type1_blocks_toilet
print(f'The total_no_of_type1_blocks: {total_no_of_type1_blocks}')
total_cost_for_type1_blocks = cost_for_type1_rm1 + cost_for_type1_rm2 + cost_for_type1_rm3 + cost_for_type1_rm4 + cost_for_type1_toilet
print(f'total_cost_for_type1_blocks: {total_cost_for_type1_blocks}')
total_no_of_type2_blocks = no_of_type2_blocks_rm1 + no_of_type2_blocks_rm2 + no_of_type2_blocks_rm3 + no_of_type2_blocks_rm4 + no_of_type2_blocks_toilet
print(f'total_no_of_type2_blocks: {total_no_of_type2_blocks}')
total_cost_for_type2_blocks = cost_for_type2_rm1 + cost_for_type2_rm2 + cost_for_type2_rm3 + cost_for_type2_rm4 + cost_for_type2_toilet
print(f'total_cost_for_type2_blocks: {total_cost_for_type2_blocks}')
Total_no_blocks = total_no_of_type1_blocks + total_no_of_type2_blocks
print(f'Total_no_blocks: {Total_no_blocks}')
Total_cost = total_cost_for_type1_blocks + total_cost_for_type2_blocks
print(f'Total_cost: {Total_cost}')