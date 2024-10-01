import pygame
from pygame.locals import *
from OpenGL.GL import *
import math
import time
from OpenGL.GLU import *
import csv
import closest
import sys


def collect_points():
    points = []
    with open('1000_points.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            x=float(lines[0])
            y=float(lines[1])
            z=float(lines[2])
            points.append((x,y,z))
    return points

# Function to draw the points in 3D space
def draw_points(points):
    if len(points)==2:
        glBegin(GL_POINTS)
        glColor3f(1.0, 1.0, 1.0)
        for point in points:
            glVertex3fv(point)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(1.0, 0.75, 0.8)
        glVertex3fv(points[1])
        glVertex3fv(points[0])
        glEnd()
        return
    
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  # Set point color to white
    for point in points:
        glVertex3fv(point)
    glEnd()


# Function to draw 3D axes lines
def draw_axes():
    glBegin(GL_LINES)

    # X-axis (Red)
    glColor3f(2.0, 0.0, 0.0)  # Red for X-axis
    glVertex3f(-4.0, 0.0, 0.0)
    glVertex3f(4.0, 0.0, 0.0)

    # Y-axis (Green)
    glColor3f(0.0, 2.0, 0.0)  # Green for Y-axis
    glVertex3f(0.0, -4.0, 0.0)
    glVertex3f(0.0, 4.0, 0.0)

    # Z-axis (Blue)
    glColor3f(0.0, 0.0, 2.0)  # Blue for Z-axis
    glVertex3f(0.0, 0.0, -4.0)
    glVertex3f(0.0, 0.0, 4.0)

    glEnd()

# Function to initialize OpenGL settings
def init_gl():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background color
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D
    glPointSize(5)  # Set size of points


def display(points):
    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Set up camera
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    camera_z = -5  # Initial zoom position on the Z-axis
    glTranslatef(0.0, 0.0, camera_z)  # Move camera back to see the object

    init_gl()

    # Rotation variables
    rotate_x, rotate_y = 0, 0

    while True:
        flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        keys = pygame.key.get_pressed()

        if keys[K_RETURN]:
            flag = True
        # Rotation controls
        if keys[K_LEFT]:
            rotate_y -= 1
        if keys[K_RIGHT]:
            rotate_y += 1
        if keys[K_UP]:
            rotate_x -= 1
        if keys[K_DOWN]:
            rotate_x += 1

        
        if keys[K_w]:  # Zoom in (move camera closer)
            camera_z += 0.1
        if keys[K_s]:  # Zoom out (move camera further)
            camera_z -= 0.1

        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        # Apply camera zoom by translating on the Z-axis
        glTranslatef(0.0, 0.0, camera_z)
        glRotatef(rotate_x, 1, 0, 0)  # Rotate around X-axis
        glRotatef(rotate_y, 0, 1, 0)  # Rotate around Y-axis

        # Draw the 3D axes
        draw_axes()
        if flag:
            p1Closest = {}
            p2Closest = {}
            distClosest = sys.maxsize
            for i in points:
                for j in points:
                    if i==j:
                        break
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    draw_axes()
                    draw_points(points)
                    glBegin(GL_LINES)
                    glColor3f(1.0, 1.0, 0) #yellow
                    glVertex3f(i[0],i[1],i[2])
                    glVertex3f(j[0],j[1],j[2])
                    glEnd()
                    pygame.display.flip()
                    tempClosest = math.sqrt( abs((j[0]-i[0])**2 +  (j[1]-i[1])**2 + (j[2]-i[2])**2 ))
                    if(tempClosest<distClosest):
                        distClosest=tempClosest
                        p1Closest=i
                        p2Closest=j
                        
            points=[]
            points.append((p1Closest))
            points.append((p2Closest))
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_axes()
                        
        
        draw_points(points)
        
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    points = collect_points()
    if points:
        display(points)
    else:
        print("No points entered.")

