from check_ import check_field
from draw_field import draw_field
from input import input_o, input_step

GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'


def output_result(result_check):
    if result_check == GAMER_F or result_check == GAMER_S:
            print(f'WIN!!! - {result_check}')
    else:
        print(f' {result_check}  ')


def game():
    GAME_END = False
    field = [[None, None, None] for i in range(3)]
    draw_field(field) 

    choice_ox = None
    while True:
            choice_ox = input("choice game for X or O: ")
            if choice_ox == GAMER_F or choice_ox == GAMER_S:
                break

    while not GAME_END:
        if choice_ox == GAMER_F:
            x_step = input_step(field, GAMER_F)
            x, y = x_step
            field[y-1][x-1] = GAMER_F

            result_check = check_field(field)
            if result_check:
                output_result(result_check)
                break

            if ([i for st in field for i in st].count(GAMER_F) + [i for st in field for i in st].count(GAMER_S)) != 9:           
                o_step = input_o(field)
                x, y = o_step
                field[y][x] = GAMER_S
        else:
            o_step = input_o(field)
            x, y = o_step
            field[y][x] = GAMER_F

            result_check = check_field(field)
            draw_field(field)
            if result_check:
                output_result(result_check)
                break

            if ([i for st in field for i in st].count(GAMER_F) + [i for st in field for i in st].count(GAMER_S)) != 9: 
                x_step = input_step(field, GAMER_S)
                x, y = x_step
                field[y-1][x-1] = GAMER_S
            
        result_check = check_field(field)
        draw_field(field)
        
        if result_check:
            output_result(result_check)
            break

    
    
    
