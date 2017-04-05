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
label.image = photo
label.pack(padx= 30, pady= 30)

#frame_rotor_position

frame1 = Frame(fenetre, borderwidth=2, relief=FLAT)
frame1.pack(side=TOP, padx=30, pady=30, )
#Label(frame1, text="frame 1").pack(padx=10, pady=10)

def update1(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab1.configure(text='position : {}'.format(alphabetList[x-1]))
def update2(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab2.configure(text='position : {}'.format(alphabetList[x-1]))
def update3(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab3.configure(text='position : {}'.format(alphabetList[x-1]))

rotor1lab = Label(frame1, text='Rotor 1', padx=20, pady=5)
rotor1lab.grid(row=0, column=0)
rotor2lab = Label(frame1, text='Rotor 2', padx=20, pady=5)
rotor2lab.grid(row=0, column=1)
rotor3lab = Label(frame1, text='Rotor 3', padx=20, pady=5)
rotor3lab.grid(row=0, column=2)

var1 = DoubleVar()
scale = Scale( frame1, from_=1, to=26, variable = var1, cursor='dot', showvalue=0, command=update1, length= 100)
scale.grid(row=1, column=0, padx=20, pady=20)
var2 = DoubleVar()
scale = Scale( frame1, from_=1, to=26, variable = var2, cursor='dot', showvalue=0, command=update2, length= 100 )
scale.grid(row=1, column=1, padx=20, pady=20)
var3 = DoubleVar()
scale = Scale( frame1, from_=1, to=26, variable = var3, cursor='dot', showvalue=0, command=update3, length= 100 )
scale.grid(row=1, column=2, padx=20, pady=20)

lab1 = Label(frame1)
lab1.grid(row=2, column=0)
lab2 = Label(frame1)
lab2.grid(row=2, column=1)
lab3 = Label(frame1)
lab3.grid(row=2, column=2)

#fonction_code
def code(event=None):
	'''
	essayer de get() les trois valeurs des rotations des rotors, puis faire les rotaion nécessaires.
	'''
	a = var1.get()
	a = int(a)
	b = var2.get()
	b = int(b)
	c = var3.get()
	c = int(c)
	def rotationRotor(liste1):
		liste1.append(liste1[0])
		del liste1[0]
		return liste1
	def estValide(liste1):
		for elt in liste1:
			if alphabetList.count(elt.upper()) < 1:
				return False
		return True
	sortie = entryvar.get()
	alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', "'"]
	alphabetDict = {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14, 'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16, 'B': 2, 'H': 8, 'K': 11, 'C': 3}
	rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
	rotor2 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
	rotor3 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
	reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
	for loop1 in range(a):
		rotationRotor(rotor1)
	for loop2 in range(b):
		rotationRotor(rotor2)
	for loop3 in range(c):
		rotationRotor(rotor3)
	sortieListe = list(sortie)
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
	value = StringVar() 
	value.set(''.join(s))
	entree = Entry(fenetre, textvariable=value, width=50)
	entree.pack()
    #resultat = Label(fenetre, state='normal', text = ''.join(s))
    #resultat.pack(padx=10, pady=10)
#entree
entryvar = StringVar()
entry = Entry(fenetre, textvariable = entryvar, width=50)
entry.focus_set()
entry.bind("<Return>", code)
entry.pack()

b = Button(fenetre, text="(de)code", width=10, command=(code))
b.pack()

#copyright
copyright = Label(fenetre, text = "coded with <3 by omnitrogen")
copyright.pack(side = BOTTOM, padx=10, pady=10)


#boutton_quit
bouttonTest = Button(fenetre, text="quit", width=10, command=fenetre.quit)
bouttonTest.pack(side = BOTTOM)

mainloop()
