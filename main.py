
import app


if __name__ == "__main__":


    while True:
        app.game()
        repeat = input('another game? input: Y/N  ')

        while repeat not in ('N', 'n', 'Y', 'y'):
           repeat = input('another game? input: Y/N  ')

        if repeat in ('N', 'n'):
            break      
