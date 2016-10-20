from Sequence import *

class Parser:
	def __init__(self,fileSeq,fileMatrice):
		self._listAA,self._matriceBlosum = self.parseMat(fileMatrice)
		self._listSeq = self.parseSeq(fileSeq)

	def getListAA(self):
		return self._listAA
	def getBlosum(self):
		return self._matriceBlosum
	def getSeq(self):
		return self._listSeq

	def parseSeq(self,fileSeq):
		#=================================================
		#==== A METTRE LORS DE LA REMISE ===
		#inputFile = input("fullPath of Sequence file : ")
		inputFile = fileSeq
		#=================================================
		f = open(inputFile,"r")
		initSeq = ">"
		seq = ""
		listSequences = []
		for line in f:
			if line[0] == initSeq:
				# On ajoute le precedent element
				if len(seq) > 0:
					listSequences.append(Sequence(seq,name,ref,number))
				splittedLine = line.split("|")
				name = splittedLine[0][1:]
				ref = splittedLine[1]
				number = splittedLine[2]
				seq = ""
			else:
				seq += line
				if seq[-1] == "\n":
					seq = seq[:len(seq)-1]
		# Add last
		listSequences.append(Sequence(seq,name,ref,number))
		f.close()

		return listSequences

	def parseMat(self,fileMatrice):
		#=================================================
		#==== A METTRE LORS DE LA REMISE ===
		#inputFile = input("fullPath of Sequence file : ")
		inputFile = fileMatrice
		#=================================================
		f = open(inputFile,"r")
		actualLine = f.readline()
		while actualLine[0] == "#":
			actualLine = f.readline();

		newLine = actualLine.strip()
		listAA = newLine.split("   ")
		sizeMatrice = len(listAA)
		#=================================================
		#==== MATRICE DE FAIBLE ====
		# matriceBlosum = []
		# for i in range(sizeMatrice):
		# 	matriceBlosum.append([0 for k in range(i+1)])
		matriceBlosum = [[0 for i in range(sizeMatrice)] for j in range(sizeMatrice)]

		for i in range(sizeMatrice):
			listNumberInLine = f.readline().strip().split("  ")
			for j in range(len(listNumberInLine)):
				matriceBlosum[i][j] = int(listNumberInLine[j].strip())
				matriceBlosum[j][i] = int(listNumberInLine[j].strip())

		return listAA,matriceBlosum