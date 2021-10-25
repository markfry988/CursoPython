# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:51:51 2021

@author: markf
"""

#Programa que identifica el tipo de dato de un valor ingresado por el usuario
#variables

cnt=0 #contador en cero para empezar las iteraciones
for cnt in [0,1,2,3,4]: #un for para que solamente me de 5 interacciones
    var1=input("Ingrese un valor cualquiera: ") #el usuario introduce un valor cualquiera
    print("Este tipo de dato en Python es: \n",type(var1)) #se devuelve el tipo de dato str
    cnt+=1 #el contador aumenta en 1, el cual está ligado con el for
    print(var1) #se muestra la variable en pantalla
print("¡YA NO SE HARÁN MÁS INTERACCIONES!") #terminada las 5 interacciones, se muestra el mensaje
