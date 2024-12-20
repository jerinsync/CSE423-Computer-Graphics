#TASK 1

from OpenGL.GL import * 
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500,500
ballx = -250 
bally = 250
ballx2 = -250 
bally2 = 200
speed = 0.10
ball_size = 2
create_new = False
bg_r, bg_g, bg_b = 0.0, 0.0, 0.0 
count = 0  

class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0


def crossProduct(a, b):
    result=point()
    result.x = a.y * b.z - a.z * b.y
    result.y = a.z * b.x - a.x * b.z
    result.z = a.x * b.y - a.y * b.x

    return result

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def draw_points(x, y, x2, y2, s):
    glLineWidth(s) # size change korte, new gl begin code block
    glBegin(GL_LINES) 

    global count
    if count == 0 or count == 1 or count == 2:
        r , g, b = 1.0, 1.0, 1.0
    elif count == 3 or count == 4 or count == 5 :
        r , g, b = 0.5, 0.7, 1.0
        
    glColor3f(r, g, b)

    glVertex2f(x, y) 
    glVertex2f(x2, y2)

    glVertex2f(x, y+100) 
    glVertex2f(x2, y2+100)

    glVertex2f(x, y+200) 
    glVertex2f(x2, y2+200)

    glVertex2f(x, y+300) 
    glVertex2f(x2, y2+300)

    glVertex2f(x, y+400) 
    glVertex2f(x2, y2+400)

    glVertex2f(x, y-100) 
    glVertex2f(x2, y2-100)

    glVertex2f(x, y-200) 
    glVertex2f(x2, y2-200)

    glVertex2f(x, y-300) 
    glVertex2f(x2, y2-300)

    glVertex2f(x, y-400) 
    glVertex2f(x2, y2-400)
    glEnd()
    
def drawAxes():
    global count
    if count == 0 or count == 1 or count == 2:
        r1 , g1, b1 = 1.0, 1.0, 1.0
    elif count == 3 or count == 4 or count == 5:
        r1 , g1, b1 = 0.0, 0.0, 0.0
        
    glColor3f(r1, g1, b1) 
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(-25,-150) 
    glEnd()
    # glColor3f(r, g, b)
    glLineWidth(3) 
    glBegin(GL_LINES) 
    #new line
    glColor3f(r1, g1, b1)
    #draw here
    glVertex2f(-200, -250) 
    glVertex2f(200, -250) 
    glVertex2f(-200, -250) 
    glVertex2f(-200, 0) 
    glVertex2f(-200, 0) 
    glVertex2f(200, 0) 
    glVertex2f(200, 0) 
    glVertex2f(200, -250) 
    # new line assume
    glColor3f(r1, g1, b1)
    # #draw here
    glVertex2f(-200, 0) 
    glVertex2f(0, 100) 
    glVertex2f(0, 100)  
    glVertex2f(200, 0) 

    glVertex2f(-100, -250) 
    glVertex2f(-100, -100) 
    glVertex2f(-100, -100)
    glVertex2f(0, -100) 
    glVertex2f(0, -100)
    glVertex2f(0, -250)


    glVertex2f(50, -50)
    glVertex2f(150, -50)
    glVertex2f(150, -50)
    glVertex2f(150, -150)
    glVertex2f(150, -150)
    glVertex2f(50, -150)
    glVertex2f(50, -150)
    glVertex2f(50, -50)

    glVertex2f(100, -50)
    glVertex2f(100, -150)
    glVertex2f(50, -100)
    glVertex2f(150, -100)


    glEnd()
    # glLineWidth(1)


def drawShapes():
    pass


def keyboardListener(key, x, y):
    pass

def night_to_day():
    global bg_r, bg_g, bg_b, count
    if count == 0:  
        bg_r, bg_g, bg_b = 0.2, 0.2, 0.2 
        count = 1
    elif count == 1:
        bg_r, bg_g, bg_b = 0.5, 0.5, 0.5 
        count = 2
    elif count == 2:  
        bg_r, bg_g, bg_b = 0.7, 0.7, 0.7  
        count = 3
    elif count == 3:
        bg_r, bg_g, bg_b = 0.9, 0.9, 0.9 
        count = 4
    elif count == 4: 
        bg_r, bg_g, bg_b = 1.0, 1.0, 1.0  
        count = 5
    print(f"bg changed: {count}")

# 0 Dark
# 1 Dark Gray
# 2 Light Dark Gray 
# 3 Light Gray 
# 4 Light Light Gray
# 5 White

def day_to_night():
    global bg_r, bg_g, bg_b, count
    if count == 5: 
        bg_r, bg_g, bg_b = 0.9, 0.9, 0.9  
        count = 4
    elif count == 4: 
        bg_r, bg_g, bg_b = 0.7, 0.7, 0.7
        count = 3
    elif count == 3: 
        bg_r, bg_g, bg_b = 0.5, 0.5, 0.5 
        count = 2
    elif count == 2:  
        bg_r, bg_g, bg_b = 0.2, 0.2, 0.2 
        count = 1
    elif count == 1: 
        bg_r, bg_g, bg_b = 0.0, 0.0, 0.0  
        count = 0
    print(f"bg changed: {count}")



