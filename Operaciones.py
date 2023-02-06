import tkinter as tk
from tkinter import messagebox



def mostrar_frame(master, frame):
    """Para mostrar el frame principal"""
    
    nuevo_frame = frame(master)
    nuevo_frame.grid(row=0, column=0, sticky='nsew')
    nuevo_frame.tkraise() # Pone al frame al frente


def centrar_widget(ancho_widget):
    """Para centrar un widget en la ventana."""
    # 400 (ancho de la ventana)
    return (400-ancho_widget)/2
    


def verifica_longitud(campo_texto):#Se debe para pasar como argumento una tupla por mas que no se use
    """Verifica si la longitud del campo de texto es de 7 caracteres."""
    
    campo_texto.set(campo_texto.get()[:7])# Permite solo 7 caracteres


def llenar_campo(var_txt, texto):
    """Inserta el valor de los botones numéricos al campo de texto."""

    if var_txt.get() != '':
        auxiliar = var_txt.get()
        var_txt.set(auxiliar + texto)
    else:
        var_txt.set(texto)


def boton_borrar(campo_texto, var_texto):
    """Borra los caracteres ingresados."""
    
    tamanio = len(var_texto.get())

    if tamanio > 0:
        campo_texto.config(state=tk.NORMAL)
        campo_texto.delete(tamanio-1)
        campo_texto.config(state=tk.DISABLED)


def boton_convertir(master, var_texto, base_partida, base_llegada):
    """Realiza la conversion del número ingresado y muestra el resultado."""
    
    if __verificar_entrada(var_texto, base_partida, base_llegada):
        from Resultado import Resultado
        resultado = __evaluar(var_texto.get(), base_partida.get(), base_llegada.get())
        
        frame_resultado = Resultado(master, base_partida, base_llegada)
        frame_resultado.set_campo_texto(var_texto)
        frame_resultado.set_resultado(resultado)

        if base_llegada.get() == 'Todas':
            frame_resultado.tabla_resultado()
        else:
            frame_resultado.etiqueta_resultado()
        frame_resultado.grid(row=0, column=0, sticky='nsew')


def boton_atras(master, frame_resultado, var_texto, base_p, base_l):
    """Muestra el frame principal."""
    
    master.title('Conversor de Bases')
    base_p.set('Base de Partida')
    base_l.set('Base de Llegada')
    var_texto.set('')
    frame_resultado.destroy()





def __verificar_entrada(var_texto, base_p, base_l):
    """Verifica que el número y las bases ingresadas sean correctas."""
    
    bandera = True
    if var_texto.get() == '':
        messagebox.showerror('[ERROR]', 'Debe ingresar un número.')
        bandera = False
    elif base_p.get() == 'Base de Partida' or base_l.get() == 'Base de Llegada':
            messagebox.showerror('[ERROR]', 'Debe elegir una base de partida y de llegada.')
            bandera = False
    elif not __verifica_entrada_base_partida(var_texto, base_p):
        messagebox.showerror('[ERROR]', 'El número ingresado debe pertenecer a la base de partida.')
        bandera = False
    return bandera


def __verifica_entrada_base_partida(var_texto, base_p):
    """Verifica que el número ingresado pertenezca a la base de partida."""
    
    bandera = True
    auxiliar = None
    for i in var_texto.get():
        if i.isdigit():
            if int(i) >= int(base_p.get()):
                bandera = False
        else:
            # Si le resto 55 a el valor de las letras queda A=10, B=11, C=12, D=13, E=14, F=15
            auxiliar = int(ord(i)) - 55
            if auxiliar >= int(base_p.get()):
                bandera = False
    return bandera


def __evaluar(numero, base_p, base_l):
    """Evalua si se debe convertir a una base o a todas."""
    
    if base_l == 'Todas':
        return __conversor_total(numero, base_p)
    else:
        return __a_otra_base(numero, base_p, base_l)
   
    
def __convertir_a_decimal(numero, base_partida):
    """Convierte un número de X base de partida a base decimal."""
    
    lista = list(reversed(numero))
    conversion = 0
    exponente = 0

    for i in lista:
        
        if i=='A': auxiliar = 10
        elif i=='B': auxiliar = 11
        elif i=='C': auxiliar = 12
        elif i=='D': auxiliar = 13
        elif i=='E': auxiliar = 14
        elif i=='F': auxiliar = 15
        else: auxiliar = int(i)
        
        conversion = conversion + auxiliar*pow(int(base_partida), exponente)
        exponente += 1
    
    return conversion


def __a_otra_base(numero, base_p, base_l):
    """Convierte un número de X base de partida a Y base de llegada."""
    
    conversion = ''
    resto = 0
    decimal = __convertir_a_decimal(numero, base_p)
    base_llegada = int(base_l)

    while True:
        resto = decimal%base_llegada
        decimal = decimal//base_llegada

        if resto==10: conversion = 'A' + conversion
        elif resto==11: conversion = 'B' + conversion
        elif resto==12: conversion = 'C' + conversion
        elif resto==13: conversion = 'D' + conversion
        elif resto==14: conversion = 'E' + conversion
        elif resto==15: conversion = 'F' + conversion
        else: conversion = str(resto) + conversion
        
        #Condicion de salida del ciclo
        if decimal <= 0: break
    
    return conversion


def __conversor_total(numero, base_p):
    """Retorna una lista con todas las conversiones de un número dado."""
    
    lista = []
    
    for i in range(2, 17): # [2, 16]
        resultado = (i, __a_otra_base(numero, base_p, i))
        lista.append(resultado)
    
    return lista

