


GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'

def check_field(field):
    
    
    for i in range(3):
        if field[i].count(GAMER_F) == 3:
            return GAMER_F
        if field[i].count(GAMER_S) == 3:
            return GAMER_S
        
    for s in range(3):
        if field[0][s] == field[1][s]  == field[2][s] == GAMER_F:
            return GAMER_F
        if field[0][s] == field[1][s]  == field[2][s] == GAMER_S:
            return GAMER_S
            
    if field[0][0] == field[1][1] == field[2][2] == GAMER_F:
        return GAMER_F
    if field[0][0] == field[1][1] == field[2][2] == GAMER_S:
        return GAMER_S
    
    if field[0][2] == field[1][1] == field[2][0] == GAMER_S:
        return GAMER_S
    if field[0][2] == field[1][1] == field[2][0] == GAMER_F:
        return GAMER_F
    
    steps = [i for st in field for i in st].count(GAMER_F) + [i for st in field for i in st].count(GAMER_S)
    if steps == 9:
        return "ничья"
    
    return False

def check_step(step, field):   
    try:
        x, y = step.split(',')
        x, y = int(x), int(y)
        if x < 1 or x > 3 or y < 1 or y > 3:
            return WRONG_INPUT
    except:
        return WRONG_INPUT
    return USED_FIELD if field[y-1][x-1] == GAMER_F or field[y-1][x-1] == GAMER_S else (x,y)


  

