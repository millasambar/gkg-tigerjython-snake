################################
#                              #
# SNAKE.PY                     #
#                              #
# Author:  Milla Sambar        #
# Date:    17.11.2020          #
#                              #
################################

###########
# IMPORTS #
###########


from gturtle import *


#####################
# GLOBAL PROPERTIES #
#####################


# Key codes
KEY_CODE_LEFT = 37
KEY_CODE_RIGHT = 39
KEY_CODE_UP = 38
KEY_CODE_DOWN = 40
KEY_CODE_ENTER = 10

# Constant settings
frameSize = 500

# General properties
points = 0
highScore = 0
lastKey = None
name = ""

# Turtle properties
frame = TurtleFrame()
snakeTurtle = None
frameTurtle = Turtle(frame)
frameTurtle.setPos(-250,-250)
appleTurtle = None
stoneTurtles = []

name = input("Enter your username")
#############
# FUNCTIONS #
#############



# FUNCTIONS TO DRAW SHAPES WITH TURTLES
def turtleFrame():
    frameTurtle.hideTurtle()

    repeat 4:
        frameTurtle.fd(frameSize)
        frameTurtle.rt(90)
#to make the turtle frame        

def onKeyPressed(event):
    global lastKey
    key = event.getKeyCode()
    print key
    
    lastKey = key 
#test with if else
    
def turnSnakeTurtle(TurtleFrame):
    key = lastKey
    snakeTurtle.penUp()
    if   key == 37:   #left
        snakeTurtle.setHeading(-90)
    elif key == 39: #right
        snakeTurtle.setHeading(90)
    elif key == 38: #up
        snakeTurtle.setHeading(0)
    elif key == 40: #down
        snakeTurtle.setHeading(180)
#that the snakehead can turn around        
def AppleTurtle(frame):
    ax = snakeTurtle.getX()
    ay = snakeTurtle.getY()
    bx = appleTurtle.getX()
    by = appleTurtle.getY()
    if ax > bx-10 and ay > by-10 and ax < bx+10 and ay < by+10:
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)
        playTone(1000)
#That the apple always appears random someone in the frame if the SnakeTurtle has the same coordinates like him + makes a noise
def StoneTurtles(frame):
     t = Turtle(frame, "stone.png")
     stoneTurtles.append(t)
     t.setRandomPos(0.9*frameSize, 0.9*frameSize)
 #that stones appear   

def snakeTurtleIsAlive():

    x = snakeTurtle.getX()
    y = snakeTurtle.getY()
    print (x, y)
    if (x > 230 or y < -230 or x < -230 or y > 230):
        return False
    
    for t in stoneTurtles:
        ax = snakeTurtle.getX()
        ay = snakeTurtle.getY()
        bx = t.getX()
        by = t.getY()
    
        if (ax > bx-10 and ay > by-10 and ax < bx+10 and ay < by+10): 
         return False
        
    else:
        return True
#that it checks if the turtle is still "alive" (on the right coordinates) and if not goes to "false"
    
    
def waitForInputName():
    global name 
    
    

    print "Name entered: " + name 
    

def play(frame):
    global points 
    global snakeTurtle
    global appleTurtle
    global stoneTurtles


    print "Play function started" 
    snakeTurtle = Turtle(frame, "snake.png", keyPressed = onKeyPressed)
    appleTurtle = Turtle(frame, "apple.png")

    
    i = 0
    isAlive = True
    while (isAlive): 
        print "Snake is alive"
        
        turnSnakeTurtle(TurtleFrame)
        

        snakeTurtle.fd(10)
        
        AppleTurtle(frame)
        
        
        isAlive = snakeTurtleIsAlive()

        i = i + 1
        if (i%100 == 1):
            StoneTurtles(frame)
    playTone(500)      

def main():
    
    print "Main function started"
    turtleFrame()
    waitForInputName();

    # Start the actual game
    play(frame)
    



main()


