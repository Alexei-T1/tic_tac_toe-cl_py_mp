

def draw_field(field):
    sN = 1
    print("y/x 1 2 3")
    for s in field:
        print(f"{sN}  |", end="")
        sN +=1
        for i in s:
            i = i if i != None else '.'
            print(f"{i}|", end="")
        print()
    print()
      