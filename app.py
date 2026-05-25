from check_ import check_field, check_step
from draw_field import draw_field
from input import input_o

field = [[None, None, None] for i in range(3)]

GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'
GAME_END = False


draw_field(field) 

while not GAME_END:
    step_x = input(f"input {GAMER_F} x, y=  ")
    x_check_step = check_step(step_x, field)
    if x_check_step == WRONG_INPUT:
        print(f"wrong input, use number x(1,2,3),y(1,2,3)")
        continue
    elif x_check_step == USED_FIELD:
        print(f"field used, try new field")
        continue

    x, y = x_check_step
    field[y-1][x-1] = GAMER_F

    step_o = input_o(field)
    
     
    draw_field(field)


    print(step_o)
    print(x_check_step)    
    check_field(field)
    
    GAME_END = True
