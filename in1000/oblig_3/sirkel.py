# The program draws a red circle.

# We import the ezgraphics module
import ezgraphics

# We create a new parent window with the dimensions 202 by 202
window = ezgraphics.GraphicsWindow(202, 202)

# We create a graphic canvas in the window
canvas = window.canvas()

# We set the outline of the objects to red color
canvas.setOutline('red')

# We set the fill color to be red
canvas.setFill('red')

# We draw a circle
canvas.drawOval(2, 2, 198, 198)
# We wait for the user to close the window
window.wait()
