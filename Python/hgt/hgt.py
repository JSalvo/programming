from struct import unpack, calcsize
from pylab import *

f = open("N46E010.hgt", "rb")
m = []
for r in range(0, 1201):
	row = f.read(1201*2)
	rm = []
	for c in range(0, 1201):
		(v, ) = unpack(">h", row[ c*calcsize(">h"): c*calcsize(">h") + calcsize(">h")])
		rm.append(v)
	m.append(rm)

# Normalizzo
for i in range(0, 1201):
	for j in range(0, 1201):
		m[i][j] = (m[i][j] + 32767) / 32767.0
		
matshow(m)
show()
