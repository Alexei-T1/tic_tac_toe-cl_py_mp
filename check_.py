


GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'

def check_field(field):
    return field

def check_step(step, field):   
    try:
        x, y = step.split(',')
        x, y = int(x), int(y)
    except:
        return WRONG_INPUT
    return USED_FIELD if field[y][x] == GAMER_F or field[y][x] == GAMER_S else (x,y)


  

