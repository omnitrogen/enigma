from tkinter import *
import time

root = Tk()
root.title("The Enigma Machine")
root.configure(background='white')

cadre     = PhotoImage(file="cadre.gif")
liaisons  = PhotoImage(file="liaisons.gif")
liaisons2 = PhotoImage(file="liaisons2.gif")
liaisons3 = PhotoImage(file="liaisons3.gif")
reflector = PhotoImage(file="reflector.gif")
abc       = PhotoImage(file="abc.gif")
entry     = PhotoImage(file="entry.gif")

canvas = Canvas(root, width = 1440, height = 500)  

canvas.create_line(87,120,149,120, fill="grey",width=0)
canvas.create_line(87,172,149,172, fill="grey",width=0)
canvas.create_line(87,224,149,224, fill="grey",width=0)
canvas.create_line(87,276,149,276, fill="grey",width=0)
canvas.create_line(87,328,149,328, fill="grey",width=0)
canvas.create_line(87,380,149,380, fill="grey",width=0)

canvas.create_line(390,120,499,120, fill="grey",width=0)
canvas.create_line(390,172,499,172, fill="grey",width=0)
canvas.create_line(390,224,499,224, fill="grey",width=0)
canvas.create_line(390,276,499,276, fill="grey",width=0)
canvas.create_line(390,328,499,328, fill="grey",width=0)
canvas.create_line(390,380,499,380, fill="grey",width=0)

canvas.create_line(740,120,849,120, fill="grey",width=0)
canvas.create_line(740,172,849,172, fill="grey",width=0)
canvas.create_line(740,224,849,224, fill="grey",width=0)
canvas.create_line(740,276,849,276, fill="grey",width=0)
canvas.create_line(740,328,849,328, fill="grey",width=0)
canvas.create_line(740,380,849,380, fill="grey",width=0)

canvas.create_line(1090,120,1203,120, fill="grey",width=0)
canvas.create_line(1090,172,1203,172, fill="grey",width=0)
canvas.create_line(1090,224,1203,224, fill="grey",width=0)
canvas.create_line(1090,276,1203,276, fill="grey",width=0)
canvas.create_line(1090,328,1203,328, fill="grey",width=0)
canvas.create_line(1090,380,1203,380, fill="grey",width=0)

cadreCanvas1    = canvas.create_image(270,250, image=cadre)
liaisonsCanvas1 = canvas.create_image(272,405, image=liaisons)
cadreCanvas2    = canvas.create_image(620,250, image=cadre)
liaisonsCanvas2 = canvas.create_image(620,405, image=liaisons2)
cadreCanvas3    = canvas.create_image(970,250, image=cadre)
liaisonsCanvas3 = canvas.create_image(970,402, image=liaisons3)

reflectorCanvas = canvas.create_image(1300,250, image=reflector)

entryCanvas     = canvas.create_image(70,251, image=entry)

rectangle1      = canvas.create_rectangle(0, 0, 1440, 93, fill="white", width=0)
rectangle2      = canvas.create_rectangle(0, 408, 1440, 900, fill="white", width=0)

canvas.pack()

i1,i2,i3 = 0,0,0

def animate(line, sens):
	coord = canvas.coords(line)
	coord = [int(x) for x in coord]
	if sens:
		lineAnimate = canvas.create_line(coord[0],coord[1],coord[0],coord[1],fill="red", width="5")
		for elt in range(coord[0], coord[2]+1,1):
			canvas.coords(lineAnimate, coord[0],coord[1], elt, coord[1])
			time.sleep(0.0000001)
			canvas.update()
	if not sens:
		lineAnimate = canvas.create_line(coord[2],coord[1],coord[2],coord[1],fill="green", width="5")
		for elt in range(coord[2]+1, coord[0],-1):
			canvas.coords(lineAnimate, coord[2],coord[1], elt, coord[1])
			time.sleep(0.0000001)
			canvas.update()

