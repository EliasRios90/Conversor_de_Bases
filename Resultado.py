import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from Operaciones import boton_atras


class Resultado(tk.Frame):
    def __init__(self, raiz, base_p, base_l):
        super().__init__(raiz)
        self.__raiz = raiz
        self.__base_p = base_p
        self.__base_l = base_l

        raiz.title('Resultado')
        self.config(background='gray17')


    def __btn_atras(self):
        """Botón para volver al frame principal."""
        imagen = Image.open("image/flecha_atras.png")
        self.imagen_nueva = ImageTk.PhotoImage(imagen)

        tk.Button(self,
            text='Atrás',
            fg='white',
            bg='#ff2301',
            cursor='hand2',
            activebackground='white',
            activeforeground='#ff2301',
            image=self.imagen_nueva,
            command=lambda:boton_atras(self.__raiz, self,self.__campo_texto, self.__base_p, self.__base_l),
            compound=tk.LEFT,
            font=('Tahoma', 16, 'bold')).pack(pady=(40, 0))

    
    def etiqueta_resultado(self):
        """Para mostrar un solo resultado."""
        lbl = tk.Label(self,
                text=self.__resultado,
                relief=tk.SUNKEN,
                borderwidth=10,
                bg='gray17',
                fg='white')
        lbl.pack(pady=(150, 30), ipadx=10, ipady=10)
        
        # Cambio el tamaño de fuente del resultado para que un numero con muchos digitos quepa en pantalla 
        if len(self.__resultado) >= 20:
            lbl.config(font=('Verdana', 13, 'bold'))
        else:
            lbl.config(font=('Verdana', 20, 'bold'))

        self.__btn_atras()
    

    

    def tabla_resultado(self):
        """Para mostrar una tabla con todas la conversiones de un número."""
        tabla = ttk.Treeview(self, columns=('Base', 'Resultado'), height=15, show='headings')
        tabla.pack(pady=(10, 0))

        tabla.heading('Base', text='Base')
        tabla.heading('Resultado', text='Resultado')

        tabla.column('Base', anchor=tk.CENTER, width=60)
        tabla.column('Resultado', anchor=tk.CENTER, width=330)
        
        #Agregando estilos a la cabecera y cuerpo del Treeview
        estilo = ttk.Style()
        estilo.theme_use('clam') #Tema aplicado al Treeview
        
        #Para los encabezados
        estilo.configure("Treeview.Heading", 
            font=('Arial Black', 12, 'bold'), 
            background='black', 
            foreground='white')
        
        #Para el cuerpo de la tabla
        estilo.configure('Treeview', 
            font=('Lucinda Console', 12, 'bold'),
            rowheight=25) #Altura de fila

        index = 0
        for item in self.__resultado:
            if index%2==0:
                tabla.insert('', tk.END, values=(item), tags=('even',)) #Resultado par
            else:
                tabla.insert('', tk.END, values=(item), tags=('odd',)) #Resultado impar
            index += 1
        
        tabla.tag_configure('even', background='lightgray', foreground='black')
        tabla.tag_configure('odd', background='white', foreground='black')

        self.__btn_atras()
        
        


    #Setters
    def set_campo_texto(self, campo_texto): 
        self.__campo_texto = campo_texto    
    
    
    def set_resultado(self, resultado): 
        self.__resultado = resultado