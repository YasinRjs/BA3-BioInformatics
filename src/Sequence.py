class Sequence:
	def __init__(self,seq,name,ref,number):
		self._seq = seq
		self._name = name
		self._ref = ref
		self._number = number
	def __str__(self):
		return ("==> "+self._seq)
	def getSeq(self):
		return self._seq
	def getName(self):
		return self._name
	def getRef(self):
		return self._ref
	def getNumber(self):
		return self._number