def keyboardListener(key, x, y):
    global bg_r, bg_g, bg_b
    if key == b'l':
        night_to_day()
    elif key == b'd': 
        day_to_night()
    glClearColor(bg_r, bg_g, bg_b, 1.0)
    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global speed, ballx2
    # if key == GLUT_KEY_UP:  
    #     speed *= 2
    #     print("Speed Increased")
    # elif key == GLUT_KEY_DOWN:  
    #     speed /= 2
    #     print("Speed Decreased")
    if key == GLUT_KEY_LEFT:  
        ballx2 -= 5
    elif key == GLUT_KEY_RIGHT: 
        ballx2 += 5
    glutPostRedisplay()


def mouseListener(button, state, x, y):	
    pass


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glClearColor(bg_r,bg_g,bg_b,1);	#//color black #alpha 1, window color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    drawAxes()
    global ballx, bally,ballx2, bally2, ball_size
    draw_points(ballx, bally, ballx2, bally2, ball_size)
    draw_points(ballx+50, bally-50, ballx2+50, bally2-50, ball_size)
    draw_points(ballx+100, bally, ballx2+100, bally2, ball_size)
    draw_points(ballx+150, bally-50, ballx2+150, bally2-50, ball_size)
    draw_points(ballx+200, bally, ballx2+200, bally2, ball_size)
    draw_points(ballx+250, bally-50, ballx2+250, bally2-50, ball_size)
    draw_points(ballx+300, bally, ballx2+300, bally2, ball_size)
    draw_points(ballx+350, bally-50, ballx2+350, bally2-50, ball_size)
    draw_points(ballx+400, bally, ballx2+400, bally2, ball_size)
    draw_points(ballx+450, bally-50, ballx2+450, bally2-50, ball_size)
    draw_points(ballx+500, bally, ballx2+500, bally2, ball_size)
    drawShapes()

    glBegin(GL_LINES)

    glEnd()

    if(create_new): #right button e click
        m,n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m,n)
        glEnd()


    glutSwapBuffers()


def animate():
    glutPostRedisplay() 
    global ballx, bally,ballx2, bally2, speed
    bally -= speed
    bally2 -= speed  
    if bally < -250:
        bally = 250 
        bally2 = 200


def init():
    #//clear the screen
    glClearColor(0,0,0,0) 
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) 

wind = glutCreateWindow(b"OpenGL")
init()

glutDisplayFunc(display)	#display callback function, THIS IS OUR SHOWSCREEN FUNCTION
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener) #a-z0-9
glutSpecialFunc(specialKeyListener) #up, down
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL































# TASK 2


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

W_Width, W_Height = 500, 500

balls = [] 
speed = 0.01
ball_size = 5
movement = ['downRight', 'upRight', 'downLeft', 'upLeft']
coloring = [0.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
freeze  = False 
blink_time = 1
last_blink_time = 0  
storeColor = [] 
blinkTransition = False 
startBlinkingTime = 0 

def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b

def draw_points(x, y, s, r, g, b):
    glPointSize(s)
    glBegin(GL_POINTS)
    glColor3f(r, g, b) 
    glVertex2f(x, y)
    glEnd()

def keyboardListener(key, x, y):
    global freeze 
    if key == b' ':
        freeze = not freeze
        print("freeze all the points :", freeze )
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed
    if key == GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key == GLUT_KEY_DOWN:
        speed /= 2
        print("Speed Decreased")
    glutPostRedisplay()


def mouseListener(button, state, x, y):
    global freeze, movement, coloring, balls, blinkTransition, storeColor, startBlinkingTime
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN and freeze == False:
            print(x,y)
            c_X, c_y = convert_coordinate(x, y)
            balls.append([c_X, c_y, random.choice(movement), random.choice(coloring), random.choice(coloring), random.choice(coloring)])

    elif button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN and freeze  == False:
            print(x,y)
            if blinkTransition == False: 
                blinkTransition = True
                startBlinkingTime = time.time()  
                for ball in balls:
                    storeColor.append((ball[3], ball[4], ball[5]))

    glutPostRedisplay()



def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    for ball in balls:
        draw_points(ball[0], ball[1], ball_size, ball[3], ball[4], ball[5])
    glutSwapBuffers()

def animate():
    global speed, balls, blinkTransition, startBlinkingTime, balls, storeColor
    glutPostRedisplay()
    
    if freeze == False: 
        for ball in balls:
            if ball[2] == 'upRight':
                ball[0] += speed
                ball[1] += speed

                if ball[1] >= 250:
                    ball[2] = 'downRight'
                elif ball[0] >= 250:
                    ball[2] = 'downLeft'

            elif ball[2] == 'downLeft':
                ball[0] -= speed
                ball[1] -= speed

                if ball[1] <= -250:
                    ball[2] = 'upLeft'
                elif ball[0] <= -250:
                    ball[2] = 'upRight'

            elif ball[2] == 'downRight':
                ball[0] += speed
                ball[1] -= speed

                if ball[0] >= 250:
                    ball[2] = 'downLeft'
                if ball[1] <= -250:
                    ball[2] = 'upLeft'

            elif ball[2] == 'upLeft':
                ball[0] -= speed
                ball[1] += speed

                if ball[0] <= -250:
                    ball[2] = 'upRight'
                if ball[1] >= 250:
                    ball[2] = 'downRight'

        if blinkTransition == True:
            elapsed_time = time.time() - startBlinkingTime
            if elapsed_time < 0.5:
                for ball in balls:
                    ball[3], ball[4], ball[5] = 0.0, 0.0, 0.0
            elif elapsed_time < 1.0:
                for i, ball in enumerate(balls):
                    ball[3], ball[4], ball[5] = storeColor[i]
            else:
                blinkTransition = False

        glutPostRedisplay()


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance



glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"Disco Balls")

init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
