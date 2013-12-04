import datetime, math

earthRadius = 6378.388  # Raggio equatoriale
sunRadius = 696000

# Angoli sessadecimali
def sin(a):
	a = (a * math.pi) / 180
	return(math.sin(a))
	
def cos(a):
	a = (a * math.pi) / 180
	return(math.cos(a))

def tan(a):
	a = (a * math.pi) / 180
	return(math.tan(a))	
	
def asin(v):
	result = math.asin(v)
	result = (result * 180) / math.pi
	
	return(result)

def acos(v):
	result = math.acos(v)
	result = (result * 180) / math.pi
	
	return(result)



def atan(v):
	result = math.atan(v)
	result = (result * 180) / math.pi
	
	return(result)


def toJulianDate(day, month, year, hours=12, minutes=0, seconds=0):
	a = (14 - month) / 12
	y = year + 4800 - a
	m = month + 12*a -3
	
	result = day + (153*m +2) / 5 + 365*y + y/4 - y/100 + y/400 - 32045
		
	if hours > 12:
		fraction =  (((hours - 12) * 3600) + minutes*60) / (24.0 * 3600)
	else:
		fraction = -((12 * 3600) - (3600 * hours) - (minutes*60)) / (24.0 * 3600)
	
	return (result+fraction)

def getGST(day, month, year, hours, minutes, seconds):
	JD = toJulianDate(day, month, year, hours, minutes, seconds)
	T = (JD - 2451545.0) / 36525.0
	
	theta0 = 280.46061837 + 360.98564736629 * (JD - 2451545.0) + 0.000387933*T*T - T*T*T/38710000.0
	
	return theta0

	
	
def normalize(v):
	if v < 0:
		while v < 0:
			v = v + 360.0
	else:
		while v >= 360:
			v = v - 360.0
	return v
	
def getEclipticCoordinates(day, month, year, hours=12, minutes=0, seconds=0):
	# Julian Date
	JD = toJulianDate(day, month, year, hours, minutes, seconds)
	
	# Numero di giorni trascorsi dal 1 Gennaio 2000 ore 12.00, o numero di giorni
	# che devono trascorrere per arrivare al 1 Gennaio 2000 ore 12.00
	n = JD - 2451545.0
	
	# Longitudine media del sole, corretta dall'abberrazione della luce
	L = normalize(280.460 + 0.9856474*n) # Gradi
	
	# Anomalia media del sole
	g = normalize(357.528 + 0.9856003*n) # Gradi
	
	# Longitudine ecliptica
	lambd = L + 1.915*sin(g) + 0.020*sin(2*g)
	
	# Latitudine ecliptica del sole
	beta = 0
	
	# Distanza del sole dalla terra
	R = 1.00014 - 0.01671*cos(g) - 0.00014*cos(2*g)
	
	return (lambd, beta, R, n)
	
def getQuadrant(v):
	v = normalize(v)
	
	if v < 180:
		if v < 90:
			return 1
		else:
			return 2

	else:
		if v < 270:
			return 3
		else:
			return 4
			
def getPolarEquatorialCoordinates(day, month, year, hours=12, minutes=0, seconds=0):
	eclipticCoordinates = getEclipticCoordinates(day, month, year, hours, minutes, seconds)
			
	lambd = eclipticCoordinates[0]
	beta = eclipticCoordinates[1]
	R = eclipticCoordinates[2]
	n = eclipticCoordinates[3]
	
	epsilon = 23.439 - 0.0000004*n # Gradi
	
	# Ascensione destra
	alpha = atan(cos(epsilon) * tan(lambd))
	
	if getQuadrant(lambd) != getQuadrant(alpha):
		alpha = 180 + alpha
	
	# Declinazione
	sigma = asin(sin(epsilon) * sin(lambd))
			
	return (alpha, sigma, R, n)
	
def getHorizontalCoordinate(latitude, longitude, day, month, year, hours, minutes, seconds):
	pc = getPolarEquatorialCoordinates(day, month, year, hours, minutes, seconds)
	
	alpha = pc[0]
	sigma = pc[1]
	
	GST = getGST(day, month, year, hours, minutes, seconds)
	
	# Angolo Orario
	h = GST - longitude - alpha
	
	# Valutare se a o 180 - a (Alzo)
	a = asin(sin(latitude)*sin(sigma) + cos(latitude)*cos(sigma)*cos(h))
	
	# Valutare se A o 180 gradi + A (Azimuth)
	A = atan(sin(h) / (cos(h)*sin(latitude) - tan(sigma)*cos(latitude)))
	
	
	
	return (a, A)



def getRectangularEquatorialCoordiantes(day, month, year, hours=12, minutes=0, seconds=0):
	
	equatorialCoordinates = getPolarEquatorialCoordinates(day, month, year, hours, minutes, secons)
	
	alpha = equatorialCoordinates[0]
	sigma = equatorialCoordinates[1]
	R = equatorialCoordinates[2]
	n = equatorialCoordinates[3]
	
	epsilon = 23.439 - 0.0000004*n # Gradi
		
	X = R * math.cos(lambd)
	
	Y = R * math.cos(epsilon) * math.sin(lambd)
	Z = R * math.sin(epsilon) * math.sin(lambd)

	return (X, Y, Z)

# http://en.wikipedia.org/wiki/Position_of_the_Sun
# GST: http://www.geoastro.de/elevaz/basics/meeus.htm
# 44 50 59.53"N -> 44.849869 latitude
# 10 22 5.99"E -> 10.368330 longitude
for ore in range(7, 17):
	for minuti in range(0, 60):
		print ore, " ", minuti, " ", getHorizontalCoordinate(44.849869, 10.368330, 04, 12, 2013, ore, minuti, 00)