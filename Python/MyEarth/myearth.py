#!/usr/bin/python

# INSTALLARE PYTHONQT4

# INSTALLARE PYTHON-OPENGL

# INSTALLARE PYTHON-QT4-GL

# INSTALLARE python-tk





import sys

import PyQt4

from PyQt4 import QtGui, QtOpenGL, QtCore

from PyQt4.QtGui import QWidget, QHBoxLayout, QColor

from PyQt4.QtOpenGL import QGLWidget

from OpenGL.GL import *

from OpenGL import GLUT

import math





def sumVector(v1, v2):
	if len(v1) == len(v2):
		result = []
		for i in range(0, len(v1)):
			result.append(v1[i] + v2[i])
			
		return result	
	else:
		return None

def vectorDivScalar(v, s):
	result = []
	for i in range(0, len(v)):
		result.append( v[i] / float(s))
	return result

def vectorPerScalar(v, s):
	result = []
	for i in range(0, len(v)):
		result.appen(v[i] * s)
	return result

def normalize(v):
	length = 0
	
	for i in range(0, len(v)):
		length = length + v[i] * v[i]
	
	length = math.sqrt(length)
	
	result = vectorDivScalar(v, length)
	
	return result


def triangle(p1, p2, p3, resolution):
	if resolution > 0:
		p12 = normalize(sumVector(p1, p2))
		p23 = normalize(sumVector(p2, p3))
		p31 = normalize(sumVector(p3, p1))
		
		triangle(p1, p12, p31, resolution - 1)
		triangle(p12, p2, p23, resolution - 1)
		triangle(p23, p3, p31, resolution - 1)
		triangle(p12, p23, p31, resolution - 1)
	else:
		glBegin(GL_TRIANGLES)
		
		glVertex3f(p1[0], p1[1], p1[2])
		glVertex3f(p2[0], p2[1], p2[2])
		glVertex3f(p3[0], p3[1], p3[2])
		
		glEnd()
		

def ico(resolution):
		triangle([1, 0, 0], [0,1, 0], [0,0,1], resolution)
		triangle([1, 0, 0], [0,1, 0], [0,0,-1], resolution)
		
		triangle([0,1, 0],[-1, 0, 0], [0,0,1], resolution)
		triangle([0,1, 0],[-1, 0, 0], [0,0,-1], resolution)
		
		triangle([-1, 0, 0], [0, -1, 0], [0,0,1], resolution)
		triangle([-1, 0, 0], [0, -1, 0], [0,0,-1], resolution)
		
		triangle([0, -1, 0], [1, 0, 0], [0,0,1], resolution)
		triangle([0, -1, 0], [1, 0, 0], [0,0,-1], resolution)
	




class GLWidget(QGLWidget):

	def __init__(self, parent):

		# Inizializza Antenato

		QGLWidget.__init__(self, parent)


		
	
	def initializeGL(self):

		GLUT.glutInit([], [])
	

		black = QColor(0,0,0)

		# Imposto colore di cancellazione

		self.qglClearColor(black)

		glViewport(0, 0, self.width(), self.height())
		glPolygonMode( GL_FRONT_AND_BACK, GL_LINE );
		glMatrixMode(GL_PROJECTION)

		glLoadIdentity()

		#glOrtho(0.0, self.width(), 0.0, self.height(), -1.0, 80)
		glFrustum(-self.width()/2, self.width()/2, -self.height()/2, self.height()/2, 20, 200)
		#glFrustum(-30, 30, -30, 30, 20, 120)
	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT);
		glColor3f(1.0, 1.0, 0.0)
		
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
		
		glTranslatef(0, 0, -60)
		glScalef(50, 50, 50)
		
		ico(3)
		
		
		
		
		"""
		glBegin(GL_TRIANGLES)
		
		glVertex3f(30, 30, 0)
		glVertex3f(40, 30, 0)
		glVertex3f(40, 40, 0)
		
		glEnd()"""
		
		
		glFlush()

	def resizeGL(self, w, h):
		glViewport(0, 0, self.width(), self.height())
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		#glOrtho(0.0, self.width(), 0.0, self.height(), -1.0, 80)
		#glFrustum(-30, 30, -30, 30, 20, 120)
		glFrustum(-self.width()/2, self.width()/2, -self.height()/2, self.height()/2, 20, 120)
		gluLookAt()


class Window(QWidget):

	def __init__(self, parent):

		# Inizializzo antenato
		QWidget.__init__(self, parent)

		# Creo widget che visualizza opengl <---------------------
		glWidget = GLWidget(None)

		# Creo un layour orizzontale
		mainLayout = QHBoxLayout()

		# Aggiungo la widget per opengl al layout
		mainLayout.addWidget(glWidget)

		# Imposto il layout per questo (self) oggetto
		self.setLayout(mainLayout)

		self.setMinimumWidth(300)

		self.setMinimumHeight(300)

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Q:
			print "Q"




app = QtGui.QApplication(sys.argv)


window = Window(None)



window.show()




sys.exit(app.exec_())