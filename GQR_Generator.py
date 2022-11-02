import qrcode as qr
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask,SolidFillColorMask
import subprocess, os
from colorchooser import Chooser
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter.ttk import *




class QR_selector:
    def __init__(self,root):
        self.window=root
        self.window.title("QR_Generator")

        style = Style()
        style.configure('W.TButton', font =
               ('Constantia', 10, 'bold', 'underline'),
                foreground = 'blue')
        
        framePrin=tk.LabelFrame(self.window,text="QR_Generator",foreground ='grey')
        framePrin.grid(row=0,column = 0, columnspan = 1,pady=20)

        frameradio=tk.LabelFrame(self.window,text="Opciones de formato",foreground ='grey')
        frameradio.grid(row=0,column = 1, columnspan = 20,pady=10)

        LabelText=Label(framePrin,text='ingresa el texto o URL a convertir').grid(row=1,column=0)
        self.Entrytext=Entry(framePrin)
        self.Entrytext.focus()
        self.Entrytext.grid(row=2,column=0,ipadx=30)

        #LabelText=Label(frameradio,text='selecciona formato').grid(row=1,column=1)
        self.exitformat=IntVar()
        self.pngradio=tk.Radiobutton(frameradio,text="PNG",variable=self.exitformat,value=1,highlightthickness=1)
        self.pngradio.grid(row=2,column=1,sticky="W")
        self.svgradio=tk.Radiobutton(frameradio,text="SVG",variable=self.exitformat,value=2,highlightthickness=0)
        self.svgradio.grid(row=3,column=1,sticky="W")

        framedesing=tk.LabelFrame(self.window,text="Opciones de diseño",foreground ='grey')
        framedesing.grid(row=3,column=1)
        self.desing=IntVar()
        self.radionormal=tk.Radiobutton(framedesing,text="Normal",variable=self.desing,value=1)
        self.radionormal.grid(row=4,column=1,sticky="W")
        self.radioredondeado=tk.Radiobutton(framedesing,text="Redondeado",variable=self.desing,value=2)
        self.radioredondeado.grid(row=5,column=1,sticky="W")
        self.radiodegradado=tk.Radiobutton(framedesing,text="Degradado",variable=self.desing,value=3)
        self.radiodegradado.grid(row=6,column=1,sticky="W")

        
        ttk.Button(self.window, text='Generar',style = 'W.TButton',command=self.Btniteraciones).grid(row=6,column=0,pady=10)#,pady = 10,sticky=W+E)
        ttk.Button(self.window, text='Salir',command=root.destroy,style = 'W.TButton').grid(row=6,column=1)

        ttk.Button(framePrin, text='Ubicar Archivo',style = 'W.TButton',command=self.ubicar).grid(row=3,column=0,pady=10)#,pady = 10,sticky=W+E=5,column=1)

 
    def Btniteraciones(self):
        if self.exitformat.get() == 1 and self.desing.get()== 1:
            self.color_solido()
            self.extensionPNG()

        if self.exitformat.get() == 2 and self.desing.get()== 1:
             self.color_solido()
             self.extensionSVG()

        if self.exitformat.get() == 1 and self.desing.get()== 2:
             self.borde_redondo()
             self.extensionPNG()

        if self.exitformat.get() == 2 and self.desing.get()== 2:
             self.borde_redondo()
             self.extensionSVG()
             
        if self.exitformat.get() == 1 and self.desing.get()== 3:
             
             self.color_centro()
             self.color_bordes()
             self.degradado()
             self.extensionPNG()

        if self.exitformat.get() == 2 and self.desing.get()== 3:
             messagebox.showinfo(title='Atencion!', message='Formato SVG no es compatible con degradado')
             #self.color_centro()
             #self.color_bordes()
             self.color_solido()
             self.extensionSVG()

    def color_solido(self):
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(self.Entrytext.get())
        self.img_1 = qr.make_image(fill_color="blue", back_color="white")
        

    def extensionPNG(self):
            self.img_1.save("CodigoQR.png")
            subprocess.Popen("CodigoQR.png", shell=True)

    def extensionSVG(self):
            self.img_1 = qrcode.make(self.Entrytext.get(), image_factory=qrcode.image.svg.SvgPathImage, box_size=20)
            self.img_1.save("CodigoQR.svg")
            subprocess.Popen("CodigoQR.svg", shell=True)

    def borde_redondo(self):
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(self.Entrytext.get())
            self.img_1 = qr.make_image(image_factory=StyledPilImage,color_mask=SolidFillColorMask(back_color = (255,255,255), front_color = (0,0,0)), module_drawer=RoundedModuleDrawer())

    def color_centro(self):
        function = Chooser()
        codigoRGB = function.show()
        Red = str(codigoRGB[0]).split(".")
        centrorojoabsoluto = str(Red[0])
        self.centrorojoabsoluto = int(centrorojoabsoluto)
        Green = str(codigoRGB[1]).split(".")
        centroverdeabsoluto = str(Green[0])
        self.centroverdeabsoluto = int(centroverdeabsoluto)
        Blue = str(codigoRGB[2]).split(".")
        centroazulabsoluto = str(Blue[0])
        self.centroazulabsoluto = int(centroazulabsoluto)

    def color_bordes(self):
    #global bordeazulabsoluto, borderojoabsoluto,bordeverdeabsoluto
        function = Chooser().wm_attributes
        codigoRGB = function.show()
        Red = str(codigoRGB[0]).split(".")
        borderojoabsoluto = str(Red[0])
        self.borderojoabsoluto = int(borderojoabsoluto)
        Green = str(codigoRGB[1]).split(".")
        bordeverdeabsoluto = str(Green[0])
        self.bordeverdeabsoluto = int(bordeverdeabsoluto)
        Blue = str(codigoRGB[2]).split(".")
        bordeazulabsoluto = str(Blue[0])
        self.bordeazulabsoluto = int(bordeazulabsoluto)

    def degradado(self):
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(self.Entrytext.get())
        self.img_1 = qr.make_image(image_factory=StyledPilImage,
                                   color_mask=RadialGradiantColorMask(

                                       back_color = (255,255,255), center_color = (self.centrorojoabsoluto

                                                                                  ,self.centroverdeabsoluto,self.centroazulabsoluto),
                                                                                  edge_color = (self.borderojoabsoluto,self.bordeverdeabsoluto,                                                                                         self.bordeazulabsoluto)))
    def ubicar(self):
            ruta=os.getcwd()
            complete_path=f'start %windir%\explorer.exe "{ruta}"'
            subprocess.run(complete_path,shell=True)
    
if __name__==('__main__'):

    root = Tk()
    apllication=QR_selector(root)
    root.mainloop()
