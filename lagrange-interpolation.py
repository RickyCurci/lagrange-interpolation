import matplotlib.pyplot as pl
import numpy as nm



x = [1,2,3]; y = [4,5,6]; lx = []; 

def lagrange(x,y, xp): 
	l = 1; L = 0

	for i in range(0,len(x)): 
		for j in range(0,len(x)): 
			if i != j: 

				l *= (xp - x[j])/(x[i] - x[j])
				
		lx.append(l); l = 1

	for v in lx: 
		
		L += v*y[lx.index(v)];

	print(xp,int(L))

	x1 = x; x1.append(xp)
	x2 = y; x2.append(L)

	pl.show(pl.plot(x1,x2))

lagrange(x,y, 19)	
