GAMER_F = "X"
GAMER_S = "O"
USED_FIELD = 'used_field'
WRONG_INPUT ='wrong_input'

def input_o(field):
    cords = [i for st in field for i in st].count(GAMER_F)
    return cords

