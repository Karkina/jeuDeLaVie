from tkinter import *
import random
from functools import partial
import tkinter.filedialog
from tkinter import colorchooser
from typing import ValuesView
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
import copy

def liste(hauteur, largeur):
    my_list=list(range(largeur))
    for i in my_list:
        my_list[i]=list(range(hauteur))
        for j in range(hauteur):
            my_list[i][j]=0
    return my_list

def randomCells(lifePop):
    global hauteur
    global largeur
    global button_reset

    reset()
    for i in range(lifePop):
        x = random.randint(0,largeur-1)
        y = random.randint(0,hauteur-1)
        createCells(x,y)
    
    button_reset.place(relx=0.1,rely=0.65,anchor=CENTER)

def createCells(x,y):
    global color_case
    global my_canvas

    l[x][y] = 1
    my_canvas.delete(r[x][y])
    r[x][y] = my_canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10,outline='pink',fill=color_case)

def reset():
    global m
    global stopBool
    global hauteur
    global largeur
    global count_step
    global label_step
    global button_reset
    global button_start
    global button_stop

    stopBool=0
    m=0
    count_step=0
    label_step.configure(text=count_step)

    for i in range(largeur):
        for j in range(hauteur):
            detruire(i,j)
    
    if button_reset.winfo_exists():
        button_reset.place_forget()
    if button_continuer.winfo_exists():
        button_continuer.place_forget()
    if button_stop.winfo_exists():
        button_stop.place_forget()
    
    button_start.place(relx=0.1,rely=0.50,anchor=CENTER)

    label_hauteur.place(relx=0.90, rely=0.37,anchor=CENTER)
    caseHauteur.place(relx=0.90,rely=0.40,anchor=CENTER)
    label_largeur.place(relx=0.90, rely=0.43,anchor=CENTER)
    caseLargeur.place(relx=0.90,rely=0.46,anchor=CENTER)
    button_taille.place(relx=0.90, rely=0.50, anchor=CENTER)
    

def listeInit(): 
    global lInit
    global l
    print('test')
    lInit = copy.deepcopy(l)
def detruire(x,y):
    global my_canvas

    l[x][y] = 0
    my_canvas.delete(r[x][y])
    r[x][y] = my_canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10,outline='pink',fill='white')

def start():
    global m
    
    if stopBool==1:
        return
    else:
        m=1
        print('test')
        listeInit()
        continuer()
    if m==0:
        m=1
        continuer()

def continuer():
    global m
    global stopBool
    global button_start
    global button_etapes
    global population
    global button_continuer
    global button_population
    global button_reset
    global label_hauteur
    global label_largeur
    global caseHauteur
    global caseLargeur
    global button_taille
    global button_stop
    global speed_values
    global button_speed

    if m==1:

        if button_start.winfo_exists():
            button_start.place_forget()
        if button_etapes.winfo_exists():
            button_etapes.place_forget()
        if population.winfo_exists():
            population.place_forget()
        if button_population.winfo_exists():
            button_population.place_forget()
        if button_continuer.winfo_exists():
            button_continuer.place_forget()
        if button_reset.winfo_exists():
            button_reset.place_forget()
        if label_hauteur.winfo_exists():
            label_hauteur.place_forget()
        if label_largeur.winfo_exists():
            label_largeur.place_forget()
        if caseHauteur.winfo_exists():
            caseHauteur.place_forget()
        if caseLargeur.winfo_exists():
            caseLargeur.place_forget()
        if button_taille.winfo_exists():
            button_taille.place_forget()
        
        button_stop.place(relx=0.1,rely=0.55,anchor=CENTER)
        speed_values.place(relx=0.38,rely=0.85,anchor=CENTER)
        button_speed.place(relx=0.38, rely=0.88,anchor=CENTER)


        comptage()
        f.after(speed,continuer)
        
    if stopBool==1:

        if button_stop.winfo_exists():
            button_stop.place_forget()
        if button_speed.winfo_exists():
            button_speed.place_forget()
        if speed_values.winfo_exists():
            speed_values.place_forget()
        
        population.place(relx=0.38,rely=0.85,anchor=CENTER)
        button_population.place(relx=0.38,rely=0.88,anchor=CENTER)
        button_etapes.place(relx=0.1,rely=0.70,anchor=CENTER)
        button_continuer.place(relx=0.1, rely=0.60,anchor=CENTER)
        button_reset.place(relx=0.1,rely=0.65,anchor=CENTER)
        label_hauteur.place(relx=0.90, rely=0.37,anchor=CENTER)
        caseHauteur.place(relx=0.90,rely=0.40,anchor=CENTER)
        label_largeur.place(relx=0.90, rely=0.43,anchor=CENTER)
        caseLargeur.place(relx=0.90,rely=0.46,anchor=CENTER)
        button_taille.place(relx=0.90, rely=0.50, anchor=CENTER)

        stopBool=0
        m=1

