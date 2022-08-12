from PIL import Image, ImageTk
from logicModule import *
from tkinter import CENTER, messagebox
import tkinter as tk

# --------------------------------------------------------
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MainApplication, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.seleccion=tk.IntVar()
        self.primary()

    # ------------------------------
    # Main menu interface
    # ------------------------------
    def primary(self):
        initializeAll()
        self.miFramePri=tk.Frame(root, width=800, height=500, background="#16A085")
        self.miFramePri.pack()
        self.miFramePri.config(cursor='hand2')
    
        selecCat=tk.Label(self.miFramePri, text="SELECCIONE LA CATEGORIA", font=("Courier",20), background="#16A085", foreground="white")
        selecCat.place(relx = 0.5, rely = 0.05, anchor = 'center')

        ButtonsCategories(self)
        bJugar=tk.Button(self.miFramePri, text = "Jugar", background = "#27AE60", height=2, width=5, font=("Courier",17), command=lambda:toPlay(self))
        bJugar.place(x=300, y=430)

        bSalir=tk.Button(self.miFramePri, text = "Salir", background = "#E74C3C", height=2, width=5, font=("Courier",17), command=self.quit)
        bSalir.place(x=420, y=430)

    # ------------------------------
    # Game menu interface
    # ------------------------------
    def secondary(self):
        global vidas
        global pal
        global resulParcial
        self.miFramePri.destroy()
        
        pal=categoryWord(self.seleccion.get()).upper()
        resulParcial=replaceUnderscore(pal)

        self.miFrameSec=tk.Frame(root, width=800, height=500, background="#16A085")
        self.miFrameSec.pack()
        self.miFrameSec.config(cursor='hand2')

        self.miFrameSecIzq=tk.Frame(self.miFrameSec, width=400, height=500, background="#16A085")
        self.miFrameSecIzq.pack(side="left")
        
        self.miFrameSecDer=tk.Frame(self.miFrameSec, width=400, height=500, background="#16A085")
        self.miFrameSecDer.pack(side="right")

        textoIngLet=tk.Label(self.miFrameSecDer, text="PRESIONE UNA LETRA", font=("Courier",20), background="#16A085")
        textoIngLet.place(x=50, y=25)
        
        textoAdivPab=tk.Label(self.miFrameSecDer, text="PALABRA A ADIVINAR:", font=("Courier",20), background="#16A085")
        textoAdivPab.place(x=50, y=320)

        interfaceLetras(self)

        selectImageLife(self)

        palParcial=tk.Label(self.miFrameSecDer, text=resulParcial, font=("Arial Black",20), background="#16A085")
        palParcial.place(relx = 0.5, rely = 0.8, anchor = 'center')

# ------------------------------------------------------------
'''
Initialize the values ​​to be able to start a new game.
'''
def initializeAll():
    global vidas
    global listLetrasIng
    global pal
    global resulParcial
    vidas=7
    listLetrasIng=[]
    pal=''
    resulParcial=[]
# ------------------------------------------------------------
'''
Method to be able to start the game and verify if I select a category.

Parameters:
- self: root interface class.
'''
def toPlay(self):
    if self.seleccion.get() == 0:
        messagebox.showinfo(message="Debes seleccionar la categoria", title="Atención!")
    else:
        self.secondary()
# ------------------------------------------------------------
'''
Method used each time a letter is pressed, call the different functions
to assess the state of the game.

Parameters:
- btn: button that was pressed to assign a color to it.
- lyrics: letter that is pressed by the user when playing.
'''
def evaluateLetter(self, btn, lyrics):
    global vidas
    global listLetrasIng
    global pal
    global resulParcial
    if vidas>0:
        if listLettersEntered(lyrics, listLetrasIng):
            btn.configure(bg="green")
            
            if thereIsCharacterInWord(lyrics, pal):
                resulParcial=replaceLetter(lyrics, pal, resulParcial)
                
                palParcial=tk.Label(self.miFrameSecDer, text=resulParcial, font=("Arial Black",20), background="#16A085")
                palParcial.place(relx = 0.5, rely = 0.8, anchor = 'center')
            else:
                btn.configure(bg="red")
                vidas-=1
        else:
            messagebox.showinfo(message="Letra ya ingresada", title="Atención!")
    if verifyWinner(resulParcial):
        imgVictoria(self)
        messagebox.showinfo(message="Ganaste", title="Felicitaciones")
        bVolverJugar=tk.Button(self.miFrameSecDer, text = "Volver a jugar", background = "#27AE60", height=2, width=12, font=("Courier",10), command=lambda:volverJugar(self))
        bVolverJugar.place(relx = 0.3, rely = 0.9, anchor = 'center')
        bSalir=tk.Button(self.miFrameSecDer, text = "Salir", background = "#E74C3C", height=2, width=5, font=("Courier",10), command=self.quit)
        bSalir.place(relx = 0.7, rely = 0.9, anchor = 'center')
    elif vidas==0:
        imgVida0(self)
        messagebox.showinfo(message="Vuelva a intentarlo \n"+"Palabra correcta:\n"+pal, title="Perdiste")
        bVolverJugar=tk.Button(self.miFrameSecDer, text = "Volver a jugar", background = "#27AE60", height=2, width=12, font=("Courier",10), command=lambda:volverJugar(self))
        bVolverJugar.place(relx = 0.3, rely = 0.9, anchor = 'center')
        bSalir=tk.Button(self.miFrameSecDer, text = "Salir", background = "#E74C3C", height=2, width=5, font=("Courier",10), command=self.quit)
        bSalir.place(relx = 0.7, rely = 0.9, anchor = 'center')
    else:
        selectImageLife(self)

