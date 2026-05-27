from check_ import check_field
from draw_field import draw_field
from input import input_o, input_step

GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'


field = [[None, None, None] for i in range(3)]
draw_field(field) 

def game():
    GAME_END = False
    while not GAME_END:

        x_step = input_step(field, GAMER_F)
        x, y = x_step
        field[y-1][x-1] = GAMER_F

        o_step = input_o(field)
        if o_step:
            x, y = o_step
            field[y][x] = GAMER_S

        result_check = check_field(field)
        draw_field(field)
        
        if result_check:
            if result_check == GAMER_F or result_check == GAMER_S:
                print(f'WIN!!! - {result_check}')
            else:
                print(f' {result_check}  ')
            GAME_END = True

    
    
    