def stop():
    global m
    global stopBool
    stopBool =1
    m=0
    
def comptage_nor():
    global largeur
    global hauteur

    if modeGrille == 0 :
        for i in range(largeur):
            for j in range(hauteur):
                #les Coins
                if i==0 and j==0:
                    compt = l[i][j+1]+l[i+1][j]+l[i+1][j+1]
                    c[i][j] = compt
                elif i==0 and j==hauteur-1:
                    compt = l[i][j-1]+l[i+1][j-1]+l[i+1][j]
                    c[i][j] = compt
                elif i==largeur-1 and j==0 :
                    compt = l[i-1][j]+l[i][j+1]+l[i-1][j+1]
                    c[i][j] = compt
                elif i==largeur-1 and j==hauteur-1:
                    compt = l[i][j-1]+l[i-1][j-1]+l[i-1][j]
                    c[i][j] = compt
                #les bord
                elif i==largeur-1 and j>0:
                    compt = l[i][j-1]+l[i-1][j-1] + l[i-1][j]+l[i-1][j+1]+l[i][j+1]
                    c[i][j] = compt
                elif i==0 and j>0:
                    compt = l[i][j-1]+l[i+1][j-1] + l[i+1][j]+l[i+1][j+1]+l[i][j+1]
                    c[i][j] = compt
                elif j==0 and i>0:
                    compt = l[i-1][j] + l[i+1][j]+l[i-1][j+1]+l[i][j+1]+l[i+1][j+1]
                    c[i][j] = compt
                elif j==hauteur-1 and i>0:
                    compt = l[i][j-1] + l[i+1][j] + l[i-1][j] + l[i-1][j-1]+l[i+1][j-1]
                    c[i][j] = compt
                #au milieu
                else:
                    compt = l[i][j+1]+l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i-1][j+1]+l[i+1][j-1]+l[i+1][j]+l[i+1][j+1]
                    c[i][j] = compt
    else :
        for i in range(largeur):
            for j in range(hauteur):
                #les Coins
                if i==0 and j==0:
                    compt = l[i][j+1]+l[i+1][j]+l[i+1][j+1]+l[largeur-1][j]+l[largeur-1][j+1]+l[i][hauteur-1]+l[i+1][hauteur-1]+l[largeur-1][hauteur-1]
                    c[i][j] = compt
                elif i==0 and j==hauteur-1:
                    compt = l[i][j-1]+l[i+1][j-1]+l[i+1][j]+l[i][0]+l[i+1][0]+l[largeur-1][j]+l[largeur-1][j-1]+l[largeur-1][0]
                    c[i][j] = compt
                elif i==largeur-1 and j==0 :
                    compt = l[i-1][j]+l[i][j+1]+l[i-1][j+1]+l[0][j]+l[0][j+1]+l[i][hauteur-1]+l[i-1][hauteur-1]+l[0][hauteur-1]
                    c[i][j] = compt
                elif i==largeur-1 and j==hauteur-1:
                    compt = l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i][0]+l[i-1][0]+l[0][j]+l[0][j-1]+l[0][0]
                    c[i][j] = compt
                #les bord
                elif i==largeur-1 and j>0:
                    compt = l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i-1][j+1]+l[i][j+1]+l[0][j-1]+l[0][j]+l[0][j+1]
                    c[i][j] = compt
                elif i==0 and j>0:
                    compt = l[i][j-1]+l[i+1][j-1]+l[i+1][j]+l[i+1][j+1]+l[i][j+1]+l[largeur-1][j-1]+l[largeur-1][j]+l[largeur-1][j+1]
                    c[i][j] = compt
                elif j==0 and i>0:
                    compt = l[i-1][j]+l[i+1][j]+l[i-1][j+1]+l[i][j+1]+l[i+1][j+1]+l[i-1][hauteur-1]+l[i][hauteur-1]+l[i+1][hauteur-1]
                    c[i][j] = compt
                elif j==hauteur-1 and i>0:
                    compt = l[i][j-1]+l[i+1][j]+l[i-1][j]+l[i-1][j-1]+l[i+1][j-1]+l[i-1][0]+l[i][0]+l[i+1][0]
                    c[i][j] = compt
                #au milieu
                else:
                    compt = l[i][j+1]+l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i-1][j+1]+l[i+1][j-1]+l[i+1][j]+l[i+1][j+1]
                    c[i][j] = compt


