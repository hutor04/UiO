from spillebrett import Spillebrett
import os
import sys

TITLE = 'The Game of Life'


# The function calculates max rows and columns based on the size of the terminal
def max_size():
    rows, cols = os.popen('stty size', 'r').read().split()
    # -3 stands for the rows with messages that are supposed to appear on screen
    rows = int(rows) - 3
    cols = int(cols)
    return rows, cols


# The function asks user to input rows and columns. It takes as parameters recommended dimensions
# of the game field.
def ask_input(r_rows, r_cols):
    happy = False
    while not happy:
        rows = input('Enter the number of rows ({} is recommended): '.format(r_rows))
        cols = input('Enter the number of columns ({} is recommended): '.format(r_cols))
        if rows.isdigit() and cols.isdigit():
            rows = int(rows)
            cols = int(cols)
            if rows > 0 and cols > 0:
                happy = True
        else:
            print('Looks like we got the wrong input...')
    return rows, cols


# The main routine of the program
def main():
    # Default rows and columns
    r_rows, r_cols = 50, 50
    print('We are going to play the game of life...')
    # This checks if the program runs in terminal
    if sys.stdout.isatty():
        # If it runs in terminal we determine the recommended rows, columns
        r_rows, r_cols = max_size()
    # We ask for user input
    rows, cols = ask_input(r_rows, r_cols)
    # We initiate the game field
    game = Spillebrett(rows, cols)
    # We are going to enter the loop
    happy = False
    while not happy:
        print('{:^{width}}'.format(TITLE, width=r_cols))
        game.tegnBrett()
        print('Generation: {}, Living cells: {}.'.format(game.generation(), game.finnAntallLevende()))
        choice = input('Press "enter" to breed new generation or "q" to exit: ')
        # If we get empty line as input, we update the game field
        if choice == '':
            game.oppdatering()
        # If we get 'q', we exit the game
        elif choice.lower() == 'q':
            print('See you later!')
            happy = True
        # We just ignore the wrong input
        else:
            pass


# starte hovedprogrammet
if __name__ == '__main__':
    main()
