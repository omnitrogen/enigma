#!/usr/bin/python3
#enigma-graphical-user-interface-version

#import_librairies
from tkinter import *
from tkinter.messagebox import *
import time

#window
fenetre = Tk()
fenetre.title("The Enigma Machine")
fenetre.configure(background='white')

i1,i2,i3 = 0,0,0
animateIncremente = 35

def animationTop():

    global i1,i2,i3, animateIncremente
    fenetreTop = Toplevel()
    fenetreTop.title("The Enigma Machine")
    fenetreTop.configure(background='white')
    fenetreTop.grab_set()

    cadre     = PhotoImage(file="cadre.gif")
    liaisons1 = PhotoImage(file="liaisons1.gif")
    liaisons2 = PhotoImage(file="liaisons2.gif")
    liaisons3 = PhotoImage(file="liaisons3.gif")
    reflector = PhotoImage(file="reflector.gif")
    abc       = PhotoImage(file="abc.gif")
    entry     = PhotoImage(file="entry.gif")

    canvas = Canvas(fenetreTop, width = 1440, height = 500, borderwidth=0, background='white',highlightthickness=0)

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

    def animate(line, sens):
        global animateIncremente
        coord = canvas.coords(line)
        coord = [int(x) for x in coord]
        if sens:
            canvas.create_line(coord[0],coord[1],coord[0],coord[1],fill="green", width="5")
            for elt in range(coord[0], coord[2]+1,1):
                canvas.coords(str(animateIncremente), coord[0],coord[1], elt, coord[1])
                time.sleep(int(speedVar.get())/100)
                canvas.update()
        if not sens:
            canvas.create_line(coord[2],coord[1],coord[2],coord[1],fill="green", width="5")
            for elt in range(coord[2]-1, coord[0],-1):
                canvas.coords(str(animateIncremente), coord[2],coord[1], elt, coord[1])
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
        '''
        def estValide(liste1):
            if liste1 == []:
                return False
            for elt in liste1:
                if alphabet.count(elt.upper()) < 1:
                    return False
            return True
        '''
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
            effacerLignes()
            time.sleep(2)
            nbRotation += 1

    frameButton = Frame(fenetreTop,background='white')

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
    entryLetter = Entry(fenetreTop, textvariable = entryvar, width=20, background='white')
    entryLetter.focus_set()
    entryLetter.bind("<Return>", codePath)
    entryLetter.pack(padx=5, pady=5)

    sortieLabelVar = StringVar()
    sortieLabel = Label(fenetreTop,textvariable=sortieLabelVar, borderwidth=0, background='white',highlightthickness=0,font=(None,20))
    sortieLabel.pack()

    coderPath = Button(text="coder", command= codePath)
    coderPath.pack(padx=5, pady=5)

    buttonReinit = Button(fenetreTop,text="Reinitialiser", command=reinitialiser)
    buttonReinit.pack(padx=5, pady=5)

    #credits
    credits = Label(fenetreTop, text = "coded with <3 by omnitrogen", background='white')
    credits.pack(side = BOTTOM, padx=10, pady=10)

    fenetreTop.mainloop()


#menu
def afficherTest():
    print("test")
def helpIt():
    showinfo("The Enigma Machine Quick Start", "Hello World!\n\nThis is a quick tutorial on how to use this app!\n\nFirst, you need to choose the order of the rotors.\n\nThen you need to set the rotors' position\n\nYou can finally write your message and encrypt it by pressing the Return key!\n\nThat's it, you've just encrypt your first enigma message!\n\n                              Have fun!")

menubar = Menu(fenetre)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Animation", command=animationTop)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Tutorial", command=helpIt)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
fenetre.config(menu=menubar)

#enigma_image
image = PhotoImage(file="enigma.gif")
Label(fenetre, image=image, background='white').pack(padx=10, pady=20, side=TOP)

'''
#help_button
def help():
    showinfo("The Enigma Machine Quick Start", "Hello World!\n\nThis is a quick tutorial on how to use this app!\n\nFirst, you need to choose the order of the rotors.\n\nThen you need to set the rotors' position\n\nYou can finally write your message and encrypt it by pressing the Return key!\n\nThat's it, you've just encrypt your first enigma message!\n\n                              Have fun!")
helpButton = Button(fenetre, text ="Help! Quick Start", command = help, background='white')
helpButton.pack(padx=5, pady=5)
'''
#spinboxes_choose_rotors
frameRotor = Frame(fenetre, background='white')

