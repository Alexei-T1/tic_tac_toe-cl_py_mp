
from random import randint
from check_ import check_step

GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'

def input_o(field):
    x, y = (randint(0,2), randint(0,2))
    if ([i for st in field for i in st].count(GAMER_F) + [i for st in field for i in st].count(GAMER_S)) == 9:
        return
    while field[y][x] == GAMER_F or  field[y][x] == GAMER_S:
        x, y = (randint(0,2), randint(0,2))
    return x, y


    # cords = [i for st in field for i in st].count(GAMER_F)
    # if cords == 1:
    #     x, y = (randint(0,2), randint(0,2))
    #     if field[y][x] == GAMER_F:
    #         input_o(field)
    #     return x, y
    # elif cords == 2:
    #     cord_list = []
    #     for row in range(len(field)):
    #         for cord in range(len(row)):
    #             if field[row][cord] == GAMER_F:
    #                 cord_list.append((row, cord))
    #     cord1, cord2 = cord_list
        
    #     if cord1[0] == cord2[0]:
    #         if cord1[1] == 0 and cord2[1] == 2:
    #             return 1, cord1[0]
    #         elif cord1[1] == 1 and cord2[1] == 2:
    #             return 0, cord1[0]
    #         return 2, cord1[0]
    #     elif cord1[1] == cord2[1]:
    #         if cord1[0] == 0 and cord2[0] == 2:
    #             return cord1[1], 1
    #         elif cord1[1] == 1 and cord2[1] == 2:
    #             return cord1[1], 0
    #         return cord1[1], 2
    #     elif cord1 == ((cord2[0]-1),(cord2[1]-1)) or cord1 == ((cord2[0]-2),(cord2[1]-2)):
    #         if cord1[0] == 0 and cord2[0] == 2:
    #             return 1,1
    #         elif cord1[0] == 1 and cord2[0] == 2:
    #             return 0,0
    #         return 2,2
    #     elif cord1 == ((cord2[0]-1),(cord2[1]+1)) or cord1 == ((cord2[0]-2),(cord2[1]+2)):
    #         if cord1[0] == 0 and cord2[0] == 2:
    #             return 1,1
    #         elif cord1[0] == 1 and cord2[0] == 2:
    #             return 2,0
    #         return 0,2
    #     else:


def input_step(field, gamer_):  

    step_ = input(f"input {gamer_} x, y=  ")
    result_check = check_step(step_, field)

    while result_check == WRONG_INPUT or result_check == USED_FIELD:

        if result_check == WRONG_INPUT:
            print(f"wrong input, use number x(1,2,3),y(1,2,3)")
            
        elif result_check == USED_FIELD:
            print(f"field used, try new field")      

        step_ = input(f"input {gamer_} x, y=  ")
        result_check = check_step(step_, field)
    
    return result_check