
from __future__ import division
import time

def pivot(N,B,A,b,c,v,l,e):
	print '________________________'
	print 'From Pivot'
	print 'A :', A
	print 'N :', N
	print 'B :', B
	print 'b :', b
	print 'c :', c
	print 'v :', v
	print 'l :', l
	print 'e :', e
	Anew = dict()
	bnew = dict()
	cnew = dict()
	bnew[e] = b[l]/A[l][e]
	N.remove(e)
	


	Anew[e] = dict()
	for j in N:
		Anew[e][j] = A[l][j]/A[l][e]
	Anew[e][l] = 1/A[l][e]
	

	#Compute the coefficients of the remaining constraints
	B.remove(l)
	for i in B:
		bnew[i] = b[i] - A[i][e] * bnew[e]
		Anew[i] = dict()
		for j in N:
			Anew[i][j] = A[i][j] - A[i][e]*Anew[e][j]
		Anew[i][l] = -A[i][e] * Anew[e][l]
	


	#Compute the objective function
	vdash = v + c[e]*bnew[e]
	for j in N:
		cnew[j] = c[j] - c[e]*Anew[e][j]
	cnew[l] = -c[e]*Anew[e][l]
	


	#Compute the new sets of basic and nonbasic variables
	N.append(l)
	B.append(e)
	print '________________________'
	return (N, B, Anew, bnew, cnew, vdash)


def findFlag(c):
	j = 0
	for i in c.values():
		if i < 0 : j += 1
	if j == len(c) : return False
	else:
		return True
def minDict(d):
	min = float('inf')
	index = 0
	for i,e in d.iteritems():
		if e < min: 
			min = e
			print 'min :' ,min
			index = i
	return index
def maxDict(d):
	max = -float('inf')
	index = 0
	for i,e in d.iteritems():
		if e > max:
			max = e
			index = i
	return index
def Simplex(N,B,A,b,c,v):
	v1 = v
	while findFlag(c):
		print '		___________'
		print 'From Simplex'
		delta = dict()
		print 'c :', c
		e = maxDict(c)
		print 'e : ' , e
		for i in B:
			#print 'i: ' ,i
			if A[i][e] > 0:
				delta[i] = b[i]/A[i][e]
			else: delta[i] = float('inf')
		print 'delta: ',delta
		l = minDict(delta)
		print'		___________'
		if delta[l] == float('inf'):
			return 'Unbounded'
		else:
			(N,B,A,b,c,v) = pivot(N,B,A,b,c,v,l,e)

	for e in (N,B,A,b,c,v):
		print e

def PivotingTrial(N,B,A,b,c,v,l,e):
	(N,B,A,b,c,v) = pivot(N,B,A,b,c,v,l,e)
	(N,B,A,b,c,v) = pivot(N,B,A,b,c,v,5,3)
	for e in pivot(N,B,A,b,c,v,3,2):
		print e

if __name__ == '__main__':
	N = [1,2,3]
	B = [4,5,6]
	v=  0
	l = 6
	e = 1
	A = {4: {1: 1, 2: 1, 3: 3}, 5: {1: 2, 2: 2, 3: 5}, 6: {1: 4, 2: 1, 3: 2}}
	b = {4:30,5:24,6:36}
	c = {1:3,2:1,3:2}
	t0 = time.clock()
	Simplex(N,B,A,b,c,v)
	#PivotingTrial(N,B,A,b,c,v,l,e)
	print time.clock() - t0



