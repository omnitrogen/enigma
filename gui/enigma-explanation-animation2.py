from tkinter import *
import time

#test

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

class line():
	i = 0
	def __init__(self,x0,y0,x1,y1, color):
		canvas.create_line(x0,y0,x1,y1, fill=str(color),width=0)
'''
		coords = [x0,]
	@staticmethod
	def incremente():
		x += x
		y += y
		i += 1
	def animate(self,color):
		x = (x1-x0)
		y = (y1-y0)
		lineAnimate = canvas.create_line(x0,y0,x/100, y/100,fill=str(color))
		canvas.after(33, incremente)
		canvas.after(33, animate)
		canvas.update()
'''

line1 = line(87,120,149,120,"black")
line2 = line(87,172,149,172,"black")
line3 = line(87,224,149,224,"black")
line4 = line(87,276,149,276,"black")
line5 = line(87,328,149,328,"black")
line6 = line(87,380,149,380,"black")
#line1.animate("green")

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

#coded with <3 by omnitrogen

mainloop()