def comptage():
    global count_step
    global label_step
    global modeGrille
    global largeur
    global hauteur

    if modeGrille == 0 :
        for i in range(largeur):
            for j in range(hauteur):
                #les Coins
                if i==0 and j==0:
                    compt = l[i][j+1]+l[i+1][j]+l[i+1][j+1]
                    c[i][j] = compt
                elif i==0 and j==hauteur-1:
                    compt = l[i][j-1]+l[i+1][j-1]+l[i+1][j]
                    c[i][j] = compt
                elif i==largeur-1 and j==0 :
                    compt = l[i-1][j]+l[i][j+1]+l[i-1][j+1]
                    c[i][j] = compt
                elif i==largeur-1 and j==hauteur-1:
                    compt = l[i][j-1]+l[i-1][j-1]+l[i-1][j]
                    c[i][j] = compt
                #les bord
                elif i==largeur-1 and j>0:
                    compt = l[i][j-1]+l[i-1][j-1] + l[i-1][j]+l[i-1][j+1]+l[i][j+1]
                    c[i][j] = compt
                elif i==0 and j>0:
                    compt = l[i][j-1]+l[i+1][j-1] + l[i+1][j]+l[i+1][j+1]+l[i][j+1]
                    c[i][j] = compt
                elif j==0 and i>0:
                    compt = l[i-1][j] + l[i+1][j]+l[i-1][j+1]+l[i][j+1]+l[i+1][j+1]
                    c[i][j] = compt
                elif j==hauteur-1 and i>0:
                    compt = l[i][j-1] + l[i+1][j] + l[i-1][j] + l[i-1][j-1]+l[i+1][j-1]
                    c[i][j] = compt
                #au milieu
                else:
                    compt = l[i][j+1]+l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i-1][j+1]+l[i+1][j-1]+l[i+1][j]+l[i+1][j+1]
                    c[i][j] = compt
    else :
        for i in range(largeur):
            for j in range(hauteur):
                #les Coins
                if i==0 and j==0:
                    compt = l[i][j+1]+l[i+1][j]+l[i+1][j+1]+l[largeur-1][j]+l[largeur-1][j+1]+l[i][hauteur-1]+l[i+1][hauteur-1]+l[largeur-1][hauteur-1]
                    c[i][j] = compt
                elif i==0 and j==hauteur-1:
                    compt = l[i][j-1]+l[i+1][j-1]+l[i+1][j]+l[i][0]+l[i+1][0]+l[largeur-1][j]+l[largeur-1][j-1]+l[largeur-1][0]
                    c[i][j] = compt
                elif i==largeur-1 and j==0 :
                    compt = l[i-1][j]+l[i][j+1]+l[i-1][j+1]+l[0][j]+l[0][j+1]+l[i][hauteur-1]+l[i-1][hauteur-1]+l[0][hauteur-1]
                    c[i][j] = compt
                elif i==largeur-1 and j==hauteur-1:
                    compt = l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i][0]+l[i-1][0]+l[0][j]+l[0][j-1]+l[0][0]
                    c[i][j] = compt
                #les bord
                elif i==largeur-1 and j>0:
                    compt = l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i-1][j+1]+l[i][j+1]+l[0][j-1]+l[0][j]+l[0][j+1]
                    c[i][j] = compt
                elif i==0 and j>0:
                    compt = l[i][j-1]+l[i+1][j-1]+l[i+1][j]+l[i+1][j+1]+l[i][j+1]+l[largeur-1][j-1]+l[largeur-1][j]+l[largeur-1][j+1]
                    c[i][j] = compt
                elif j==0 and i>0:
                    compt = l[i-1][j]+l[i+1][j]+l[i-1][j+1]+l[i][j+1]+l[i+1][j+1]+l[i-1][hauteur-1]+l[i][hauteur-1]+l[i+1][hauteur-1]
                    c[i][j] = compt
                elif j==hauteur-1 and i>0:
                    compt = l[i][j-1]+l[i+1][j]+l[i-1][j]+l[i-1][j-1]+l[i+1][j-1]+l[i-1][0]+l[i][0]+l[i+1][0]
                    c[i][j] = compt
                #au milieu
                else:
                    compt = l[i][j+1]+l[i][j-1]+l[i-1][j-1]+l[i-1][j]+l[i-1][j+1]+l[i+1][j-1]+l[i+1][j]+l[i+1][j+1]
                    c[i][j] = compt

    regleJeu()
    count_step+=1
    label_step.configure(text=count_step)

