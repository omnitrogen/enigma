#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#enigma-explanation-animation
from tkinter import *
import time

root = Tk()
root.geometry("1200x600")

canvas = Canvas(root, width=1200, height=600, bg="grey", borderwidth=0, highlightthickness=0)
#rect = canvas.create_rectangle(0, 0, 200, 200, fill="blue", width=1)

imageTot = PhotoImage(file="enigma-animation.gif")
Label(canvas, image=imageTot, background='white', borderwidth=0, highlightthickness=0).pack(padx=0, pady=0, side=TOP)

photo = PhotoImage(file ='rotor1.gif')
rotor1 = canvas.create_image(500, 70, image=photo)
#rotor1.pack()
canvas.update()
'''
imageRotor = PhotoImage(file="rotor1.gif")
rotor1 = Label(canvas, image=imageRotor, background='white', borderwidth=0, highlightthickness=0)
rotor1.pack(padx=0, pady=0)
rotor1.place(x=460, y=60)
canvas.pack()
'''

canvas.pack()

#for it in range(2000):
#	canvas.move(rect,1,0)
#	time.sleep(0.01)
#	canvas.update()


mainloop()

