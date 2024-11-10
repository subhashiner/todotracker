import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Interactive Drawing Program")
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)

# Set initial pen properties
pen_color = "black"
pen_width = 3
pen.pensize(pen_width)

# Functions for movement
def move_forward():
    pen.forward(10)

def move_backward():
    pen.backward(10)

def turn_left():
    pen.left(15)

def turn_right():
    pen.right(15)

# Functions for changing pen color
def change_color_red():
    global pen_color
    pen_color = "red"
    pen.color(pen_color)

def change_color_blue():
    global pen_color
    pen_color = "blue"
    pen.color(pen_color)

def change_color_green():
    global pen_color
    pen_color = "green"
    pen.color(pen_color)

def change_color_black():
    global pen_color
    pen_color = "black"
    pen.color(pen_color)

# Functions for changing pen size
def increase_pen_size():
    global pen_width
    pen_width += 1
    pen.pensize(pen_width)

def decrease_pen_size():
    global pen_width
    pen_width = max(1, pen_width - 1)  # Minimum width of 1
    pen.pensize(pen_width)

# Function to clear the screen
def clear_screen():
    pen.clear()

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(change_color_red, "r")
screen.onkey(change_color_blue, "b")
screen.onkey(change_color_green, "g")
screen.onkey(change_color_black, "k")
screen.onkey(increase_pen_size, "plus")
screen.onkey(decrease_pen_size, "minus")
screen.onkey(clear_screen, "c")

# Instructions
print("Use arrow keys to move the turtle:")
print("Up - Forward, Down - Backward, Left - Turn Left, Right - Turn Right")
print("Press 'r' for Red, 'b' for Blue, 'g' for Green, 'k' for Black pen colors")
print("Press '+' to increase pen size, '-' to decrease pen size")
print("Press 'c' to clear the screen")

# Start the program
turtle.done()