def regleJeu():
    global largeur
    global hauteur

    for i in range(largeur):
        for j in range(hauteur):
            if (l[i][j]==1 and c[i][j]<2) or (c[i][j]>3 and l[i][j]==1):
                detruire(i,j)
            elif l[i][j]==0 and c[i][j]==3:
                createCells(i,j)

def sauvegarder():
    global hauteur
    global largeur

    test = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if test is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    
    fichier = open(test.name,"w")
    test.close()

    fichier.write("%d\n" %hauteur)
    fichier.write("%d\n" %(largeur))

    for i in range(hauteur):
        for j in range(largeur):
             fichier.write("%d " %(l[j][i]))
        fichier.write("\n")
             
    fichier.close()
    
def InitSave():
    global hauteur
    global largeur
    global lInit
    test = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if test is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    
    fichier = open(test.name,"w")
    test.close()

    fichier.write("%d\n" %hauteur)
    fichier.write("%d\n" %(largeur))
    print("\n")
    print(lInit)
    for i in range(hauteur):
        for j in range(largeur):
             fichier.write("%d " %(lInit[j][i]))
        fichier.write("\n")
             
    fichier.close()
def openGame():
    global l,c
    global hauteur
    global largeur


    filename = tkinter.filedialog.askopenfilename()
    
    'On ouvre le fichier en lecture'
    fichier = open(filename,'r')
    hauteur =int(fichier.readline())
    largeur=int(fichier.readline())
    
    createWindow(hauteur, largeur)
    reset()
    cmp=0
    while cmp!=hauteur:
        'Lecture ligne par ligne'
        line =fichier.readline()
        if not line:
            break
        data = line.split()
        for i in range(largeur):
            l[i][cmp]=int(data[i])

        cmp+=1
    #comptage_nor()
    
    for i in range(largeur):
        for j in range(hauteur):
            if l[i][j]==1:
                createCells(i,j)
        


def rajouter(event):
    x = event.x//10
    y = event.y//10
    createCells(x,y) 

def enlever(event):
    x = event.x//10
    y = event.y//10
    detruire(x,y)      