# --------------------------------------------------------
'''
Method to go to the main menu.
'''
def volverJugar(self):
    self.miFrameSec.destroy()
    self.primary()
# --------------------------------------------------------
'''
Button interface method with their respective functions.
'''
def ButtonsCategories(self):
    bFrutas=tk.Radiobutton(self.miFramePri, text = "Frutas", variable=self.seleccion, value = 1, indicator = 0, background = "#F8C471", height=6, width=10, font=("Courier",20))
    bFrutas.place(x=120, y=60)

    bVerduras=tk.Radiobutton(self.miFramePri, text = "Verduras", variable=self.seleccion, value = 2, indicator = 0, background = "#F8C471", height=6, width=10, font=("Courier",20))
    bVerduras.place(x=320, y=60)

    bProfesiones=tk.Radiobutton(self.miFramePri, text = "Oficios", variable=self.seleccion, value = 3, indicator = 0, background = "#F8C471", height=6, width=10, font=("Courier",20))
    bProfesiones.place(x=520, y=60)

    bColores=tk.Radiobutton(self.miFramePri, text = "Colores", variable=self.seleccion, value = 4, indicator = 0, background = "#F8C471", height=6, width=10, font=("Courier",20))
    bColores.place(x=120, y=240)

    bAnimales=tk.Radiobutton(self.miFramePri, text = "Animales", variable=self.seleccion, value = 5, indicator = 0, background = "#F8C471", height=6, width=10, font=("Courier",20))
    bAnimales.place(x=320, y=240)

    bDeportes=tk.Radiobutton(self.miFramePri, text = "Deportes", variable=self.seleccion, value = 6, indicator = 0, background = "#F8C471", height=6, width=10, font=("Courier",20))
    bDeportes.place(x=520, y=240)

# --------------------------------------------------------
'''
Button interface method with their respective functions.
'''
def interfaceLetras(self):
    # Line 1
    letraA=tk.Button(self.miFrameSecDer, text="A", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraA, "A"))
    letraA.place(x=30, y=80)

    letraB=tk.Button(self.miFrameSecDer, text="B", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraB, "B"))
    letraB.place(x=80, y=80)

    letraC=tk.Button(self.miFrameSecDer, text="C", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraC, "C"))
    letraC.place(x=130, y=80)

    letraD=tk.Button(self.miFrameSecDer, text="D", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraD, "D"))
    letraD.place(x=180, y=80)

    letraE=tk.Button(self.miFrameSecDer, text="E", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraE, "E"))
    letraE.place(x=230, y=80)

    letraF=tk.Button(self.miFrameSecDer, text="F", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraF, "F"))
    letraF.place(x=280, y=80)

    letraG=tk.Button(self.miFrameSecDer, text="G", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraG, "G"))
    letraG.place(x=330, y=80)

    # Line 2
    letraH=tk.Button(self.miFrameSecDer, text="H", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraH, "H"))
    letraH.place(x=30, y=130)

    letraI=tk.Button(self.miFrameSecDer, text="I", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraI, "I"))
    letraI.place(x=80, y=130)

    letraJ=tk.Button(self.miFrameSecDer, text="J", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraJ, "J"))
    letraJ.place(x=130, y=130)

    letraK=tk.Button(self.miFrameSecDer, text="K", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraK, "K"))
    letraK.place(x=180, y=130)

    letraL=tk.Button(self.miFrameSecDer, text="L", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraL, "L"))
    letraL.place(x=230, y=130)

    letraM=tk.Button(self.miFrameSecDer, text="M", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraM, "M"))
    letraM.place(x=280, y=130)

    letraN=tk.Button(self.miFrameSecDer, text="N", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraN, "N"))
    letraN.place(x=330, y=130)

    # Line 3
    letraÑ=tk.Button(self.miFrameSecDer, text="Ñ", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraÑ, "Ñ"))
    letraÑ.place(x=30, y=180)

    letraO=tk.Button(self.miFrameSecDer, text="O", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraO, "O"))
    letraO.place(x=80, y=180)

    letraP=tk.Button(self.miFrameSecDer, text="P", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraP, "P"))
    letraP.place(x=130, y=180)

    letraQ=tk.Button(self.miFrameSecDer, text="Q", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraQ, "Q"))
    letraQ.place(x=180, y=180)

    letraR=tk.Button(self.miFrameSecDer, text="R", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraR, "R"))
    letraR.place(x=230, y=180)

    letraS=tk.Button(self.miFrameSecDer, text="S", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraS, "S"))
    letraS.place(x=280, y=180)

    letraT=tk.Button(self.miFrameSecDer, text="T", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraT, "T"))
    letraT.place(x=330, y=180)

    # Line 4
    letraU=tk.Button(self.miFrameSecDer, text="U", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraU, "U"))
    letraU.place(x=30, y=230)

    letraV=tk.Button(self.miFrameSecDer, text="V", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraV, "V"))
    letraV.place(x=80, y=230)

    letraW=tk.Button(self.miFrameSecDer, text="W", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraW, "W"))
    letraW.place(x=130, y=230)

    letraX=tk.Button(self.miFrameSecDer, text="X", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraX, "X"))
    letraX.place(x=180, y=230)

    letraY=tk.Button(self.miFrameSecDer, text="Y", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraY, "Y"))
    letraY.place(x=230, y=230)

    letraZ=tk.Button(self.miFrameSecDer, text="Z", font=("Arial",20), border=1, width=1, command=lambda:evaluateLetter(self, letraZ, "Z"))
    letraZ.place(x=280, y=230)
