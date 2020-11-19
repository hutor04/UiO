# Create a program in file oppgave_5.py
# The program must ask the user to provide coordinates and dimensions for two geometric shapes (oval and rectangle).
# The program must verify if the format of the input is correct and if the shapes will fully fit in the canvas.
# Default canvas dimensions are 200x200.
# The information about the shapes must be stored in a dictionary.
# The program then uses the provided data to draw the geometric shapes.

# Importing the required modules
import re
import ezgraphics

# We will use this pattern to make sure that user provides data in the right format
PATTERN = re.compile('\d+,\d+,\d+,\d+')

# Constant that sets window size
WINDOW_SIZE = [200, 200]

# We initiate the dictionary, where we will store data about the shapes.
available_shapes = {'circle': [], 'rectangle': []}


# The function checks if the input format is correct. It matches the input against the pattern. If pattern is found,
# the function return True
def verify_input(string, pattern):
    if pattern.match(string) is not None:
        return True
    else:
        return False


# The function checks if the provided coordinates and dimensions allow to fit the shape to the window. It sums
# x-coordinate with x-dimension and y-coordinate with y-dimension and compares them with the dimensions of the
# graphic window. It doesn't check for zero coordinates or dimensions.
def verify_prepare_coordinates(string):
    coordinates_size = [int(x) for x in string.split(',')]
    check_x = coordinates_size[0] + coordinates_size[2]
    check_y = coordinates_size[1] + coordinates_size[3]
    if (check_x < WINDOW_SIZE[0]) and (check_y < WINDOW_SIZE[1]):
        return coordinates_size
    else:
        return False


# The input routine. We ask the user for data and use the functions above to verify it.
def input_routine(shapes):
    print('Lets draw some geometric shapes.')
    for key in shapes:
        happy = False
        while not happy:
            data = input('\nWe are going to draw a {}, input its coordinates and size, '
                         'comma separated: '.format(key.upper()))
            if (verify_input(data, PATTERN) and verify_prepare_coordinates(data)) is not False:
                happy = True
                data = verify_prepare_coordinates(data)
            else:
                print('\nWrong input format or coordinates/size are out of range! Try 100,100,50,50 ')
        shapes[key] = data
    print('\nGood job! The shapes are getting cooked......')


# The function that creates the graphic window, reads the data about shapes and draws them.
def draw_shapes(shapes):
    window = ezgraphics.GraphicsWindow(WINDOW_SIZE[0], WINDOW_SIZE[1])
    canvas = window.canvas()
    for key in shapes:
        if key == 'circle':
            canvas.drawOval(shapes[key][0], shapes[key][1], shapes[key][2], shapes[key][3])
        elif key == 'rectangle':
            canvas.drawRectangle(shapes[key][0], shapes[key][1], shapes[key][2], shapes[key][3])
    window.wait()


# Main routine of the program
def main():
    input_routine(available_shapes)
    draw_shapes(available_shapes)


if __name__ == '__main__':
    main()
