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

from OpenGL import GL, GLU, GLUT


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

import lib.Vectorial



def gpsToCartesian(nord, est):
	# 180 : math.pi = nord : x
	# 180 : math.pi = est : y
	
	# z / 6371 = sin(x)
	z = 6371 * math.sin((math.pi * nord) / 180.0)
	
	
	# k / 6371 = cos(x)
	k = 6371 * math.cos((math.pi * nord) / 180.0)
	
	# y / k = sin(y)
	y = k * math.sin( (math.pi*est) / 180.0)
	
	
	# x / k = cos(y)
	y = k * math.cos( (math.pi*est) / 180.0)
	
	return (x, y, z)


# Raggio terrestre 6371
class Patch:
	def __init__(self, nord, est):
		pass
	

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


def assi():
	glBegin(GL_LINES)
	
	
	glColor3f(0, 1, 1)
	glVertex3f(0,0,0)
	glVertex3f(1, 0, 0)	
	
	
	glEnd()
	
	glBegin(GL_LINES)
	glColor3f(1, 0, 0)
	glVertex3f(0,0,0)
	glVertex3f(0, 1, 0)
	glEnd()
	
	
	glBegin(GL_LINES)
	glColor3f(0, 0, 1)
	glVertex3f(0,0,0)
	glVertex3f(0, 0, 1)
	glEnd()
	

class GLWidget(QGLWidget):

	def __init__(self, parent):

		# Inizializza Antenato

		QGLWidget.__init__(self, parent)
		self.xyRotation = 0.0
		self.rotationAroundX = 0.0
		self.zoom = 1.0
		
		self.eye = lib.Vectorial.Point3d([0, -20, 20])
		self.target = lib.Vectorial.Point3d([0, -60, 0])	
		
	
	def addXYrotation(self, v):
		self.xyRotation = self.xyRotation + v
		
	def addRotazionAroundX(self, v):
		self.rotationAroundX = self.rotationAroundX  + v 
	
	def addZoom(self, v):
		self.zoom = self.zoom + v/1000.0
	
	def initializeGL(self):

		#GLUT.glutInit([], [])
	

		black = QColor(0,0,0)

		# Imposto colore di cancellazione

		self.qglClearColor(black)

		glViewport(0, 0, self.width(), self.height())
		glPolygonMode( GL_FRONT_AND_BACK, GL_LINE );
		
		
		glMatrixMode(GL_PROJECTION)

		glLoadIdentity()

		
		glFrustum(-self.width()/2, self.width()/2, -self.height()/2, self.height()/2, 20, 800)
		gluLookAt(self.eye.getX(), self.eye.getY(), self.eye.getZ(), self.target.getX(), self.target.getY(), self.target.getZ(), 0, 0, 1)
	
		glRotatef(self.xyRotation, 0, 0, 1)
	
	
	#	glScalef(self.zoom, self.zoom, self.zoom)
		
	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT);
		glColor3f(1.0, 1.0, 0.0)
		
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
		
		glTranslatef(0, -60, 0)
		glScalef(50, 50, 50)
		
		
		
		#ico(0)
		assi()
		
		
		
		"""
		glBegin(GL_TRIANGLES)
		
		glVertex3f(30, 30, 0)
		glVertex3f(40, 30, 0)
		glVertex3f(40, 40, 0)
		
		glEnd()"""
		
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		
		
		glFrustum(-self.width()/2, self.width()/2, -self.height()/2, self.height()/2, 20, 800)
		
		gluLookAt(self.eye.getX(), self.eye.getY(), self.eye.getZ(), self.target.getX(), self.target.getY(), self.target.getZ(), 0, 0, 1)	
		
		glTranslatef(0, -60, 0)
		glRotatef(self.xyRotation, 0, 0, 1)
		glTranslatef(0, 60, 0)
	
	#	glScalef(self.zoom, self.zoom, self.zoom)
		
		
		
		
		glFlush()

	def resizeGL(self, w, h):
		glViewport(0, 0, self.width(), self.height())
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		#glOrtho(0.0, self.width(), 0.0, self.height(), -1.0, 80)
		#glFrustum(-30, 30, -30, 30, 20, 120)
		glFrustum(-self.width()/2, self.width()/2, -self.height()/2, self.height()/2, 20, 800)
		gluLookAt(self.eye.getX(), self.eye.getY(), self.eye.getZ(), self.target.getX(), self.target.getY(), self.target.getZ(), 0, 0, 1)
		
		
		glRotatef(self.xyRotation, 0, 0, 1)
		
		
		
	#	glScalef(self.zoom, self.zoom, self.zoom)
	
	def straightAheadCamera(self, step=1):
		direction = (self.target - self.eye).normalize()
		translation = direction.scalarPerVector(step)
				
		self.target = lib.Vectorial.Point3d((self.target.to3dVector() + translation))
		self.eye = lib.Vectorial.Point3d((self.eye.to3dVector() + translation))
		
		#print self.target
		#print self.eye


class Window(QWidget):

	def __init__(self, parent):

		# Inizializzo antenato
		QWidget.__init__(self, parent)

		# Creo widget che visualizza opengl <---------------------
		self.glWidget = GLWidget(None)

		# Creo un layour orizzontale
		mainLayout = QHBoxLayout()

		# Aggiungo la widget per opengl al layout
		mainLayout.addWidget(self.glWidget)

		# Imposto il layout per questo (self) oggetto
		self.setLayout(mainLayout)

		self.setMinimumWidth(300)

		self.setMinimumHeight(300)
		self.previousX = 0;

	def keyPressEvent(self, e):
		"""
		Key_Left
		Key_PageUp
		Key_Shift		
		
		"""
		
		if e.key() == QtCore.Qt.Key_Left:
			print "Left"
		elif e.key() == QtCore.Qt.Key_Right:
			print "Right"
		elif e.key() == QtCore.Qt.Key_Up:
			self.glWidget.straightAheadCamera(+1)
			self.glWidget.glDraw()
		elif e.key() == QtCore.Qt.Key_Down:
			self.glWidget.straightAheadCamera(-1)
			self.glWidget.glDraw()
	def mousePressEvent(self, e):
		"""
		LeftButton
		MiddleButton
		
		"""
		#print e.x(), " ", e.y()
		e.ignore()
	def mouseMoveEvent(self, e):
		#print e.x(), " ", e.y()
		
		self.glWidget.addXYrotation(e.x() - self.previousX)
		self.glWidget.glDraw()
		
		self.previousX = e.x()
		
		e.ignore()
	def mouseReleaseEvent(self, e):
		#print e.x(), " ", e.y()
		e.ignore()
	def wheelEvent(self, e):
		self.glWidget.addZoom(e.delta())
		self.glWidget.glDraw()
		print e.delta()
		e.ignore()

app = QtGui.QApplication(sys.argv)

window = Window(None)

window.show()

sys.exit(app.exec_())