#!/usr/bin/python3

from tkinter import *
import time

root = Tk()
root.title("The Enigma Machine")
root.configure(background='white')

cadre     = PhotoImage(file="cadre.gif")
liaisons1 = PhotoImage(file="liaisons1.gif")
liaisons2 = PhotoImage(file="liaisons2.gif")
liaisons3 = PhotoImage(file="liaisons3.gif")
reflector = PhotoImage(file="reflector.gif")
abc       = PhotoImage(file="abc.gif")
entry     = PhotoImage(file="entry.gif")

canvas = Canvas(root, width = 1440, height = 500, borderwidth=0, background='white',highlightthickness=0)

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
liaisonsCanvas1 = canvas.create_image(272,718, image=liaisons1)
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
animateIncremente = 35
def animate(line, sens):
    global animateIncremente
    coord = canvas.coords(line)  # récupère les coordonnées de la ligne (x0,y0,x1,y1)
    coord = [int(x) for x in coord]
    if sens:  # sens de gauche à droite
        canvas.create_line(coord[0],coord[1],coord[0],coord[1],fill="green", width="5")
        for elt in range(coord[0], coord[2]+1,1):  # boucle se répétant autant de fois que la longueur de la ligne en pixel
            canvas.coords(str(animateIncremente), coord[0],coord[1], elt, coord[1])  # on met à jour les coordonnées de la ligne -> on la fait "grandir"
            time.sleep(int(speedVar.get())/100)
            canvas.update()
    if not sens:  # sens de droite à gauche
        canvas.create_line(coord[2],coord[1],coord[2],coord[1],fill="green", width="5")
        for elt in range(coord[2]-1, coord[0],-1):  # boucle se répétant autant de fois que la longueur de la ligne en pixel
            canvas.coords(str(animateIncremente), coord[2],coord[1], elt, coord[1])  # on met à jour les coordonnées de la ligne -> on la fait "grandir"
            time.sleep(int(speedVar.get())/100)
            canvas.update()
    animateIncremente += 1

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
    canvas.delete('35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199')
    sortieLabelVar.set('')
    i1, i2, i3 = 0, 0, 0

def rotationRotor(liste1):
    liste1.append(liste1[0])
    del liste1[0]
    return liste1

def circle(numLigne,color):
    numLigne = numLigne % 6
    if numLigne == 6 or numLigne == 0:
        canvas.create_oval(54,367,81,394, outline=color, width="2")
    if numLigne == 5:
        canvas.create_oval(54,317,81,344, outline=color, width="2")
    if numLigne == 4:
        canvas.create_oval(54,262,81,289, outline=color, width="2")
    if numLigne == 3:
        canvas.create_oval(54,210,81,237, outline=color, width="2")
    if numLigne == 2:
        canvas.create_oval(54,159,81,186, outline=color, width="2")
    if numLigne == 1:
        canvas.create_oval(54,107,81,134, outline=color, width="2")
    canvas.update()

def effacerLignes():
    canvas.delete('35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199')
    canvas.update()