# --------------------------------------------------------
'''
Method to select the corresponding image of the game state.
'''
def selectImageLife(self):
    global vidas
    if vidas==7:
        imgVida7(self)
    if vidas==6:
        imgVida6(self)
    if vidas==5:
        imgVida5(self)
    if vidas==4:
        imgVida4(self)
    if vidas==3:
        imgVida3(self)
    if vidas==2:
        imgVida2(self)
    if vidas==1:
        imgVida1(self)
    if vidas==0:
        imgVida0(self)
    if vidas==8:
        imgVictoria(self)
    
def imgVida7(self):
    imgVida7 = Image.open("./images/Vida7.jpg")
    imgVida7 = imgVida7.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida7)
    labelVida7 = tk.Label(self.miFrameSecIzq, image=self.render, border=5)
    labelVida7.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVida6(self):
    imgVida6 = Image.open("./images/Vida6.jpg")
    imgVida6 = imgVida6.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida6)
    labelVida6 = tk.Label(self.miFrameSecIzq, image=self.render, border=5)
    labelVida6.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVida5(self):
    imgVida5 = Image.open("./images/Vida5.jpg")
    imgVida5 = imgVida5.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida5)
    labelVida5 = tk.Label(self.miFrameSecIzq, image=self.render, border=5)
    labelVida5.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVida4(self):
    imgVida4 = Image.open("./images/Vida4.jpg")
    imgVida4 = imgVida4.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida4)
    labelVida4 = tk.Label(self.miFrameSecIzq, image=self.render, border=5)
    labelVida4.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVida3(self):
    imgVida3 = Image.open("./images/Vida3.jpg")
    imgVida3 = imgVida3.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida3)
    labelVida3 = tk.Label(self.miFrameSecIzq, image=self.render, border=5)
    labelVida3.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVida2(self):
    imgVida2 = Image.open("./images/Vida2.jpg")
    imgVida2 = imgVida2.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida2)
    labelVida2 = tk.Label(self.miFrameSecIzq, image=self.render, border=5)
    labelVida2.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVida1(self):
    imgVida1 = Image.open("./images/Vida1.jpg")
    imgVida1 = imgVida1.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida1)
    labelVida1 = tk.Label(self.miFrameSecIzq, image=self.render, border=5)
    labelVida1.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVida0(self):
    imgVida0 = Image.open("./images/Vida0.jpg")
    imgVida0 = imgVida0.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVida0)
    labelVida0 = tk.Label(self.miFrameSecIzq, image=self.render)
    labelVida0.place(relx = 0.5, rely = 0.5, anchor = 'center')

def imgVictoria(self):
    imgVictoria = Image.open("./images/Ganador.jpg")
    imgVictoria = imgVictoria.resize((350, 450), Image.ANTIALIAS)
    self.render = ImageTk.PhotoImage(imgVictoria)
    labelVictoria = tk.Label(self.miFrameSecIzq, image=self.render)
    labelVictoria.place(relx = 0.5, rely = 0.5, anchor = 'center')
# --------------------------------------------------------
'''
Position the window Root
'''
def posicionarVentanaRoot(root):
    #Posicionar ventana
    ancho_ventana = 800
    alto_ventana = 500
    
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.resizable(0,0)
# --------------------------------------------------------    
'''
Execution of the main program
'''
if __name__ == '__main__':

    vidas=7
    listLetrasIng=[]
    pal=''
    resulParcial=[]
    
    root=tk.Tk()
    root.title("JUEGO DEL AHORCADO")
    posicionarVentanaRoot(root)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()