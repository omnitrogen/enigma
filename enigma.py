#implementation de la machine enigma en python

#import math

class ensembleRotorReflector:
	"""classe définissant un rotor d'énigma, un objet qui aura donc les même propriétés que son analogue physique, à savoir:
	pouvoir effectuer une rotation. On modélisera le rotor par une liste."""

	def __init__(self):
		'''par défaut, on a un alphabet trié et un alphabet "random" de la version d'enigma 1941 (1er rotor).
		On utilise des dictionnaires plutôt que des listes c'est plus facile à traier car les rotors bougent l'un par rapport à l'autre mais pas tout seul.'''
		self.alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.alphabetDict = {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14, 'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16, 'B': 2, 'H': 8, 'K': 11, 'C': 3}
		self.rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
		self.rotor2 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
		self.rotor3 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
		self.reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
		#self.rotor1 = {'O': 'V', 'M': 'F', 'A': 'J', 'N': 'R', 'U': 'K', 'D': 'Q', 'C': 'D', 'Q': 'P', 'E': 'O', 'G': 'U', 'P': 'T', 'Z': 'H', 'V': 'B', 'W': 'L', 'H': 'S', 'X': 'Z', 'J': 'A', 'L': 'I', 'B': 'G', 'F': 'X', 'T': 'W', 'K': 'M', 'I': 'C', 'S': 'E', 'y': 'Y', 'R': 'N'}
		#self.rotor2 = {'O': 'D', 'M': 'C', 'A': 'N', 'N': 'J', 'U': 'Y', 'D': 'P', 'C': 'Z', 'Q': 'V', 'E': 'S', 'G': 'B', 'P': 'I', 'Z': 'Q', 'V': 'U', 'W': 'X', 'H': 'O', 'X': 'H', 'J': 'M', 'L': 'R', 'B': 'T', 'F': 'F', 'T': 'E', 'K': 'W', 'I': 'K', 'S': 'A', 'y': 'G', 'R': 'L'}
		#self.rotor3 = {'O': 'Z', 'M': 'E', 'A': 'J', 'N': 'Q', 'U': 'N', 'D': 'U', 'C': 'I', 'Q': 'O', 'E': 'B', 'G': 'T', 'P': 'P', 'Z': 'L', 'V': 'R', 'W': 'M', 'H': 'C', 'X': 'W', 'J': 'Y', 'L': 'K', 'B': 'V', 'F': 'H', 'T': 'X', 'K': 'A', 'I': 'D', 'S': 'G', 'y': 'F', 'R': 'S'}

	def reverse(self):
		'''permet d'inverser les éléments... peu utile pour le moment'''
		self.rotor1.reverse()

<<<<<<< HEAD
	def rotationRotor(self, test):
		'''permet d'effectuer une rotation du rotor... très utile'''
		self.test.append(self.test[0])
		del self.test[0]


continuer = True
a = ensembleRotorReflector()
i = 1
while continuer:
	lettre = str(input("Entrez une lettre à coder: "))
	r = a.alphabetDict[lettre.upper()]
	print(a.rotor1[r-1])
	for loop in range(i):
		a.rotationRotor(a.rotor1)
	i += 1
	quitter = str(input("Voulez vous continuer ? y or n\n"))
	if quitter == "n":
		continuer = False
	else:
		pass

	def rotationRotor(self, liste1):
		'''on peut mettre un compteur i et le rotor1 rotate quand i%1 = 0, le rotor2 quand i%26 = 0, et le rotor3 quand i%676 = 0. (avec 676 = 26^2)'''
		'''permet d'effectuer une rotation du rotor... très utile'''
		self.liste1.append(self.liste1[0])
		del self.liste1[0]

class rotor1:
	"""docstring for rotor1"""
	def __init__(self):
		self.rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']

		

continuer = True
a = ensembleRotorReflector()
while continuer:
	lettre = str(input("Entrez une lettre à coder: "))
	r = a.alphabetDict[lettre.upper()]
	print(a.rotor1[r-1])
	a.rotationRotor(a.rotor1)
	quitter = str(input("Voulez vous continuer ? y or n\n"))
	if quitter == "n":
		continuer = False
	else:
		pass


>>>>>>> 520dc09c6c21cb170270bc6003193c6b7597962f
'''
a = rotor()
print(a)
print(a.alphabetList)
print(a.rotor1)
rotations = int(input("How many rotations do you want ?\n"))
for i in range(0, rotations):
	a.rotationRotor()
print(a.alphabetList, a.alphabetDict)
print(a.rotor1)
help(rotor.reverse)
'''
'''
a = rotor()
print(a.randAlphabet)
a.rotationRotor()
print(a.randAlphabet)
rotor.rotationRotor(a)
print(a.randAlphabet)
'''