def close_escape(event=None):
    global f
    f.destroy()    
    
def setSpeed(speed_val):
    global speed
    speed=speed_val

def init_taille ():
    global hauteur
    global largeur
    global caseHauteur
    global caseLargeur
    global button_reset
    global button_continuer

    hauteur=int(caseHauteur.get())
    largeur=int(caseLargeur.get())

    createWindow(hauteur, largeur)
    if button_reset.winfo_exists():
        button_reset.place_forget()
    if button_continuer.winfo_exists():
        button_continuer.place_forget()

def changer_mode():
    global modeGrille
    global label_mode

    if modeGrille == 0 :
        modeGrille=1
        label_mode.configure(text='Torique')
    else:
        modeGrille=0
        label_mode.configure(text='Normal')

def exemple1():
    global l
    global hauteur
    global largeur

    hauteur=20
    largeur=20
    createWindow(hauteur,largeur)
    reset()

    createCells(0,1)
    createCells(1,2)
    createCells(2,0)
    createCells(2,1)
    createCells(2,2)

    createCells(5,1)
    createCells(6,2)
    createCells(7,0)
    createCells(7,1)
    createCells(7,2)

    createCells(10,1)
    createCells(11,2)
    createCells(12,0)
    createCells(12,1)
    createCells(12,2)

    createCells(15,1)
    createCells(16,2)
    createCells(17,0)
    createCells(17,1)
    createCells(17,2)

    createCells(1,6)
    createCells(2,7)
    createCells(3,5)
    createCells(3,6)
    createCells(3,7)

    createCells(6,6)
    createCells(7,7)
    createCells(8,5)
    createCells(8,6)
    createCells(8,7)

    createCells(11,6)
    createCells(12,7)
    createCells(13,5)
    createCells(13,6)
    createCells(13,7)

    createCells(16,6)
    createCells(17,7)
    createCells(18,5)
    createCells(18,6)
    createCells(18,7)

    createCells(2,11)
    createCells(3,12)
    createCells(4,10)
    createCells(4,11)
    createCells(4,12)
    createCells(7,11)
    createCells(8,12)
    createCells(9,10)
    createCells(9,11)
    createCells(9,12)
    createCells(12,11)
    createCells(13,12)
    createCells(14,10)
    createCells(14,11)
    createCells(14,12)
    createCells(17,11)
    createCells(18,12)
    createCells(19,10)
    createCells(19,11)
    createCells(19,12)
    createCells(0,15)
    createCells(0,16)
    createCells(0,17)
    createCells(3,16)
    createCells(4,17)
    createCells(5,15)
    createCells(5,16)
    createCells(5,17)
    createCells(8,16)
    createCells(9,17)
    createCells(10,15)
    createCells(10,16)
    createCells(10,17)
    createCells(13,16)
    createCells(14,17)
    createCells(15,15)
    createCells(15,16)
    createCells(15,17)
    createCells(18,16)
    createCells(19,17)

def exemple2():
    global l
    global hauteur
    global largeur

    hauteur=10
    largeur=35
    createWindow(hauteur,largeur)
    reset()

    createCells(0,0)
    createCells(0,1)
    createCells(0,2)
    createCells(0,3)
    createCells(0,4)
    createCells(0,5)
    createCells(0,6)
    createCells(0,7)
    createCells(0,8)
    createCells(0,9)

