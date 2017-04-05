#enigma-gui

from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk  

#debut_fenetre
fenetre = Tk()
fenetre.title("The Enigma Machine")

#image_enigma
image = Image.open("enigma.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo # keep a reference!
label.pack(padx= 20, pady= 20)

#entree
entryvar = StringVar()
entry = Entry(fenetre, textvariable = entryvar)
entry.pack()
entry.focus_set()

def code():
    sortie = entryvar.get()
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', "'"]
    alphabetDict = {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14, 'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16, 'B': 2, 'H': 8, 'K': 11, 'C': 3}
    rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    rotor2 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    rotor3 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
    reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
	def rotationRotor(liste1):
		liste1.append(liste1[0])
		del liste1[0]
		return liste1
	def estValide(liste1):
		for elt in liste1:
			if alphabetList.count(elt.upper()) < 1:
				return False
		return True

    sortieListe = list(sortie)
    #if estValide(sortieListe):
    s = []
	for i in range(0,len(sortieListe),1):
		if sortieListe[i] == ' ':
			s.append(' ')
		elif sortieListe[i] == "'":
			s.append("'")
		else:
			a = alphabetDict[sortieListe[i].upper()]
			b = rotor1[a-1]
			c = alphabetDict[b]
			d = rotor2[c-1]
			e = alphabetDict[d]
			f = rotor3[e-1]
			g = alphabetDict[f]
			h = reflector[g-1]
			j = rotor3.index(h)
			k = alphabetList[j]
			l = rotor2.index(k)
			m = alphabetList[l]
			n = rotor1.index(m)
			o = alphabetList[n]
			s.append(o)
		if (i+1)%1 == 0:
			rotationRotor(rotor1)
		if (i+1)%26 == 0:
			rotationRotor(rotor2)
		if (i+1)%676 == 0:
			rotationRotor(rotor3)
    resultat = Label(fenetre, text = ''.join(s))
    resultat.pack(padx=10, pady=10)
	

b = Button(fenetre, text="(de)code", width=10, command=(code))
b.pack()

#copyright
copyright = Label(fenetre, text = "coded with <3 by omnitrogen")
copyright.pack(side = BOTTOM, padx=10, pady=10)


#boutton_quit
bouttonTest = Button(fenetre, text="quit", width=10, command=fenetre.quit)
bouttonTest.pack(side = BOTTOM)

mainloop()