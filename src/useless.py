#=============================================
			# score = self._globalSubMatrice[i][j]
			# scoreDiag = self._globalSubMatrice[i-1][j-1]
			# scoreUp = self._globalSubMatrice[i][j-1]
			# scoreLeft = self._globalSubMatrice[i-1][j]


			# score = self._globalSubMatrice[i+1][j+1]
			# scoreDiag = self._globalSubMatrice[i][j]
			# scoreUp = self._globalSubMatrice[i+1][j]
			# scoreLeft = self._globalSubMatrice[i][j+1]


			# score = self._globalSubMatrice[j][i]
			# scoreDiag = self._globalSubMatrice[j-1][i-1]
			# scoreUp = self._globalSubMatrice[j][i-1]
			# scoreLeft = self._globalSubMatrice[j-1][i]

			# score = self._globalSubMatrice[i][j]
			# scoreDiag = self._globalSubMatrice[i-1][j-1]
			# scoreUp = self._globalSubMatrice[i-1][j]
			# scoreLeft = self._globalSubMatrice[i][j-1]
"""
			score = self._globalSubMatrice[j][i]
			scoreDiag = self._globalSubMatrice[j-1][i-1]
			scoreUp = self._globalSubMatrice[j-1][i]
			scoreLeft = self._globalSubMatrice[j][i-1]

			score = self._globalSubMatrice[i][j]
			scoreDiag = self._globalSubMatrice[i-1][j-1]
			scoreUp = self._globalSubMatrice[i-1][j]
			scoreLeft = self._globalSubMatrice[i][j-1]


		while (i>0 and j>0):
			score = self._globalSubMatrice[i][j]
			scoreDiag = self._globalSubMatrice[i-1][j-1]
			scoreLeft = self._globalSubMatrice[i][j-1]
			scoreUp = self._globalSubMatrice[i-1][j]

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

