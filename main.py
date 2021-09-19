from tkinter import * 
from tkinter import filedialog
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from numpy.lib.function_base import select
from skimage import io, color, transform
#import cv2
#import imutils
import numpy as np



def elegir_imagen():
    path_image = filedialog.askopenfilename(filetypes= [
    ("images",".jpg"),
    ("images",".jpeg"),
    ("images",".png"),
    ]
    )
    if len(path_image) > 0:
        global image
        #Leer imagen de entrada
        image = io.imread(path_image)
        image = transform.rescale(image, scale=(0.5,0.5,1))

        # Imagen visualizar las imagenes de entrada en GUI
        imageToShow = transform.resize(image, (180,180 ) ) 
        im = Image.fromarray((imageToShow* 255).astype(np.uint8))
        #print("O"*20)
        img = ImageTk.PhotoImage(image = im)
        lblInputImage.configure(image=img)
        lblInputImage.image = img
        ##Label de la imagen
        lblInfo1 = Label(root,text = "Imagen de entrada",bg = '#D673FA')
        lblInfo1.grid(column= 0 , row = 1 ,padx= 5 , pady=5)


        rad1['state'] = tk.NORMAL
        rad2['state'] = tk.NORMAL
        rad3['state'] = tk.NORMAL
        rad4['state'] = tk.NORMAL
        rad5['state'] = tk.NORMAL
        rad6['state'] = tk.NORMAL
        rad7['state'] = tk.NORMAL
        rad8['state'] = tk.NORMAL
        rad9['state'] = tk.NORMAL

def resizing():
    global image
    global img_resized
    if select.get() == 1:
        multiplicador = 4
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (350,350 ) )
    if select.get() == 2:
        multiplicador = 2
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (350,350 ) )
    if select.get() == 3:
        multiplicador = 1
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (350,350 ) )

    if select.get() == 4:
        multiplicador = 1/2
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (300,300 ) )

    if select.get() == 5:
        multiplicador = 1/4
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (250,250 ) )

    if select.get() == 6:
        multiplicador = 1/8
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (200,200 ) )
    if select.get() == 7:
        multiplicador = 1/16
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (180,180 ) )

    if select.get() == 8:
        multiplicador = 1/32
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (150,150 ) )

    if select.get() == 9:
        multiplicador = 1/64
        tupla_de_tam = image.shape
        img_resized = transform.resize(image, (int(tupla_de_tam[0] * multiplicador),int(tupla_de_tam[1] * multiplicador) ))
        imageToShow = transform.resize(img_resized, (50,50 ) )

    # Imagen visualizar las imagenes de entrada en GUI
    #imageToShow = transform.resize(img_resized, (250,250 ) ) 
    im = Image.fromarray((imageToShow* 255).astype(np.uint8))
    #rint("O"*20)
    img = ImageTk.PhotoImage(image = im)

    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    ##Label de la imagen
    lblInfo3 = Label(root,text = "Imagen de salida",font="bold",bg = '#D673FA')
    lblInfo3.grid(column= 1 , row = 0 ,padx= 5 , pady=5)
    btn_save['state'] = tk.NORMAL

def salvar():
    io.imsave("imagen_guarda.png", img_resized)
    pass


image = None
img_resized = None
#principal window
root = Tk()
"""
icono = PhotoImage(file="album.png")
Label(root,image=icono).pack()"""
#

root.config(bg = '#D673FA')
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='album.png'))
root.title("Operador de imagenes")

lblOutputImage = Label(root)
lblOutputImage.config(bg= '#D673FA')
lblOutputImage.grid(column=1,row=1, rowspan=6)

#Label donde se presenta la imagen de salida 
# 
lblInputImage = Label(root)
lblInputImage.config(bg = '#D673FA')
lblInputImage.grid(column=0,row=2)

#label 
lblInfo2 = Label(root , text="Escoje la proporcion a la cual vas a escalar la imagen" ,bg = '#D673FA')
lblInfo2.grid(column=  0 ,row = 3, padx= 5 ,pady= 5)

lblInfo4 = Label(root , text="Esto solo es una representacion aproximada para obtener la imagen da click en guardar",bg = '#D673FA' )
lblInfo4.grid(column=  1 ,row = 9, padx= 5 ,pady= 5)
#Creamos radio buttons
select = IntVar()
rad1 = Radiobutton(root,text = "2", width =5,value = 1 , variable = select,command=resizing    ,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad2 = Radiobutton(root,text = "1", width =5,value = 2 , variable = select,command=resizing    ,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad3 = Radiobutton(root,text = "1/2", width =5,value = 3 , variable = select,command=resizing  ,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad4 = Radiobutton(root,text = "1/4", width =5,value = 4 , variable = select,command=resizing  ,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad5 = Radiobutton(root,text = "1/8", width =5,value = 5 , variable = select,command=resizing  ,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad6 = Radiobutton(root,text = "1/16", width =5,value =  6 , variable = select,command=resizing,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad7 = Radiobutton(root,text = "1/32", width =5,value = 7 , variable = select,command=resizing ,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad8 = Radiobutton(root,text = "1/64", width =5,value =  8 , variable = select,command=resizing,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')
rad9 = Radiobutton(root,text = "1/128", width =5,value = 9 , variable = select,command=resizing,state=tk.DISABLED ,fg = "#9744E3",bg = "#D673FA",activebackground='#9567FB')

rad1.grid(column=  0 ,row = 4)
rad2.grid(column=  0 ,row = 5)
rad3.grid(column=  0 ,row = 6)
rad4.grid(column=  0 ,row = 7)
rad5.grid(column=  0 ,row = 8)
rad6.grid(column=  0 ,row = 9)
rad7.grid(column=  0 ,row = 10)
rad8.grid(column=  0 ,row = 11)
rad9.grid(column=  0 ,row = 12)


btn = Button(root, text = "Elige tu imagen", width=25,command=elegir_imagen, bg = "#9744E3")
btn.grid(column=  0 ,row = 0, padx= 5 ,pady= 5)

btn_save = Button(root, text = "Guardar", width=25,command=salvar,state= tk.DISABLED,bg = "#9744E3")
btn_save.grid(column=  1 ,row = 10, padx= 5 ,pady= 5)

root.mainloop()

