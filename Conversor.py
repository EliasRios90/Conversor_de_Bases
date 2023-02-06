from functools import partial
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from Operaciones import boton_borrar, boton_convertir, centrar_widget, llenar_campo, verifica_longitud


BASE_PARTIDA = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
BASE_LLEGADA = ['Todas', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

class Conversor(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.__lista_botones = []
        self.raiz = raiz
        self.raiz.title('Conversor de Bases')

        estilo = ttk.Style()
        estilo.theme_use('clam') #Tema aplicado los checkbox
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        ########################################## IMAGEN DE FONDO ################################################
        imagen = Image.open('image/lago.jpg')
        img = imagen.resize((400, 550), Image.ANTIALIAS)
        self.fondo = ImageTk.PhotoImage(img)

        self.canvas.create_image(0, 0, image=self.fondo, anchor=tk.NW)


        ########################################## ETIQUETA TITULO ################################################
        self.canvas.create_text(centrar_widget(368), 20,
        text='Conversor de Bases',
        fill='white',
        font=('Cooper Black', 26, 'bold'),
        anchor=tk.NW)
        
        
        ########################################### ENTRADA NUMERICA ##############################################
        self.var_txt = tk.StringVar()
        self.txt = tk.Entry(self,
            width=12,
            textvariable=self.var_txt,
            fg='gray17',
            font=('Verdana', 10, 'bold'),
            justify=tk.RIGHT,
            state=tk.DISABLED,
            relief=tk.SUNKEN,
            borderwidth=2)
        # Le sumo 22 (ancho del boton borrar) al ancho del campo de texto
        self.canvas.create_window(centrar_widget(self.txt.winfo_reqwidth()+22), 96, anchor=tk.NW, window=self.txt)
        
        
        ########################################### BOTON BORRAR ##################################################
        self.imagen = tk.PhotoImage(file='image/eliminar.png')
        btn_borrar = tk.Button(self,
            image=self.imagen,
            command=lambda:boton_borrar(self.txt, self.var_txt),
            cursor='hand2',
            bg='#ff2301')
        # Le resto 114 (ancho del campo de texto) al ancho del boton borrar
        self.canvas.create_window(centrar_widget(btn_borrar.winfo_reqwidth()-114), 96, anchor=tk.NW, window=btn_borrar)
        
        
        ########################################## BOTONES NUMERICOS #############################################
        self.__botones()
        
        
        ########################################## BASE DE PARTIDA ###############################################
        self.var_bp = tk.StringVar()
        cbbx_base_partida = ttk.Combobox(self,
            textvariable=self.var_bp,
            state='readonly',
            width=15,
            height=5,
            font=('Tahoma', 10, 'bold'),
            values=BASE_PARTIDA)
        cbbx_base_partida.set('Base de Partida')
        self.canvas.create_window(centrar_widget(cbbx_base_partida.winfo_reqwidth()), 350, anchor=tk.NW, window=cbbx_base_partida)
        
        
        ########################################## BASE DE LLEGADA ###############################################
        self.var_bll = tk.StringVar()
        cbbx_base_llegada = ttk.Combobox(self,
            textvariable=self.var_bll,
            state='readonly',
            width=15,
            height=5,
            font=('Tahoma', 10, 'bold'),
            values=BASE_LLEGADA)
        cbbx_base_llegada.set('Base de Llegada')
        self.canvas.create_window(centrar_widget(cbbx_base_llegada.winfo_reqwidth()), 400, anchor=tk.NW, window=cbbx_base_llegada)
        
        
        ########################################## BOTON CONVERTIR ##############################################
        btn_convertir = tk.Button(self,
            text='Convertir',
            command=lambda:boton_convertir(self.raiz, self.var_txt, self.var_bp, self.var_bll),
            cursor='hand2',
            bg='#ff2301',
            fg='white',
            activeforeground='#ff2301',
            font=('Tahoma', 16, 'bold'))
        self.canvas.create_window(centrar_widget(btn_convertir.winfo_reqwidth()), 460, anchor=tk.NW, window=btn_convertir)
        

        # Para limitar la cantidad de caracteres ingresados al campo de texto
        self.var_txt.trace_variable('w', lambda *args: verifica_longitud(self.var_txt))


    def __botones(self):
        index = 0
        alto = 170
        self.__botones_numericos()
        
        for i in range(6):
            ancho = centrar_widget(self.__lista_botones[0].winfo_reqwidth()*3)
            for j in range(3):
                self.canvas.create_window(ancho, alto, anchor=tk.SW, window=self.__lista_botones[index])
                index += 1
                ancho += 45
            alto += 32


    def __botones_numericos(self):
        texto = 'DEFABC789456123 0 '

        for i in range(18):
            if texto[i] == ' ':
                self.__lista_botones.append(tk.Button(self,
                    text=texto[i],
                    width=4,
                    state=tk.DISABLED,
                    font=('Arial Black', 10, 'bold'),
                    bg='gray17'))
            else:
                self.__lista_botones.append(tk.Button(self,
                    text=texto[i],
                    # partial en lugar de lambda porque estan dentro de un ciclo for
                    command=partial(llenar_campo, self.var_txt, texto[i]),
                    width=4,
                    font=('Arial Black', 10, 'bold'),
                    fg='white',
                    bg='gray17',
                    cursor='hand2',
                    activebackground='white',
                    activeforeground='gray17'))
    
  

