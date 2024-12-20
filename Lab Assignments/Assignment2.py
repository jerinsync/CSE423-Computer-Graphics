import OpenGL.GLUT as glu
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

window_width = 800
window_height = 600
shooter_x = window_width // 2
shooter_radius = 20
projectiles = []
AllListofCircleRain = []
score = 0
missed_circles = 0
missed_fire = 0
game_over = False
paused = False
shooter_color = (random.uniform(0.6, 1.0), random.uniform(0.6, 1.0), random.uniform(0.6, 1.0))
playPauseColor = (1.0, 0.65, 0.0) 
closeColor = (1.0, 0.1, 0.1)
resetColor = (0.0, 1.0, 1.0)  
color = (random.uniform(0.4, 0.9), random.uniform(0.4, 0.9), random.uniform(0.4, 0.9))
special_circles = []

def circledrawingAlgo(x_center, y_center, radius):
    x = 0
    y = radius
    d = 1 - radius
    while x < y:
        plot_circle_points(x_center, y_center, x, y)
        if d < 0:
            d += 2 * x + 1
            x += 1
        else:
            
            d += 2 * (x - y) + 1
            x += 1
            y -= 1

def plot_circle_points(x_center, y_center, x, y):
    glBegin(GL_POINTS)
    glVertex2f(x_center + x, y_center + y)
    glVertex2f(x_center - x, y_center + y)
    glVertex2f(x_center + x, y_center - y)
    glVertex2f(x_center - x, y_center - y)
    glVertex2f(x_center + y, y_center + x)
    glVertex2f(x_center - y, y_center + x)
    glVertex2f(x_center + y, y_center - x)
    glVertex2f(x_center - y, y_center - x)
    glEnd()


def drawPoints(x, y, zone):
    if zone == 0:
        glVertex2f(x, y)
    elif zone == 1:
        glVertex2f(y, x)
    elif zone == 2:
        glVertex2f(-y, x)
    elif zone == 3:
        glVertex2f(-x, y)
    elif zone == 4:
        glVertex2f(-x, -y)
    elif zone == 5:
        glVertex2f(-y, -x)
    elif zone == 6:
        glVertex2f(y, -x)
    elif zone == 7:
        glVertex2f(x, -y)


