# The program draws circles of varying size
# We import the graphics module
import ezgraphics

# We create window object with size 300 by 300
win = ezgraphics.GraphicsWindow(300, 300)
# We create canvas object
can = win.canvas()

# This is the counter
teller = 0
# This variable sets the position x
x_pos = 10
# This variable sets the diameter of the circle
stoerrelse = 40

# We enter the for loop and will be there until counter reaches 9
while teller < 9:
    # We draw a circle
    can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    # We increment the counter by one
    teller += 1
    # We increment the position by five
    x_pos += 5
    # We increment the diameter by five
    stoerrelse += 5
# We wait until the graphic window is closed
win.wait()
