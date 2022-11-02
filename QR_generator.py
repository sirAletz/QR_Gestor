import qrcode as qr
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask,SolidFillColorMask
import subprocess
from colorchooser import Chooser
import sys


centrorojoabsoluto = ''
centroverdeabsoluto = ''
centroazulabsoluto = ''
borderojoabsoluto = ''
bordeverdeabsoluto = ''
bordeazulabsoluto = ''
text = ''

def color_centro():
    global centroazulabsoluto, centrorojoabsoluto, centroverdeabsoluto
    function = Chooser()
    codigoRGB = function.show()
    Red = str(codigoRGB[0]).split(".")
    centrorojoabsoluto = str(Red[0])
    centrorojoabsoluto = int(centrorojoabsoluto)
    Green = str(codigoRGB[1]).split(".")
    centroverdeabsoluto = str(Green[0])
    centroverdeabsoluto = int(centroverdeabsoluto)
    Blue = str(codigoRGB[2]).split(".")
    centroazulabsoluto = str(Blue[0])
    centroazulabsoluto = int(centroazulabsoluto)

def color_bordes():
    global bordeazulabsoluto, borderojoabsoluto,bordeverdeabsoluto
    function = Chooser()
    codigoRGB = function.show()
    Red = str(codigoRGB[0]).split(".")
    borderojoabsoluto = str(Red[0])
    borderojoabsoluto = int(borderojoabsoluto)
    Green = str(codigoRGB[1]).split(".")
    bordeverdeabsoluto = str(Green[0])
    bordeverdeabsoluto = int(bordeverdeabsoluto)
    Blue = str(codigoRGB[2]).split(".")
    bordeazulabsoluto = str(Blue[0])
    bordeazulabsoluto = int(bordeazulabsoluto)
    
def extension(img_1):
        global text
        formato=input("Código generado!- elige el formato de salida\n1) PNG 2) SVG\n")
        if formato=='1':
            img_1.save("CodigoQR.png")
            subprocess.Popen("CodigoQR.png", shell=True)
        elif formato == '2':
            img_1 = qrcode.make(text, image_factory=qrcode.image.svg.SvgPathImage, box_size=20)
            img_1.save("CodigoQR.svg")
            subprocess.Popen("CodigoQR.svg", shell=True)
    
def respuesta_final():
    respuesta=input("Deseas otro codigo? S/N:\n")
    if respuesta=='S' or respuesta== 's':
        Menu_estilos()
    elif respuesta=='N' or respuesta=='n':
        print("Hasta pronto!")
        sys.exit()
    else:
        print("respuesta invalida")
        respuesta_final()
            
def Menu_estilos():
    global text
    text=input("Indica el texto a convertir en QR\n")
    
    """formato=input("Elige el formato de salida\n")"""

    print("si deseas algún estilo preciona la opcion deseada\n")

    estilo=input("1) sin estilo\n2) redondeado\n3) degradado\n4) Salir\n")
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(text)
    if estilo =='2':
        continuar=input("Presiona enter para Definir el color\n")
        color_bordes()
        img_1 = qr.make_image(image_factory=StyledPilImage,color_mask=SolidFillColorMask(back_color = (255,255,255), front_color = (borderojoabsoluto,bordeverdeabsoluto,bordeazulabsoluto)), module_drawer=RoundedModuleDrawer())
        extension(img_1)
        respuesta_final()
    elif estilo=='1':
        img_1 = qr.make_image(fill_color="blue", back_color="white")
        extension(img_1)
        respuesta_final()
    elif estilo == '3':
        continuar=input("Presiona enter para Definir el color del centro\n")
        color_centro()
        continuar=input("Presiona enter para Definir el color del exterior\n")
        color_bordes()
        img_1 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(back_color = (255,255,255), center_color = (centrorojoabsoluto,centroverdeabsoluto,centroazulabsoluto), edge_color = (borderojoabsoluto,bordeverdeabsoluto,bordeazulabsoluto)))
        extension(img_1)
        respuesta_final()
    elif estilo=='4':
        sys.exit()
    else:
        print("Opción ínvalida")
        Menu_estilos()

Menu_estilos()


