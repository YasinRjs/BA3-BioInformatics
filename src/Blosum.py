class Blosum:
	def __init__(self,listAA,matrice):
		self._listAA = listAA
		self._matrice = matrice
	def __str__(self):
		return ("==> "+ str(self._listAA))
	def getMatrice(self):
		return self._matrice
	def getListAA(self):
		return self._listAA
	def getIndex(self,AA):
		return self._listAA.index(AA)
	def getValue(self,x1,y2):
		return self._matrice[x1][y2]