def exemple3():
    global l
    global hauteur
    global largeur

    hauteur=16
    largeur=20
    createWindow(hauteur,largeur)
    reset()

    createCells(0,1)
    createCells(1,1)
    createCells(2,1)

    createCells(4,1)
    createCells(5,1)
    createCells(6,1)

    createCells(8,1)
    createCells(9,1)
    createCells(10,1)

    createCells(12,1)
    createCells(13,1)
    createCells(14,1)

    createCells(16,1)
    createCells(17,1)
    createCells(18,1)

    createCells(1,5)
    createCells(2,5)
    createCells(3,5)

    createCells(5,5)
    createCells(6,5)
    createCells(7,5)

    createCells(9,5)
    createCells(10,5)
    createCells(11,5)

    createCells(13,5)
    createCells(14,5)
    createCells(15,5)

    createCells(17,5)
    createCells(18,5)
    createCells(19,5)

    createCells(0,9)
    createCells(1,9)
    createCells(2,9)

    createCells(4,9)
    createCells(5,9)
    createCells(6,9)

    createCells(8,9)
    createCells(9,9)
    createCells(10,9)

    createCells(12,9)
    createCells(13,9)
    createCells(14,9)

    createCells(16,9)
    createCells(17,9)
    createCells(18,9)

    createCells(1,13)
    createCells(2,13)
    createCells(3,13)

    createCells(5,13)
    createCells(6,13)
    createCells(7,13)

    createCells(9,13)
    createCells(10,13)
    createCells(11,13)

    createCells(13,13)
    createCells(14,13)
    createCells(15,13)

    createCells(17,13)
    createCells(18,13)
    createCells(19,13)

def petite():
    global hauteur
    global largeur

    largeur=15
    hauteur=15
    createWindow(hauteur,largeur)
    reset()

def moyenne():
    global hauteur
    global largeur

    largeur=25
    hauteur=25
    createWindow(hauteur,largeur)
    reset()

def grande():
    global hauteur
    global largeur

    largeur=50
    hauteur=50
    createWindow(hauteur,largeur)
    reset()
   
def color_back():
    global f
    global background_label
    color_code = colorchooser.askcolor(title ="Choose color")
    background_label.place_forget()
    f.configure(bg=color_code[1])

def color_Case():
    global color_case
    color_code = colorchooser.askcolor(title ="Choose color")
    color_case = color_code[1]

#def par_defaut():
#    global background_label
#    global color_case
#    global f
#    global image
#    f.configure(bg=image)
#    color_case = 'pink'

def createWindow(Hauteur, Largeur):
    global hauteur
    global largeur
    global my_canvas
    global f
    global button_start #start
    global button_etapes #pas à pas
    global population #population
    global button_population #population.val
    global l,r,c,lInit
    global label_step
    global count_step
    global speed
    global speed_values
    global button_speed
    global button_stop
    global button_continuer
    global button_reset
    
    hauteur=Hauteur
    largeur=Largeur
    lInit = liste(hauteur,largeur)
    l = liste(hauteur,largeur)
    r = liste(hauteur,largeur)
    c = liste(hauteur,largeur)

    count_step=0
    label_step.configure(text=count_step)
    speed=100

    if my_canvas.winfo_exists():
        my_canvas.place_forget()

    my_canvas = Canvas(f,width=Largeur*10,height=Hauteur*10,background="white")
    for i in range(Largeur):
        for j in range(hauteur):
            lo=i*10
            ha=j*10
            r[i][j] = my_canvas.create_rectangle(lo,ha,lo+10,ha+10,outline='pink',fill='white')      

    my_canvas.bind("<Button-1>",rajouter) 
    my_canvas.bind("<Button-3>",enlever)

    my_canvas.place(relx=0.5,rely=0.38,anchor=CENTER) 
    
    population.place(relx=0.38,rely=0.85,anchor=CENTER)
    
    button_population.place(relx=0.38,rely=0.88,anchor=CENTER)
    
    button_start.place(relx=0.1,rely=0.50,anchor=CENTER)

    button_etapes.place(relx=0.1,rely=0.70,anchor=CENTER)

    label_step.place(relx=0.1, rely=0.75,anchor=CENTER)


f=Tk()  

image = Image.open(r"cell.jpg")
background_image = ImageTk.PhotoImage(image)

background_label = Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

modeGrille=1
color_case='pink'
stopBool=0
largeur=0
hauteur=0
m=1
pop=0
widthButton=18
taille_canvas =40
count_step=0
speed=100
#f.attributes('-fullscreen',True)
f.bind("<Escape>", close_escape)
f.title('Jeu de la Vie')
f.geometry("800x800")
f.configure(bg='lightblue')
menubar = Menu(f) 

