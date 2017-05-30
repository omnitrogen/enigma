#!/usr/bin/python3
#enigma-graphical-user-interface-version

#import_librairies
from tkinter import *
from tkinter.messagebox import *

#window
fenetre = Tk()
fenetre.title("The Enigma Machine")
fenetre.configure(background='white')

#enigma_image
image = PhotoImage(file="enigma.gif")
Label(fenetre, image=image, background='white').pack(padx=10, pady=10, side=TOP)

#help_button
def help():
    showinfo("The Enigma Machine Quick Start", "Hello World!\n\nThis is a quick tutorial on how to use this app!\n\nFirst, you need to choose the order of the rotors.\n\nThen you need to set the rotors' position\n\nYou can finally write your message and encrypt it by pressing the Return key!\n\nThat's it, you've just encrypt your first enigma message!\n\n                              Have fun!")
helpButton = Button(fenetre, text ="Help! Quick Start", command = help, background='white')
helpButton.pack(padx=5, pady=5)

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
    lab1.configure(text='position : {}'.format(alphabetList[x]))
def update2(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab2.configure(text='position : {}'.format(alphabetList[x]))
def update3(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab3.configure(text='position : {}'.format(alphabetList[x]))

rotor1lab = Label(frame1, text='Rotor 1', padx=10, pady=5, borderwidth=0, background='white')
rotor1lab.grid(row=0, column=0)
rotor2lab = Label(frame1, text='Rotor 2', padx=10, pady=5, borderwidth=0, background='white')
rotor2lab.grid(row=0, column=1)
rotor3lab = Label(frame1, text='Rotor 3', padx=10, pady=5, borderwidth=0, background='white')
rotor3lab.grid(row=0, column=2)

#scales_choose_position
var1 = DoubleVar()
scale = Scale(frame1, from_=0, to=25, variable = var1, cursor='dot', showvalue=0, command=update1, length= 100, background='white')
scale.grid(row=1, column=0, padx=60, pady=10)
var2 = DoubleVar()
scale = Scale(frame1, from_=0, to=25, variable = var2, cursor='dot', showvalue=0, command=update2, length= 100, background='white')
scale.grid(row=1, column=1, padx=60, pady=10)
var3 = DoubleVar()
scale = Scale(frame1, from_=0, to=25, variable = var3, cursor='dot', showvalue=0, command=update3, length= 100, background='white')
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

    if var4list[5] == '1':  # si rotor en position 1 est le 1
        rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    elif var4list[5] == '2':  # si rotor en position 1 est le 2
        rotor1 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    elif var4list[5] == '3':  # si rotor en position 1 est le 3
        rotor1 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
    if var5list[5] == '1':  # si rotor en position 2 est le 1
        rotor2 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    elif var5list[5] == '2':  # si rotor en position 2 est le 2
        rotor2 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    elif var5list[5] == '3':  # si rotor en position 2 est le 3
        rotor2 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
    if var6list[5] == '1':  # si rotor en position 3 est le 1
        rotor3 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
    elif var6list[5] == '2':  # si rotor en position 3 est le 2
        rotor3 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
    elif var6list[5] == '3':  # si rotor en position 3 est le 3
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

#button_to_(de)code
b1 = Button(fenetre, text="(de)code", width=10, command=code, background='white')
b1.pack()

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