var4 = StringVar()
spinbox = Spinbox(frameRotor, values = ("rotor1=[J,G,D,Q,O,X,U,S,C,A,M,I,F,R,V,T,P,N,E,W,K,B,L,Z,Y,H]",
"rotor2=[N,T,Z,P,S,F,B,O,K,M,W,R,C,J,D,I,V,L,A,E,Y,U,X,H,G,Q]",
"rotor3=[J,V,I,U,B,H,T,C,D,Y,A,K,E,Q,Z,P,O,S,G,X,N,R,M,W,F,L]"), textvariable=var4, width=44)
var4.set("rotor1=[J,G,D,Q,O,X,U,S,C,A,M,I,F,R,V,T,P,N,E,W,K,B,L,Z,Y,H]")
spinbox.grid(row=0, column=1)

var5 = StringVar()
spinbox = Spinbox(frameRotor, values = ("rotor1=[J,G,D,Q,O,X,U,S,C,A,M,I,F,R,V,T,P,N,E,W,K,B,L,Z,Y,H]",
"rotor2=[N,T,Z,P,S,F,B,O,K,M,W,R,C,J,D,I,V,L,A,E,Y,U,X,H,G,Q]",
"rotor3=[J,V,I,U,B,H,T,C,D,Y,A,K,E,Q,Z,P,O,S,G,X,N,R,M,W,F,L]"), textvariable=var5, width=44)
var5.set("rotor2=[N,T,Z,P,S,F,B,O,K,M,W,R,C,J,D,I,V,L,A,E,Y,U,X,H,G,Q]")
spinbox.grid(row=1, column=1)

var6 = StringVar()
spinbox = Spinbox(frameRotor, values = ("rotor1=[J,G,D,Q,O,X,U,S,C,A,M,I,F,R,V,T,P,N,E,W,K,B,L,Z,Y,H]",
"rotor2=[N,T,Z,P,S,F,B,O,K,M,W,R,C,J,D,I,V,L,A,E,Y,U,X,H,G,Q]",
"rotor3=[J,V,I,U,B,H,T,C,D,Y,A,K,E,Q,Z,P,O,S,G,X,N,R,M,W,F,L]"), textvariable=var6, width=44)
var6.set("rotor3=[J,V,I,U,B,H,T,C,D,Y,A,K,E,Q,Z,P,O,S,G,X,N,R,M,W,F,L]")
spinbox.grid(row=2, column=1)

var7 = StringVar()
spinbox = Spinbox(frameRotor, values = ("reflec=[Y,R,U,H,Q,S,L,D,P,X,N,G,O,K,M,I,E,B,F,Z,C,W,V,J,A,T]"), textvariable=var7, width=44)
var7.set("reflec=[Y,R,U,H,Q,S,L,D,P,X,N,G,O,K,M,I,E,B,F,Z,C,W,V,J,A,T]")
spinbox.grid(row=3, column=1)

rotorn1 = Label(frameRotor, text='Slot n°=1:', padx=10, pady=5, background='white')
rotorn1.grid(row=0, column=0)
rotorn2 = Label(frameRotor, text='Slot n°=2:', padx=10, pady=5, background='white')
rotorn2.grid(row=1, column=0)
rotorn3 = Label(frameRotor, text='Slot n°=3:', padx=10, pady=5, background='white')
rotorn3.grid(row=2, column=0)
reflectorn = Label(frameRotor, text='Reflector:', padx=10, pady=5, background='white')
reflectorn.grid(row=3, column=0)

frameRotor.pack()

#frame_to_set_rotor_position
frame1 = Frame(fenetre, borderwidth=0, relief=FLAT, background='white')
frame1.pack(side=TOP, padx=10, pady=10)

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

rotor1lab = Label(frame1, text='Rotor 1', padx=10, pady=5, borderwidth=0, background='white')
rotor1lab.grid(row=0, column=0)
rotor2lab = Label(frame1, text='Rotor 2', padx=10, pady=5, borderwidth=0, background='white')
rotor2lab.grid(row=0, column=1)
rotor3lab = Label(frame1, text='Rotor 3', padx=10, pady=5, borderwidth=0, background='white')
rotor3lab.grid(row=0, column=2)

#scales_choose_position
var1 = DoubleVar()
scale = Scale(frame1, from_=1, to=26, variable = var1, cursor='dot', showvalue=0, command=update1, length= 100, background='white')
scale.grid(row=1, column=0, padx=60, pady=10)
var2 = DoubleVar()
scale = Scale(frame1, from_=1, to=26, variable = var2, cursor='dot', showvalue=0, command=update2, length= 100, background='white')
scale.grid(row=1, column=1, padx=60, pady=10)
var3 = DoubleVar()
scale = Scale(frame1, from_=1, to=26, variable = var3, cursor='dot', showvalue=0, command=update3, length= 100, background='white')
scale.grid(row=1, column=2, padx=60, pady=10)

