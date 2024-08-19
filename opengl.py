from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# Global variables for rotation and scaling
angle = 0
scale = 1.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background color (black)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw_triangle():
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_TRIANGLES)
    glVertex2f(-2.0, -2.0)
    glVertex2f(2.0, -2.0)
    glVertex2f(0.0, 2.0)
    glEnd()

def draw_circle():
    glColor3f(0.0, 1.0, 0.0)  # Green color
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = math.radians(i)
        x = 1.5 * math.cos(theta)
        y = 1.5 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

def draw_rectangle():
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glBegin(GL_QUADS)
    glVertex2f(-3.0, 1.0)
    glVertex2f(3.0, 1.0)
    glVertex2f(3.0, -1.0)
    glVertex2f(-3.0, -1.0)
    glEnd()

def display():
    global angle, scale
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw and manipulate the triangle
    glPushMatrix()
    glTranslatef(-5.0, 5.0, 0.0)  # Position
    glScalef(scale, scale, 1.0)   # Scale
    glRotatef(angle, 0.0, 0.0, 1.0)  # Rotate
    draw_triangle()
    glPopMatrix()
    
    # Draw and manipulate the circle
    glPushMatrix()
    glTranslatef(5.0, 5.0, 0.0)   # Position
    glScalef(scale, scale, 1.0)   # Scale
    glRotatef(angle, 0.0, 0.0, 1.0)  # Rotate
    draw_circle()
    glPopMatrix()

    # Draw and manipulate the rectangle
    glPushMatrix()
    glTranslatef(0.0, -5.0, 0.0)  # Position
    glScalef(scale, scale, 1.0)   # Scale
    glRotatef(angle, 0.0, 0.0, 1.0)  # Rotate
    draw_rectangle()
    glPopMatrix()
    
    glutSwapBuffers()

def timer(value):
    global angle, scale
    angle += 2.0
    if angle > 360:
        angle -= 360
    
    scale = 1.0 + 0.1 * math.sin(math.radians(angle))
    
    glutPostRedisplay()
    glutTimerFunc(30, timer, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("OpenGL Shapes")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
