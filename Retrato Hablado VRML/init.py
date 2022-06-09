import cv2
import time
import imutils
from tkinter import PhotoImage
# import gpio_motor as gp
import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Label, Scale, Style
from PIL import Image, ImageTk
# import captura as cap
import subprocess
import time

#################
import pandas as pd
import tkinter  as tk 

from tkinter import filedialog
from tkinter.filedialog import askopenfile
########

# 1694791985
x = 0
n = 0
ti = 1
OptionListRo = [
    "Rostro Ovalado",
    "Rostro Cuadrado"
] 
OptionListOj = [
    "Ojos Hundidos",
    "Ojos Estrechos"
] 
OptionListNa = [
    "Nariz Ancha",
    "Nariz Base Redonda"
] 
OptionListLa = [
    "Labios Pequeños",
    "Labios Finos"
] 

color_fondo="#A5A8AC"


class App:
    def __init__(self, window, window_title):
        self.window = window
        menubar1 = tk.Menu(self.window)
        self.window.title(window_title)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.geometry("620x320+100+100")

        self.window.configure(background=color_fondo)
        #self.window.wm_iconbitmap('./img/mari2.ico')
        self.style = Style()

        self.window_big()
        self.window_oj()
        self.window_na()
        self.window_la()

        logo_ipn = tk.Frame(self.window, bg="#A5A8AC",  width=80, height=132)
        logo_ipn.place(x=20, y=20)
        ipn = ImageTk.PhotoImage(file="./img/logotipo-ipn.png")
        Imagen_3 = tk.Label(logo_ipn, bg="#A5A8AC",image=ipn)
        Imagen_3.place(x=0, y=0)

        logo_esc = tk.Frame(self.window, bg="#A5A8AC", width=135, height=90)
        logo_esc.place(x=500, y=20)
        esc = ImageTk.PhotoImage(file="./img/logoescom2.png")
        Imagen_2 = tk.Label(logo_esc, bg="#A5A8AC",image=esc)
        Imagen_2.place(x=0, y=0)

        img = Image.open('./img/ro.png')
        img = ImageTk.PhotoImage(img)        
        
        # self.button_mt = tk.Button(self.window, bg="#922b3e", image=img, text="", command=self.motor)
        self.button_ro = tk.Button(self.window, bg="#4b1a21", image=img, text="", command=self.bt_ro)
        self.button_ro["border"] = "0"
        self.button_ro.place(x=320, y=140)

        self.button_oj = tk.Button(self.window, bg="#4b1a21", image=img, text="", command=self.bt_oj)
        self.button_oj["border"] = "0"
        self.button_oj.place(x=390, y=170)

        self.button_na = tk.Button(self.window, bg="#4b1a21", image=img, text="", command=self.bt_na)
        self.button_na["border"] = "0"
        self.button_na.place(x=320, y=210)

        self.button_la = tk.Button(self.window, bg="#4b1a21", image=img, text="", command=self.bt_la)
        self.button_la["border"] = "0"
        self.button_la.place(x=390, y=250)

        img_led = Image.open('./img/ro.png')
        img_led = ImageTk.PhotoImage(img_led)
        self.button_led = tk.Button(self.window, bg="#4b1a21", relief="flat", overrelief="raised", image=img_led,
                                    text="", command=self.bt_led)
        self.button_led["border"] = "0"
        self.button_led.place(x=540, y=200)


        self.imageFrame = tk.Frame(window, width=640, height=400)
        self.imageFrame.columnconfigure(0, weight=1)
        self.imageFrame.grid(row=1, column=0, padx=10, pady=20)
        self.lmain = tk.Label(self.imageFrame)
        self.lmain.grid(row=2, column=0, sticky="w")
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

        # self.show_frame()
        self.window.mainloop()

    def window_big(self):

        my_font1=('times', 12, 'bold')

        self.variable = tk.StringVar(self.window)
        self.variable.set(OptionListRo[0])

        self.opt = tk.OptionMenu(self.window, self.variable, *OptionListRo)
        self.opt.config(width=20, font=('Helvetica', 12))
        self.opt.place(x=50, y=150)

    def window_oj(self):

        my_font1=('times', 12, 'bold')

        self.variableOj = tk.StringVar(self.window)
        self.variableOj.set(OptionListOj[0])

        self.opt = tk.OptionMenu(self.window, self.variableOj, *OptionListOj)
        self.opt.config(width=20, font=('Helvetica', 12))
        self.opt.place(x=50, y=190)

    def window_na(self):

        my_font1=('times', 12, 'bold')

        self.variableNa = tk.StringVar(self.window)
        self.variableNa.set(OptionListNa[0])

        self.opt = tk.OptionMenu(self.window, self.variableNa, *OptionListNa)
        self.opt.config(width=20, font=('Helvetica', 12))
        self.opt.place(x=50, y=230)

    def window_la(self):

        my_font1=('times', 12, 'bold')

        self.variableLa = tk.StringVar(self.window)
        self.variableLa.set(OptionListLa[0])

        self.opt = tk.OptionMenu(self.window, self.variableLa, *OptionListLa)
        self.opt.config(width=20, font=('Helvetica', 12))
        self.opt.place(x=50, y=270)
        

    def bt_ro(self, *args):
        z = self.variable.get()
        if z == 'Rostro Cuadrado':
            print("cara cuadrada") #esta sentencia no se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/rostro_rectangular.wrl"])
            time.sleep(5)
            p.terminate()
        elif z == 'Rostro Ovalado':
            print("cara ovalada") #esta sentencia se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/rostro_ovalado.wrl"])
            time.sleep(5)
            p.terminate()
        else:
            print("¡Yo tampoco!") #esta sentencia no se ejecuta

    def bt_oj(self, *args):
        z = self.variableOj.get()
        if z == 'Ojos Hundidos':
            print("ojos hundidos") #esta sentencia no se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/ojos.wrl"])
            time.sleep(5)
            p.terminate()
        elif z == 'Ojos Estrechos':
            print("ojos estrechos") #esta sentencia se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/ojos.wrl"])
            time.sleep(5)
            p.terminate()
        else:
            print("¡Yo tampoco!") #esta sentencia no se ejecuta

    def bt_na(self, *args):
        z = self.variableNa.get()
        if z == 'Nariz Ancha':
            print("nariz ancha") #esta sentencia no se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/nariz_ancha.wrl"])
            time.sleep(5)
            p.terminate()
        elif z == 'Nariz Base Redonda':
            print("nariz base redonda") #esta sentencia se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/nariz_ancha.wrll"])
            time.sleep(5)
            p.terminate()
        else:
            print("¡Yo tampoco!") #esta sentencia no se ejecuta

    def bt_la(self, *args):
        z = self.variableLa.get()
        if z == 'Labios Pequeños':
            print("labios pequeños") #esta sentencia no se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/labios_pequeños.wrl"])
            time.sleep(5)
            p.terminate()
        elif z == 'Labios Finos':
            print("labios finos") #esta sentencia se ejecuta
            p = subprocess.Popen(["C:/Users/ACER/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "R:/Maestría ESCOM/2do Semestre/RV/labios_finos.wrl"])
            time.sleep(5)
            p.terminate()
        else:
            print("¡Yo tampoco!") #esta sentencia no se ejecuta
        

    def bt_led(self):
        # t2=self.entry.get())
        p = subprocess.Popen(["C:/Users/pc/AppData/Local/Bitmanagement Software/BS Contact/BSContact.exe", "C:/Users/pc/Documents/Articulo Realidad virtual/inline/interface/V006.wrl"])
        time.sleep(10)
        p.terminate()
        # try:
        #     t2=int(self.entry_led.get())
        #     if t2 < 100:
        #         print(t2)
        #     else:
        #         t2 = self.entry_led.get()
        #         messagebox.showwarning("Dato invalido", "El dato *" + t2 + "* debe ser menor a 100 ")

        # except ValueError:
        #     t2=self.entry_led.get()
        #     messagebox.showwarning("Dato invalido", "El dato *"+t2+"* no es invalido ")
        # self.entry_led.delete(0, tk.END)
    
    def upload_file(self):
        self.f_types = [('CSV files',"*.csv"),('All',"*.*")]
        self.file = filedialog.askopenfilename(filetypes=self.f_types)
        self.l1.config(text=self.file) # display the path 
        self.df=pd.read_csv(self.file) # create DataFrame
        str1="Rows:" + str(self.df.shape[0])+ "\nColumns:"+str(self.df.shape[1])
        #print(str1)
        self.t1.insert(tk.END, str1) # add to Text widget


    def show_frame(self):
        _, frame = self.cap.read()
        frame = imutils.resize(frame, height=200,width=600)
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame)

    def foto(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            self.img_name = "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
            cv2.imwrite(self.img_name, frame)
            print("{} written!".format(self.img_name))
            f = self.img_name
            label = tk.Label(self.window, bg="#000000", fg="#FF8000", font=("Arial Black", 8), text="" + f)
            label.place(x=90, y=375)
            shutil.move(self.img_name, 'Temp/' + self.img_name)
            self.saveas = 'Temp/' + self.img_name


        if not ret:
            print("failed to grab frame")

    def snapshot(self):
        #f = cap.file_save(self.saveas)
        f='relize'
        label = tk.Label(self.window, bg="#000000", fg="#FF8000", font=("Arial Black", 8), text="" + f)
        label.place(x=90, y=375)
        print(f)


    def on_closing(self):
        if messagebox.askokcancel("Cerrar", "El programa finalizará ¿Desea continuar?"):
            dir = "Temp/"
            lista_ficheros = os.listdir(dir)
            print(lista_ficheros)
            for fichero in lista_ficheros:
                if fichero.endswith(".jpg"):
                    os.remove(dir + fichero)
            dir = "./"
            lista_ficheros = os.listdir(dir)
            print(lista_ficheros)
            for fichero in lista_ficheros:
                if fichero.endswith(".jpg"):
                    os.remove(dir + fichero)
            if self.cap.isOpened():
                self.cap.release()

            self.window.destroy()



App(tk.Tk(), "RETRATO HABLADO")