menu1 = Menu(menubar,tearoff=0)
menu2 = Menu(menubar,tearoff=0)
menu3 = Menu(menubar,tearoff=0)
menu4 = Menu(menubar,tearoff=0)

menu1.add_command(label="Save", command=sauvegarder) 
menu1.add_command(label="Save Initial", command=InitSave)
menu1.add_command(label="Open", command=openGame)
menu1.add_separator()
menu1.add_command(label="Quitter", command=close_escape) 

menu2.add_command(label="Non-stop", command=exemple1)
menu2.add_command(label="Code-Barre", command=exemple2)
menu2.add_command(label="Plus/moins l'infini", command=exemple3)

menu3.add_command(label="Petite", command=petite)
menu3.add_command(label="Moyenne", command=moyenne)
menu3.add_command(label="Grande", command=grande)

menu4.add_command(label="Background", command=color_back)
menu4.add_command(label="Cases", command=color_Case)
#menu4.add_separator()
#menu4.add_command(label="Par défaut", command=par_defaut)

menubar.add_cascade(label="Configuration", menu=menu1)
menubar.add_cascade(label="Exemples", menu=menu2)
menubar.add_cascade(label="taille", menu=menu3)
menubar.add_cascade(label="Color", menu=menu4)

f.config(menu=menubar)  

lInit = liste(0,0)
l = liste(0,0)
r = liste(0,0)
c = liste(0,0)

my_canvas = Canvas(f,width=800,height=800,background="white")
button_start = Button(f,text="start",command=start,width=widthButton,bg='DarkOrange1',fg='white')
population=Spinbox(f,values=(20,40,80,160,300,400,500,600))
button_population = Button(f,text="La population de départ",command= lambda : randomCells(int(population.get())),width=widthButton,bg='slate blue',fg='white')    
speed_values=Spinbox(f,values=(100,250,500,1000,2000))
button_speed = Button(f,text="Applique la vitesse",command= lambda : setSpeed(int(speed_values.get())),width=widthButton,bg='slate blue',fg='white')
button_stop = Button(f,text="stop",command=stop,width=widthButton,bg='DarkOrange1',fg='white')
button_continuer = Button(f,text="Continuer",command=continuer,width=widthButton,bg='DarkOrange1',fg='white')
button_reset = Button(f,text="Reset",command=reset,width=widthButton,bg='DarkOrange1',fg='white')
button_etapes = Button(f, text ='Évolution étape/étape', command =comptage,width=widthButton,bg='slate blue',fg='white')
button_mode=Button(f, text='Changer mode', command=changer_mode, width=widthButton, bg='DarkOrange1',fg='white')
label_step = Label(f,bg='white',text=0,width=20)
label_hauteur= Label(f,bg='slate blue',fg='white',text='Hauteur',width=20)
label_largeur= Label(f,bg='slate blue',fg='white',text='Largeur',width=20)
label_mode=Label(f, text='Torique', bg='white' ,width=20)
caseHauteur=Spinbox(f, from_=10, to=50, state='readonly')
caseLargeur=Spinbox(f, from_=10, to=50, state='readonly')
button_taille=Button(f, text="initialiser taille",command=init_taille,bg='DarkOrange1',fg='white')


label_hauteur.place(relx=0.90, rely=0.37,anchor=CENTER)
caseHauteur.place(relx=0.90,rely=0.40,anchor=CENTER)
label_largeur.place(relx=0.90, rely=0.43,anchor=CENTER)
caseLargeur.place(relx=0.90,rely=0.46,anchor=CENTER)
button_taille.place(relx=0.90, rely=0.50, anchor=CENTER)

label_mode.place(relx=0.90, rely=0.80, anchor=CENTER)
button_mode.place(relx=0.90, rely=0.85, anchor=CENTER)


f.mainloop()