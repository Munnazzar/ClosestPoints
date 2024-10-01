import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
import time
def bruteforce3D(points):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glBegin(GL_LINES)
    
    p1Closest = {}
    p2Closest = {}
    distClosest = sys.maxsize
    for i in points:
        for j in points:
            if i==j:
                break
            glBeing(GL_LINES)
            glColor3f(1.0, 1.0, 0) #yellow
            glVertex3f(i[0],i[1],i[2])
            glVertex3f(j[0],j[1],j[2])
            glEnd()
            glFlush()
            time.sleep(0.005)
            tempClosest = math.sqrt( abs((j[0]-i[0])**2 +  (j[1]-i[1])**2 + (j[2]-i[2])**2 ))
            if(tempClosest<distClosest):
                distClosest=tempClosest
                p1Closest=i
                p2Closest=j
    glEnd()
    glPopMatrix()
    
    return [p1Closest,p2Closest]         