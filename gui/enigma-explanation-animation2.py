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

line1  = canvas.create_line(87,120,149,120, fill="black",width=0)
line2  = canvas.create_line(87,172,149,172, fill="black",width=0)
line3  = canvas.create_line(87,224,149,224, fill="black",width=0)
line4  = canvas.create_line(87,276,149,276, fill="black",width=0)
line5  = canvas.create_line(87,328,149,328, fill="black",width=0)
line6  = canvas.create_line(87,380,149,380, fill="black",width=0)

line7  = canvas.create_line(390,120,499,120, fill="black",width=0)
line8  = canvas.create_line(390,172,499,172, fill="black",width=0)
line9  = canvas.create_line(390,224,499,224, fill="black",width=0)
line10 = canvas.create_line(390,276,499,276, fill="black",width=0)
line11 = canvas.create_line(390,328,499,328, fill="black",width=0)
line12 = canvas.create_line(390,380,499,380, fill="black",width=0)

line13 = canvas.create_line(87+303+350,120,149+350+350,120, fill="black",width=0)
line14 = canvas.create_line(87+303+350,172,149+350+350,172, fill="black",width=0)
line15 = canvas.create_line(87+303+350,224,149+350+350,224, fill="black",width=0)
line16 = canvas.create_line(87+303+350,276,149+350+350,276, fill="black",width=0)
line17 = canvas.create_line(87+303+350,328,149+350+350,328, fill="black",width=0)
line18 = canvas.create_line(87+303+350,380,149+350+350,380, fill="black",width=0)

line19 = canvas.create_line(87+303+350+350,120,149+350+350+354,120, fill="black",width=0)
line20 = canvas.create_line(87+303+350+350,172,149+350+350+354,172, fill="black",width=0)
line21 = canvas.create_line(87+303+350+350,224,149+350+350+354,224, fill="black",width=0)
line22 = canvas.create_line(87+303+350+350,276,149+350+350+354,276, fill="black",width=0)
line23 = canvas.create_line(87+303+350+350,328,149+350+350+354,328, fill="black",width=0)
line24 = canvas.create_line(87+303+350+350,380,149+350+350+354,380, fill="black",width=0)


cadreCanvas1    = canvas.create_image(270,250, image=cadre)
liaisonsCanvas1 = canvas.create_image(272,405, image=liaisons)
cadreCanvas2    = canvas.create_image(620,250, image=cadre)
liaisonsCanvas2 = canvas.create_image(620,405, image=liaisons2)
cadreCanvas3    = canvas.create_image(970,250, image=cadre)
liaisonsCanvas3 = canvas.create_image(970,405, image=liaisons3)

reflectorCanvas = canvas.create_image(1300,250, image=reflector)

abcCanvas1      = canvas.create_image(445,250, image=abc)
abcCanvas2      = canvas.create_image(795,250, image=abc)
abcCanvas3      = canvas.create_image(1145,250, image=abc)

entryCanvas     = canvas.create_image(70,251, image=entry)

rectangle1      = canvas.create_rectangle(0, 0, 1440, 93, fill="white", width=0)
rectangle2      = canvas.create_rectangle(0, 408, 1440, 900, fill="white", width=0)

def animate(line, coord):
	coord = [int(x) for x in coord]
	lineAnimate = canvas.create_line(coord[0],coord[1],coord[0],coord[1],fill="red", width="3")
	for elt in range(coord[0], coord[2]):
		canvas.coords(lineAnimate, coord[0],coord[1], elt, coord[1])
		abcCanvas1      = canvas.create_image(445,250, image=abc)
		abcCanvas2      = canvas.create_image(795,250, image=abc)
		abcCanvas3      = canvas.create_image(1145,250, image=abc)
		#time.sleep(0.0000001)
		canvas.update()

def animate2():
	animate(line1,  canvas.coords(line1))
	animate(line7,  canvas.coords(line7))
	animate(line13, canvas.coords(line13))
	animate(line19, canvas.coords(line19))


canvas.pack()

i1 = 0
i2 = 0
i3 = 0
def rotate1():
	global i1
	for it in range(52):
		canvas.move(liaisonsCanvas1, 0, -1)
		canvas.update()
		time.sleep(0.01)
	i1 += 1
def rotate2():
	global i2
	for it in range(52):
		canvas.move(liaisonsCanvas2, 0, -1)
		canvas.update()
		time.sleep(0.01)
	i2 += 1
def rotate3():
	global i3
	for it in range(52):
		canvas.move(liaisonsCanvas3, 0, -1)
		canvas.update()
		time.sleep(0.01)
	i3 += 1

def reinitialiser():
	global i1, i2, i3
	canvas.move(liaisonsCanvas1, 0, i1*52)
	canvas.move(liaisonsCanvas2, 0, i2*52)
	canvas.move(liaisonsCanvas3, 0, i3*52) 
	i1, i2, i3 = 0, 0, 0

buttonReinit = Button(text="Reinitialiser", command=reinitialiser)
buttonReinit.pack(padx=155, pady=20, side=LEFT)

buttonRotate1 = Button(text="Rotate 1", command=rotate1)
buttonRotate1.pack(padx=20, pady=20, side=LEFT)

buttonRotate2 = Button(text="Rotate 2", command=rotate2)
buttonRotate2.pack(padx=20, pady=20, side=LEFT)

buttonRotate3 = Button(text="Rotate 3", command=rotate3)
buttonRotate3.pack(padx=20, pady=20, side=LEFT)

buttonAnimateLine = Button(text="Animate Line", command=animate2)
buttonAnimateLine.pack(padx=20, pady=20, side=LEFT)

#coded with <3 by omnitrogen

mainloop()