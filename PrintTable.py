from tabulate import tabulate

class PrintTable():
	def __init__(self):
		self.headers = ["Basic","Cb","Xb","x1","x2","x3","x4","x5","x6"]
	def makeTable(self,N,B,A,b,c,v,z):
		table = dict()
		B.sort()
		N.sort()
		table[1] = ['x'+str(i) for i in B]
		table[1].append('Delta-j')
		table[2] = list()
		
		table[3] = [b[i] for i in B]
		for i in range(1,len(B) + len(N) + 1):
			if i not in z.keys():
				z[i] = 0
			if i not in c.keys():
				c[i] = 0
		for i in range(4,len(B) + len(N) + 4):
			table[i] = list()
			for j in B:
				if i-3 in N:
					table[i].append(A[j][i-3])
				else:
					if i-3 == j: table[i].append(1)
					else: table[i].append(0)
			table[i].append(-c[i-3])
		for i in B: table[2].append(z[i])
		print tabulate(table, headers = self.headers, tablefmt = "grid")
		