def rotate(liaisonsCanvas):
	global i1,i2,i3
	for it in range(52):
		canvas.move(liaisonsCanvas,0,-1)
		canvas.update()
		time.sleep(0.01)
	if liaisonsCanvas == liaisonsCanvas1:
		i1 += 1
	elif liaisonsCanvas == liaisonsCanvas2:
		i2 += 1
	elif liaisonsCanvas == liaisonsCanvas3:
		i3 += 1

def reinitialiser():
	global i1, i2, i3
	canvas.move(liaisonsCanvas1, 0, i1*52)
	canvas.move(liaisonsCanvas2, 0, i2*52)
	canvas.move(liaisonsCanvas3, 0, i3*52) 
	i1, i2, i3 = 0, 0, 0

def rotationRotor(liste1):
	liste1.append(liste1[0])
	del liste1[0]
	return liste1

def codePath():
	global i1, i2, i3
	rotor1List = [3,5,2,6,4,1]
	rotor2List = [6,1,4,2,3,5]
	rotor3List = [3,5,1,6,4,2]
	reflecList = [5,6,4,3,1,2]
	for it in range(i1):
		rotationRotor(rotor1List)
	for it in range(i2):
		rotationRotor(rotor2List)
	for it in range(i3):
		rotationRotor(rotor3List)
	print(rotor1List)
	letter = "A"
	ligneDepart = 3
	a = rotor1List[ligneDepart-1]
	b = rotor2List[a-1]
	c = rotor3List[b-1]
	d = reflecList[c-1]
	e = rotor3List.index(d) + 1
	f = rotor2List.index(e) + 1
	g = rotor1List.index(f) + 1
	print(a,b,c,d,e,f,g)
	dic = {"11":"1","12":"2","13":"3","14":"4","15":"5","16":"6","21":"7","22":"8","23":"9","24":"10","25":"11","26":"12","31":"13","32":"14","33":"15","34":"16","35":"17","36":"18","41":"19","42":"20","43":"21","44":"22","45":"23","46":"24"}
	animate(dic.get("1"+str(ligneDepart)),1)
	animate(dic.get("2"+str(a)),1)
	animate(dic.get("3"+str(b)),1)
	animate(dic.get("4"+str(c)),1)
	animate(dic.get("4"+str(d)),0)
	animate(dic.get("3"+str(e)),0)
	animate(dic.get("2"+str(f)),0)
	animate(dic.get("1"+str(g)),0)

'''
rotor1List = [(1,3),(2,5),(3,2),(4,6),(5,4),(6,1)]
rotor2List = [(1,6),(2,1),(3,4),(4,2),(5,3),(6,5)]
rotor3List = [(1,3),(2,5),(3,1),(4,6),(5,4),(6,2)]
reflecList = [(1,5),(2,6),(3,4),(4,3),(5,1),(6,2)]
'''

buttonReinit = Button(text="Reinitialiser", command=reinitialiser)
buttonReinit.pack(padx=155, pady=20, side=LEFT)

buttonRotate1 = Button(text="Rotate 1", command= lambda: rotate(liaisonsCanvas1))
buttonRotate1.pack(padx=20, pady=20, side=LEFT)

buttonRotate2 = Button(text="Rotate 2", command= lambda: rotate(liaisonsCanvas2))
buttonRotate2.pack(padx=20, pady=20, side=LEFT)

buttonRotate3 = Button(text="Rotate 3", command= lambda: rotate(liaisonsCanvas3))
buttonRotate3.pack(padx=20, pady=20, side=LEFT)

buttonAnimateLine = Button(text="Animate Line", command= lambda: animate(line1,1))
buttonAnimateLine.pack(padx=20, pady=20, side=LEFT)

coderPath = Button(text="coder", command= codePath)
coderPath.pack(padx=20, pady=20, side=LEFT)

#coded with <3 by omnitrogen

mainloop()