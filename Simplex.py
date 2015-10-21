
from __future__ import division
import time
from PrintTable import PrintTable

table = PrintTable()

def pivot(N,B,A,b,c,v,l,e):
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
	z = c
	table.makeTable(N,B,A,b,c,v,z)
	while findFlag(c):
		delta = dict()
		e = maxDict(c) #Optimality Condition
		for i in B:
			try:
				if A[i][e] > 0:
					delta[i] = b[i]/A[i][e]
				else: delta[i] = float('inf')
			except Exception as e:
				pass
		l = minDict(delta) #Feasibility Condition
		try:
			if delta[l] == float('inf'):
				return 'Unbounded'
			else:

				(N,B,A,b,c,v) = pivot(N,B,A,b,c,v,l,e)
				table.makeTable(N,B,A,b,c,v,z)
		except Exception as e:
			pass

def PivotingTrial(N,B,A,b,c,v,l,e):
	(N,B,A,b,c,v) = pivot(N,B,A,b,c,v,l,e)
	(N,B,A,b,c,v) = pivot(N,B,A,b,c,v,5,3)
	for e in pivot(N,B,A,b,c,v,3,2):
		print e

if __name__ == '__main__':
	print 'Input the number of Variables'
	n = input()
	print 'Input the number of Equations'
	m = input()
	N = [i for i in range(1,n+1)]
	B = [n+j for j in range(1,m+1)]
	v =  0
	A = dict()
	b = dict()
	c = dict()
	print 'Enter the coefficient Matrix'
	for i in B:
		A[i] = dict()
		for j in N:
			A[i][j] = input()
	print 'Enter the B matrix'
	for i in B:
		b[i] = input()
	print 'Enter the coefficients of the objective function in the order of entry of the variables'
	for i in N:
		c[i] = input()
	Simplex(N,B,A,b,c,v)
	#PivotingTrial(N,B,A,b,c,v,l,e)



