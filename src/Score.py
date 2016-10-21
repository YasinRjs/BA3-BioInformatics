from Blosum import *

class Score:
	def __init__(self,seq1,seq2,BlosumObj,penalite):			# Va faire l'algo
		self._penalite = penalite
		self._resultat = 0
		self._seq1 = seq1
		self._seq2 = seq2
		self._Blosum = BlosumObj
		self._similarAA = ['ST','TS','SP','PS','SA','AS','SG','GS','TP','PT','TA','AT','TG','GT','PA','AP','PG','GP','AG','GA','ND','DN','NE','EN','NQ','QN','DE','ED','DQ',
'QD','EQ','QE','HR','RH','HK','KH','RK','KR','MI','IM','ML','LM','MV','VM','IL','LI','IV','VI','LV','VL','FY','YF','FW','WF','YW','WY'];

		self._match = 2
		self._mismatch = -1

#============ GLOBAL ALIGN
		self.globalAlignment()
#============ LOCAL ALIGN
		self.localAlignment()

	def __str__(self):
		return self._resultat
	def getResultat(self):
		return self._resultat
	def globalAlignment(self):
		print("================ Début alignement global ================")
		matrice = self.globalMatAfine()
		self.printMatrice(matrice)
		align1,align2,score = self.globalScoreAndAlign(matrice)
		self.printGlobalAlign(matrice,align1,align2,score)
	def localAlignment(self):
		print("================ Début alignement local ================")
		mat,pointer,maxPos = self.localSubMatrice()
		align1, align2 = self.traceback(mat,pointer,maxPos)
		identity,similarity,score = self.result(align1,align2)
		self.printLocalAlign(mat,maxPos,align1,align2,identity,similarity,score)

	def printMatrice(self,mat):
		for row in mat:
			print(*row)
	def printLocalAlign(self,mat,maxPos,align1,align2,identity,similarity,score):
		#self.printMatrice(mat)
		print("--> Position du max : ",maxPos)
		print("===--- Alignement Local Terminé ---===")
		print(align1)
		print(align2)
		print("Identité : ",identity, "%")
		print("Similarité : ",similarity, "%")
		print("Score : ",score)
	def printGlobalAlign(self,mat,align1,align2,score):
		print("===--- Alignement Global Terminé ---===")
		print(align1)
		print(align2)
		print("Score : ",score)


	def globalMatAfine(self):
		m,n = len(self._seq1),len(self._seq2)
		I = 4
		E = 1

		S = [[0 for i in range(n+1)] for j in range(m+1)]
		V = [[0 for i in range(n+1)] for j in range(m+1)]
		W = [[0 for i in range(n+1)] for j in range(m+1)]
		S[0][1] = -I
		V[0][1] = -I
		W[0][1] = -I
		S[1][0] = -I
		V[1][0] = -I
		W[1][0] = -I
		for i in range(2,m+1):
			V[i][0] = V[i-1][0] - E
			W[i][0] = W[i-1][0] - E
			S[i][0] = S[i-1][0] - E 
		for j in range(2,n+1):
			V[0][j] = V[0][j-1] - E
			W[0][j] = W[0][j-1] - E
			S[0][j] = S[0][j-1] - E
		
		for i in range(1,m+1):
			for j in range(1,n+1):
				V[i][j] = max((S[i-1][j]-I),(V[i-1][j]-E))
				W[i][j] = max((S[i][j-1]-I),(W[i][j-1]-E))
				i1 = self._Blosum.getIndex(self._seq1[i-1])
				i2 = self._Blosum.getIndex(self._seq2[j-1])
				S[i][j] = max((S[i-1][j-1]+self._Blosum.getValue(i1,i2)),(V[i][j]),(W[i][j]))
		
		return S


	def globalMatriceSub(self):
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

		return matrice

	def globalScoreAndAlign(self,globalSubMatrice):
		align1 = ""
		align2 = ""
		i = len(self._seq1)
		j = len(self._seq2)

		while (i>0 and j>0):
			score = globalSubMatrice[i][j]
			scoreDiag = globalSubMatrice[i-1][j-1]
			scoreLeft = globalSubMatrice[i][j-1]
			scoreUp = globalSubMatrice[i-1][j]

			i1 = self._Blosum.getIndex(self._seq1[i-1])
			i2 = self._Blosum.getIndex(self._seq2[j-1])
			x2 = scoreDiag + self._Blosum.getValue(i1,i2)
			
			if score == scoreUp+self._penalite:
				a1,a2 = self._seq1[i-1],"-"
				i -= 1
			elif score == x2:
				a1,a2 = self._seq1[i-1],self._seq2[j-1]
				i,j = i-1,j-1
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

		return align1,align2,score

	def localSubMatrice(self):
		m,n = len(self._seq1),len(self._seq2)
		matrice = [[0 for i in range(n+1)] for j in range(m+1)]
		pointer = [[0 for i in range(n+1)] for j in range(m+1)]
		maxScore = 0
		maxPos = None

		for i in range(1,m+1):
			for j in range(1,n+1):
				i1 = self._Blosum.getIndex(self._seq1[i-1])
				i2 = self._Blosum.getIndex(self._seq2[j-1])
				diag = matrice[i-1][j-1] + self._Blosum.getValue(i1,i2)
				up = matrice[i-1][j] + self._penalite
				left = matrice[i][j-1] + self._penalite
				score = max(0,diag,up,left)

				matrice[i][j] = score
				if score == 0:
					pointer[i][j] = 0
				if score == up:
					pointer[i][j] = 1
				if score == left:
					pointer[i][j] = 2
				if score == diag:
					pointer[i][j] = 3
				if score >= maxScore:
					maxPos = (i,j)
					maxScore = score

		return matrice,pointer,maxPos

	def traceback(self,matrice,pointer,maxPos):
		align1,align2 = "",""
		i,j = maxPos
		while pointer[i][j] != 0:
			if pointer[i][j] == 3:
				align1 += self._seq1[i-1]
				align2 += self._seq2[j-1]
				i -= 1
				j -= 1
			elif pointer[i][j] == 2:
				align1 += "-"
				align2 += self._seq2[j-1]
				j -= 1
			elif pointer[i][j] == 1:
				align1 += self._seq1[i-1]
				align2 += "-"
				i -= 1

		align1 = align1[::-1]
		align2 = align2[::-1]

		return align1,align2

	def valueInBlosum(self,alpha,beta):
		i1 = self._Blosum.getIndex(alpha)
		i2 = self._Blosum.getIndex(beta)
		
		return self._Blosum.getValue(i1,i2)


	def result(self,align1,align2):
		symbol=""
		found = 0
		score = 0
		identity,similarity = 0,0
		for i in range(len(align1)):
			if align1[i]==align2[i]:
				symbol += align1[i]
				identity += 1
				similarity += 1
				score += self.valueInBlosum(align1[i],align2[i])
			elif align1[i] != align2[i] and align1[i] != "-" and align2[i] != "-":
				score += self.valueInBlosum(align1[i],align2[i])
				for j in range(len(self._similarAA)):
					if align1[i]+align2[i]==self._similarAA[j]:
						found=1
				if found:
					symbol += ":"
					similarity += 1
				found = 0
			elif align1[i] == "-" or align2[i] == "-":
				symbol += " "
				score += self._penalite

		identity = float(identity)/len(align1)*100
		similarity = float(similarity)/len(align2)*100

		return identity,similarity,score

"""
	def calcul_score(self,mat,x,y):
		i1 = self._Blosum.getIndex(self._seq1[x-1])
		i2 = self._Blosum.getIndex(self._seq2[y-1])

		diag = mat[x-1][y-1] + self._Blosum.getValue(i1,i2)
		up = mat[x-1][y] + self._penalite
		left = mat[x][y-1] + self._penalite

		return max(0,diag,up,left)		
"""



















