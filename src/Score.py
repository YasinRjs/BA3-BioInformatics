from Blosum import *

class Score:
	def __init__(self,seq1,seq2,BlosumObj,penalite):			# Va faire l'algo
		self._penalite = penalite
		self._resultat = 0
		self._seq1 = seq1
		self._seq2 = seq2
		self._Blosum = BlosumObj

		self._subMatrice = self.matriceSub()
		self.findAlignement()

	def __str__(self):
		return self._resultat

	def getResultat(self):
		return self._resultat

	def matriceSub(self):
		m,n = len(self._seq1),len(self._seq2)
		matrice = [[0 for i in range(n+1)] for j in range(m+1)]
#============ PENALITE AFINE ==================
		for i in range(m+1):
			matrice[i][0] = i*self._penalite
		for j in range(n+1):
			matrice[0][j] = j*self._penalite

		for i in range(1,m+1):
			for j in range(1,n+1):
				x1 = self._Blosum.getIndex(self._seq1[i-1])
				y2 = self._Blosum.getIndex(self._seq2[j-1])
				value = self._Blosum.getValue(x1,y2)
				blosValue = matrice[i-1][j-1]+value
				up = matrice[i][j-1]+self._penalite
				left = matrice[i-1][j]+self._penalite
				matrice[i][j] = max(up,left,blosValue)

		#print(matrice)
		return matrice

	def findAlignement(self):
		align1 = ""
		align2 = ""
		i = len(self._seq1)
		j = len(self._seq2)

		while (i>0 and j>0):
			score = self._subMatrice[i][j]
			scoreDiag = self._subMatrice[i-1][j-1]
			scoreLeft = self._subMatrice[i][j-1]
			scoreUp = self._subMatrice[i-1][j]

			i1 = self._Blosum.getIndex(self._seq1[i-1])
			i2 = self._Blosum.getIndex(self._seq2[j-1])
			x2 = scoreDiag + self._Blosum.getValue(i1,i2)
			
			if score == x2:
				a1,a2 = self._seq1[i-1],self._seq2[j-1]
				i,j = i-1,j-1
			elif score == scoreUp+self._penalite:
				a1,a2 = self._seq1[i-1],"-"
				i -= 1
			elif score == scoreLeft + self._penalite:
				a1,a2 = "-",self._seq2[j-1]
				j -= 1

			align1 += a1
			align2 += a2

		while i>0:
			a1,a2 = self._seq1[i-1],"-"
			align1 += a1
			align2 += a2
			i-=1
		while j>0:
			a1,a2 = "-",self._seq2[j-1]
			align1 += a1
			align2 += a2
			j -= 1

		align1 = align1[::-1]
		align2 = align2[::-1]
		len1 = len(align1)
		score = 0
		for i in range(len1):
			a1 = align1[i]
			a2 = align2[i]
			if a1 == "-" or a2 == "-":
				score += self._penalite
			else:
				ind1 = self._Blosum.getIndex(a1)
				ind2 = self._Blosum.getIndex(a2)
				score += self._Blosum.getValue(ind1,ind2)
	
		print("===--- Alignement terminé ---===")

		print(align1)
		print(align2)
		print("Score : ",score)
		return align1,align2

#=============================================

			# score = self._subMatrice[i][j]
			# scoreDiag = self._subMatrice[i-1][j-1]
			# scoreUp = self._subMatrice[i][j-1]
			# scoreLeft = self._subMatrice[i-1][j]


			# score = self._subMatrice[i+1][j+1]
			# scoreDiag = self._subMatrice[i][j]
			# scoreUp = self._subMatrice[i+1][j]
			# scoreLeft = self._subMatrice[i][j+1]


			# score = self._subMatrice[j][i]
			# scoreDiag = self._subMatrice[j-1][i-1]
			# scoreUp = self._subMatrice[j][i-1]
			# scoreLeft = self._subMatrice[j-1][i]

			# score = self._subMatrice[i][j]
			# scoreDiag = self._subMatrice[i-1][j-1]
			# scoreUp = self._subMatrice[i-1][j]
			# scoreLeft = self._subMatrice[i][j-1]
"""
			score = self._subMatrice[j][i]
			scoreDiag = self._subMatrice[j-1][i-1]
			scoreUp = self._subMatrice[j-1][i]
			scoreLeft = self._subMatrice[j][i-1]

			score = self._subMatrice[i][j]
			scoreDiag = self._subMatrice[i-1][j-1]
			scoreUp = self._subMatrice[i-1][j]
			scoreLeft = self._subMatrice[i][j-1]


		while (i>0 and j>0):
			score = self._subMatrice[i][j]
			scoreDiag = self._subMatrice[i-1][j-1]
			scoreLeft = self._subMatrice[i][j-1]
			scoreUp = self._subMatrice[i-1][j]

			i1 = self._Blosum.getIndex(self._seq1[i-1])
			i2 = self._Blosum.getIndex(self._seq2[j-1])
			x2 = scoreDiag + self._Blosum.getValue(i1,i2)
			
			if self.isEqual(score,x2):
				alignA = self._seq1[i] + alignA
				alignB = self._seq2[j] + alignB
				i -= 1
				j -= 1
			elif self.isEqual(score,scoreLeft+self._penalite):
				alignA = self._seq1[i] + alignA
				alignB = "-" + alignB
				i -= 1
			else:
				alignA = "-" + alignA
				alignB = self._seq2[j] + alignB
				j -= 1
		while (i>=0):
			alignA = self._seq1[i] + alignA
			alignB = "-" + alignB
			i -= 1
		while (j>=0):
			alignA = "-" + alignA
			alignB = self._seq2[j] + alignB
			j -= 1

"""

