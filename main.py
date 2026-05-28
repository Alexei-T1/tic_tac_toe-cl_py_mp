
import app


if __name__ == "__main__":

    repeat = True

    while repeat:
        app.game()
        repeat = input('another game? input: Y/N  ')

        while repeat != 'N' != 'n' != 'Y' != 'y':
            if repeat == 'N' or repeat == 'n':
                repeat = False
                break
            if repeat == 'Y' or repeat == 'y':
               repeat = True
               break
            repeat = input('another game? input: Y/N  ') 