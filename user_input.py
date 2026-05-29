
from random import randint
from check_ import check_step
from consts import GAMER_F, GAMER_S, USED_FIELD, WRONG_INPUT

def input_o(field):
    x, y = (randint(0,2), randint(0,2))
    
    while field[y][x] == GAMER_F or  field[y][x] == GAMER_S:
        x, y = (randint(0,2), randint(0,2))
    return x, y


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