def midpointLine(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x = x1
    y = y1
    drawPoints(x, y, zone)
    while x < x2:
        if d < 0:
            d = d + dE
            x = x + 1
        else:
            d = d + dNE
            x = x + 1
            y = y + 1
        drawPoints(x, y, zone)

def convertToZoneZero(x1, y1, x2, y2, zone):
    if zone == 0:
        return x1, y1, x2, y2
    elif zone == 1:
        return y1, x1, y2, x2
    elif zone == 2:
        return y1, -x1, y2, -x2
    elif zone == 3:
        return -x1, y1, -x2, y2
    elif zone == 4:
        return -x1, -y1, -x2, -y2
    elif zone == 5:
        return -y1, -x1, -y2, -x2
    elif zone == 6:
        return -y1, x1, -y2, x2
    elif zone == 7:
        return x1, -y1, x2, -y2


def getZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx > 0:
            if dy >= 0:
                return 0
            else:
                return 7
        else:
            if dy >= 0:
                return 3
            else:
                return 4
    else:
        if dx > 0:
            if dy >= 0:
                return 1
            else:
                return 6
        else:
            if dy >= 0:
                return 2
            else:
                return 5
            
def restart_game():
    global projectiles, AllListofCircleRain, special_circles, score, missed_circles, missed_fire, game_over
    projectiles = []
    AllListofCircleRain = []
    special_circles = []  
    score = 0
    missed_circles = 0
    missed_fire = 0
    game_over = False

def linedrawingalgo(x1, y1, x2, y2):
    zone = getZone(x1, y1, x2, y2)

    x1, y1, x2, y2 = convertToZoneZero(x1, y1, x2, y2, zone)
    midpointLine(x1, y1, x2, y2, zone)

def create_special_circle():
    radius = random.randint(15, 25)
    x = random.randint(20, window_width - 20) 
    y = window_height - 20
    body = True #to see radius overfit
    special_circles.append({'x': x, 'y': y, 'radius': radius, 'body': body})

def update_special_circles():
    global special_circles
    for special_circle in special_circles:
        if special_circle['body']:
            special_circle['radius'] += 0.2
            if special_circle['radius'] >= 25:
                special_circle['body'] = False
        else:
            special_circle['radius'] -= 0.2
            if special_circle['radius'] <= 15:
                special_circle['body'] = True

def draw_left_arrow():
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    linedrawingalgo(30, 570, 50, 585) 
    linedrawingalgo(30, 570, 70, 570)  
    linedrawingalgo(30, 570, 50, 555)  
    glEnd()


def draw_pause_icon():
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    linedrawingalgo(390, 560, 390, 590)  
    linedrawingalgo(410, 560, 410, 590) 
    glEnd()

def draw_play_icon():
    glColor3f(1.0, 0.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    linedrawingalgo(370, 560, 400, 575)  
    linedrawingalgo(370, 590, 400, 575) 
    linedrawingalgo(370, 560, 370, 590) 
    glEnd()

def draw_cross():
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    linedrawingalgo(730, 560, 760, 590) 
    linedrawingalgo(730, 590, 760, 560)  
    glEnd()

def draw_rocket(x, y):
    glColor3f(1.0, 0.0, 0.0)  
    glPointSize(3)
    glBegin(GL_POINTS)
    linedrawingalgo(x - 15, y, x + 15, y)  # Bottom
    linedrawingalgo(x + 15, y, x + 15, y + 40)  # Right
    linedrawingalgo(x + 15, y + 40, x - 15, y + 40)  # Top 
    linedrawingalgo(x - 15, y + 40, x - 15, y)  # Left
    glEnd()

    glColor3f(1.0, 1.0, 0.0) 
    glPointSize(3)
    glBegin(GL_POINTS)
    linedrawingalgo(x + 15, y + 40, x - 15, y + 40)   # Base 
    linedrawingalgo(x - 15, y + 40, x, y + 60)  # Left 
    linedrawingalgo(x + 15, y + 40, x, y + 60)  # Right 
    glEnd()

    glColor3f(1.0, 0.5, 0.0)  
    glPointSize(3)
    glBegin(GL_POINTS)
    linedrawingalgo(x - 10, y, x + 10, y)  # Base
    linedrawingalgo(x - 10, y, x, y - 20)  # Left
    linedrawingalgo(x + 10, y, x, y - 20)  # Righ
    glEnd()

def animate():
    global projectiles, AllListofCircleRain, special_circles, score, missed_circles, game_over, shooter_radius, shooter_x
    glClear(GL_COLOR_BUFFER_BIT)

    draw_cross()
    draw_left_arrow()
    draw_pause_icon() if not paused else draw_play_icon()

    if not game_over:
        glColor3f(0.0, 0.0, 1.0)
        draw_rocket(shooter_x, shooter_radius + 10)
        for proj in projectiles:
            circledrawingAlgo(proj[0], proj[1], 5)

        glColor3f(1.0, 0.71, 0.76)
        for circle in AllListofCircleRain:
            circledrawingAlgo(circle[0], circle[1], 15)

        glColor3f(0.529, 0.808, 0.922) 
        for special_circle in special_circles:
            circledrawingAlgo(special_circle['x'], special_circle['y'], special_circle['radius'])


        draw_text(10, window_height - 80, f'Your Score: {score}', 0.0, 1.0, 0.0)
        draw_text(10, window_height - 100, f'Circle missed: {missed_circles}', 0.0, 1.0, 0.0)
        draw_text(10, window_height - 120, f'Misfire: {missed_fire}', 0.0, 1.0, 0.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
        draw_rocket(shooter_x, shooter_radius + 10)
        # circledrawingAlgo(shooter_x, shooter_radius + 10, shooter_radius)
        draw_text((window_width // 2) - 50, window_height // 2, 'Game Over!!', 0.0, 1.0, 0.0)
        draw_text((window_width // 2) - 50, (window_height // 2) - 20, f'Final Score: {score}', 0.0, 1.0, 0.0)

    glutSwapBuffers()

def draw_text(x, y, text, R=1.0, G=1.0, B=1.0):
    glColor3f(R, G, B)
    glRasterPos2f(x, y)
    for i in text:
        glutBitmapCharacter(glu.GLUT_BITMAP_HELVETICA_18, ord(i))

def timer(value):
    global projectiles, AllListofCircleRain, score, missed_circles, game_over, shooter_radius, shooter_x, missed_fire, special_circles

    if not game_over and not paused:
        #shoot
        updatedProj = []
        for (x, y) in projectiles:  # Projectiles' Position
            if y < window_height:
                updatedProj.append((x, y + 20))  # slow fast
        projectiles = updatedProj

        #normal circle
        new_AllListofCircleRain = []
        for circle in AllListofCircleRain:
            if circle[1] - 65 > 0:  # circle[1] = y coordinate of the center, rockets
                circle = (circle[0], circle[1] - 1)  # falling circles speed
                new_AllListofCircleRain.append(circle)
            else:
                missed_circles += 1
        AllListofCircleRain = new_AllListofCircleRain

        #unique
        for special_circle in special_circles[:]: 
            if special_circle['y'] - 65 > 0:  
                special_circle['y'] -= 1  
            else:
                missed_circles += 1  
                special_circles.remove(special_circle) 

        # miss fire
        for proj in projectiles:
            if proj[1] >= window_height:  # proj[1] = y value, center y
                missed_fire += 1
                projectiles.remove(proj)  
            if missed_fire == 3:
                game_over = True
                break

            # circle vs proj (collision check)
            proj_aabb = calc_circleBox(proj[0], proj[1], 5)
            for circle in AllListofCircleRain[:]:
                circle_aabb = calc_circleBox(circle[0], circle[1], 15)
                if check_collision(proj_aabb, circle_aabb):
                    score += 1
                    AllListofCircleRain.remove(circle)
                    projectiles.remove(proj)
                    break

            for special_circle in special_circles[:]:
                special_circle_aabb = calc_circleBox(special_circle['x'], special_circle['y'], special_circle['radius'])
                if check_collision(proj_aabb, special_circle_aabb):
                    score += 5  
                    special_circles.remove(special_circle)
                    projectiles.remove(proj)
                    break

        #rocket vs circle
        for circle in AllListofCircleRain:
            circle_aabb = calc_circleBox(circle[0], circle[1], 15)
            rocket_aabb = calc_circleBox(shooter_x, shooter_radius + 50, shooter_radius)
            if check_collision(rocket_aabb, circle_aabb):
                game_over = True
                break
            if missed_circles == 3:
                game_over = True
                break

        for special_circle in special_circles:
            special_circle_aabb = calc_circleBox(special_circle['x'], special_circle['y'], special_circle['radius'])
            rocket_aabb = calc_circleBox(shooter_x, shooter_radius + 50, shooter_radius)
            if check_collision(rocket_aabb, special_circle_aabb):
                game_over = True
                break
            if missed_circles == 3:
                game_over = True


        # falling Circle timimg
        if random.random() < 0.04:
            AllListofCircleRain.append((random.randint(20, window_width - 20), window_height - 20))
        if random.random() < 0.01:
            create_special_circle()
        update_special_circles()

    glutPostRedisplay()
    glutTimerFunc(25, timer, 0)

def check_collision(box1, box2):
    return (box1['x'] < box2['x'] + box2['width'] and
            box1['x'] + box1['width'] > box2['x'] and
            box1['y'] < box2['y'] + box2['height'] and
            box1['y'] + box1['height'] > box2['y'])

def calc_circleBox(x, y, radius):
    dictionary = {'x': x - radius, 'y': y - radius, 'width': radius + radius, 'height': radius + radius} #top-left
    return dictionary

def mouse_click(button, state, x, y):
    global paused, game_over
    if state == GLUT_DOWN:
        y = 600 - y 
        if 20 <= x <= 70 and 550 <= y <= 600:
            restart_game()
            print("Starting Over")
        elif 375 <= x <= 425 and 550 <= y <= 600:
            paused = not paused
            print("Game Paused" if paused else "Game Resumed")
        elif 720 <= x <= 770 and 550 <= y <= 600:
            game_over = True
            print(f"Your Final Score: {score}")
            print(f"Goodbye")
            glutLeaveMainLoop()

def keyboard(key, x, y):
    global shooter_x, projectiles, misfires, game_over, paused
    if key == b'a' and shooter_x - shooter_radius > 0 and not paused:
        shooter_x -= 20
    elif key == b'd' and shooter_x + shooter_radius < window_width and not paused:
        shooter_x += 20
    elif key == b' ' and not game_over and not paused:
        projectiles.append((shooter_x, shooter_radius + 50)) #upore fire position initialize

# Initialize 
def init_gl():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()#identity matrix, which is the default matrix (no transformation applied).
    gluOrtho2D(0, window_width, 0, window_height)#2D scene and coordinates fit into the window dimensions 
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(window_width, window_height)
glutCreateWindow(b'Shoot The Circles!')
glutDisplayFunc(animate) #callback every time the window needs to be redrawn.
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse_click)
glutTimerFunc(0, timer, 0)# called at regular intervals after 0 milliseconds
init_gl()
glutMainLoop()