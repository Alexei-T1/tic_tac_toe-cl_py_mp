from check_ import check_step

GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'

def input_o(field):
    cords = [i for st in field for i in st].count(GAMER_F)
    return cords

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