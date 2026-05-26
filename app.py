from check_ import check_field
from draw_field import draw_field
from input import input_o, input_step

GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'
GAME_END = False

field = [[None, None, None] for i in range(3)]
draw_field(field) 

while not GAME_END:
    x_step = input_step(field, GAMER_F)

    x, y = x_step
    field[y-1][x-1] = GAMER_F

    step_o = input_o(field)

    check_field(field)   
    draw_field(field)

    print(step_o) 
    
    
    GAME_END = True