lab1 = Label(frame1, background='white')
lab1.grid(row=2, column=0)
lab2 = Label(frame1, background='white')
lab2.grid(row=2, column=1)
lab3 = Label(frame1, background='white')
lab3.grid(row=2, column=2)

#function_code
def code(event=None):
    a = int(var1.get())
    b = int(var2.get())
    c = int(var3.get())
    def rotationRotor(liste1):
        liste1.append(liste1[0])
        del liste1[0]
        return liste1
    def estValide(liste1):
        if liste1 == []:
            return False
        for elt in liste1:
            if elt == " ":
                pass
            elif alphabetList.count(elt.upper()) < 1:
                return False
        return True
    sortie = entryvar.get()

    var4str = var4.get()
    var4list = list(var4str)
    var5str = var5.get()
    var5list = list(var5str)
    var6str = var6.get()
    var6list = list(var6str)

    if var4list[5] == '1':
        rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    elif var4list[5] == '2':
        rotor1 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    elif var4list[5] == '3':
        rotor1 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
    if var5list[5] == '1':
        rotor2 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    elif var5list[5] == '2':
        rotor2 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    elif var5list[5] == '3':
        rotor2 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
    if var6list[5] == '1':
        rotor3 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    elif var6list[5] == '2':
        rotor3 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    elif var6list[5] == '3':
        rotor3 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']

    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    alphabetDict = {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14, 'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16, 'B': 2, 'H': 8, 'K': 11, 'C': 3}
    #rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    #rotor2 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    #rotor3 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
    reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

    for loop1 in range(a):
        rotationRotor(rotor1)
    for loop2 in range(b):
        rotationRotor(rotor2)
    for loop3 in range(c):
        rotationRotor(rotor3)

    sortieListe = list(sortie)
    print(sortieListe)
    sortieListe = [x for x in sortieListe if x != " "]
    print(sortieListe)

    if not estValide(sortieListe):
        value = StringVar()
        value.set('Please enter only letters!')
        liste.insert(END, value.get())
        liste.itemconfig(END, {'bg':'red'})
        liste.see("end")
    elif (var4list[5] == var5list[5] == var6list[5]) or (var4list[5] == var5list[5]) or (var4list[5] == var6list[5]) or (var5list[5] == var6list[5]):
        value = StringVar()
        value.set('You can only use a rotor once!')
        liste.insert(END, value.get())
        liste.itemconfig(END, {'bg':'red'})
        liste.see("end")
    else:
        s = []
        for i in range(0,len(sortieListe),1):
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
            if (i+1) % 1 == 0:
                rotationRotor(rotor1)
            if (i+1) % 26 == 0:
                rotationRotor(rotor2)
            if (i+1) % 676 == 0:
                rotationRotor(rotor3)
        value = StringVar()
        value.set(''.join(s))
        liste.insert(END, value.get())
        liste.see("end")

#text_entry
entryvar = StringVar()
entry = Entry(fenetre, textvariable = entryvar, width=50, background='white')
entry.focus_set()
entry.bind("<Return>", code)
entry.pack(padx=10, pady=10)

#clear_listbox
def clear():
    liste.delete(0, END)

'''
#button_to_(de)code
b1 = Button(fenetre, text="(de)code", width=10, command=code, background='white')
b1.pack()
'''
#store_results
f1 = Frame(fenetre)
s1 = Scrollbar(f1)
liste = Listbox(f1, height=5, width=50, borderwidth=0, background='white')
s1.config(command = liste.yview)
liste.config(yscrollcommand = s1.set)
liste.pack(side = LEFT, fill = Y, padx=5, pady=5)
s1.pack(side = RIGHT, fill = Y)
f1.pack()

#button_to_clear_listbox
b2 = Button(fenetre, text="clear list", width=10, command=clear, background='white')
b2.pack(padx=5, pady=5)

#credits
credits = Label(fenetre, text = "coded with <3 by omnitrogen", background='white')
credits.pack(side = BOTTOM, padx=10, pady=10)

#quit_button
quitButton = Button(fenetre, text="quit", width=10, command=fenetre.quit, background='white')
quitButton.pack(side = BOTTOM)

mainloop()
