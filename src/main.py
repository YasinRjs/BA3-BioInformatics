import sys

from Blosum import *
from Sequence import *
from Score import *
from Parser import *


def main():
	fileSeq = "../files/maguk-sequences.fasta"
	fileMatrice = "../files/blosum62.iij"
	parsedFiles = Parser(fileSeq,fileMatrice)
#=============== Sequences ================
	mySequences = parsedFiles.getSeq()
	# for elem in mySequences:
	# 	print(elem)
#==========================================

#================ Blosum ==================
	listAA = parsedFiles.getListAA()
	blosum = parsedFiles.getBlosum()
	blosumObj = Blosum(listAA,blosum)
	#print(blosumMatrice)

	# print(mySequences[0])
	# print(mySequences[1])
	x1 = mySequences[0].getSeq()
	x2 = mySequences[2].getSeq()
	x1 = ["T","H","I","S","L","I","N","E"]
	x2 = ["I","S","A","L","I","G","N","E","D"]

	x1 = ["T","H","I","S","L","I","N","E","D","E","D","E","D"]
	x2 = ["I","S","A","L","I","G","N","E","D","A","D","I"]

	print(x1)
	print(x2)
	test = Score(x1,x2,blosumObj,-4)

#==========================================

if __name__=="__main__":
	main()