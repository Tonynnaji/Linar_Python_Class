
# 2048.py
# pygame_test.py
import pygame
import random
pygame.init()


# importing the logic.py file 
# where we have written all the 
# logic functions used.
import logic_2048

# Driver code
if __name__ == ' __main__':

# calling start_game function
# to initialize the matrix
    mat = logic_2048.start_game()

while(True):

    # taking the user input
    # for next step
    x = input("Press the command : ")

    # we have to move up
    if (x == 'W' or x == 'w'):

        # call the move_up function
        mat, flag = logic_2048.move_up(mat)

        # get the current state and print it
        status = logic_2048.get_current_state(mat)
        print(status)

        # if the game not over  then continue
        # and add a new two
        if(status == 'GAME NOT OVER'):
            logic_2048.add_new_2(mat)

        # else break the loop
        else:
            break
    
    # the above process will be followed 
    # in case of each type of move
    # below
        sz
    # to move down
    elif(x == 'S' or x == 's'):
        mat, flag = logic_2048.move_down(mat)
        status = logic_2048.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic_2048.add_new_2(mat)

        else:
            break
    
    # to move left
    elif(x == 'A' or x == 'a'):
        mat, flag = logic_2048.move_left(mat)
        status = logic_2048.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic_2048.add_new_2(mat)

        else:
            break
    
    # to move right
    elif(x == 'D' or x == 'd'):
        mat, flag = logic_2048.move_right(mat)
        status = logic_2048.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic_2048.add_new_2(mat)

        else:
            break

    else:
        print("Invalid Key Pressed")

    # print the matrix after each
    # move
print(mat)






 