def codePath(event=None):
    lettresEntrees = list(entryvar.get())
    speedInt = int(speedVar.get())
    print(speedInt)
    nbRotation = 0
    alphabet = ["A", "B", "C", "D", "E", "F"]
    resultList = []
    reflecList = [5,0,4,3,1,2]

    r1G = [3,5,2,0,4,1]
    r2G = [0,1,4,2,3,5]
    r3G = [3,5,1,0,4,2]

    r1D = [6,3,1,5,2,4]
    r2D = [2,4,5,3,6,1]
    r3D = [3,6,1,5,2,4]

    for elt in lettresEntrees:
        ligneDepart = alphabet.index(str.upper(elt)) + 1
        a = r1G[ligneDepart-1] - i1
        b = r2G[(a-1) % 6] - i2
        c = r3G[(b-1) % 6] - i3
        d = reflecList[(c-1) % 6]
        e = r3D[(d-1) % 6] - i3
        f = r2D[(e-1) % 6] - i2
        g = r1D[(f-1) % 6] - i1
        print(ligneDepart,a,b,c,d,e,f,g)
        dic = {"10":"6","20":"12","30":"18","40":"24","11":"1","12":"2","13":"3","14":"4","15":"5","16":"6","21":"7","22":"8","23":"9","24":"10","25":"11","26":"12","31":"13","32":"14","33":"15","34":"16","35":"17","36":"18","41":"19","42":"20","43":"21","44":"22","45":"23","46":"24"}
        for loop in range(nbRotation+1):
            animate(dic.get("1"+str(ligneDepart)),1)
            time.sleep(speedInt/10)
        animate(dic.get("2"+str(a % 6)),1)
        time.sleep(speedInt/10)
        animate(dic.get("3"+str(b % 6)),1)
        time.sleep(speedInt/10)
        animate(dic.get("4"+str(c % 6)),1)
        time.sleep(speedInt/10)
        animate(dic.get("4"+str(d)),0)
        time.sleep(speedInt/10)
        animate(dic.get("3"+str(e % 6)),0)
        time.sleep(speedInt/10)
        animate(dic.get("2"+str(f % 6)),0)
        time.sleep(speedInt/10)
        animate(dic.get("1"+str(g % 6)),0)
        time.sleep(speedInt/10)
        circle(g,"red")
        resultList.append(alphabet[(g-1) % 6])
        print("ok")
        sortieLabelVar.set(resultList)
        time.sleep(5)
        effacerLignes()
        time.sleep(2)
        if (nbRotation+1) % 1 == 0:
            rotate(liaisonsCanvas1)
            rotationRotor(r1G)
            rotationRotor(r1D)
        if (nbRotation+1) % 6 == 0:
            rotate(liaisonsCanvas2)
            rotationRotor(r2G)
            rotationRotor(r2D)
        if (nbRotation+1) % 36 == 0:
            rotate(liaisonsCanvas3)
            rotationRotor(r3G)
            rotationRotor(r3D)
        time.sleep(2)
        nbRotation += 1


frameButton = Frame(root,background='white')

buttonRotate1 = Button(frameButton,text="Rotate 1", command= lambda: rotate(liaisonsCanvas1))
buttonRotate1.grid(row=1, column=0,padx=50)

buttonRotate2 = Button(frameButton,text="Rotate 2", command= lambda: rotate(liaisonsCanvas2))
buttonRotate2.grid(row=1, column=1,padx=50)

buttonRotate3 = Button(frameButton,text="Rotate 3", command= lambda: rotate(liaisonsCanvas3))
buttonRotate3.grid(row=1, column=2,padx=50)

labelSpeed = Label(frameButton,text="Enter speed (0:fastest, 1,2:slower):")
labelSpeed.grid(row=1, column=3, padx=20)

speedVar = StringVar()
speedEntry = Entry(frameButton, textvariable = speedVar, width=2, background='white')
speedEntry.insert(END, "0")
speedEntry.grid(row=1, column=4,padx=0)

frameButton.pack(pady=20)

entryvar = StringVar()
entryLetter = Entry(root, textvariable = entryvar, width=10, background='white')
entryLetter.focus_set()
entryLetter.bind("<Return>", codePath)
entryLetter.pack(padx=5, pady=5)

sortieLabelVar = StringVar()
sortieLabel = Label(root,textvariable=sortieLabelVar, borderwidth=0, background='white',highlightthickness=0,font=(None,20))
sortieLabel.pack()


coderPath = Button(text="coder", command= codePath)
coderPath.pack(padx=5, pady=5)

buttonReinit = Button(root,text="Reinitialiser", command=reinitialiser)
buttonReinit.pack(padx=5, pady=5)

#credits
credits = Label(root, text = "coded with <3 by omnitrogen", background='white')
credits.pack(side = BOTTOM, padx=10, pady=10)

mainloop()
