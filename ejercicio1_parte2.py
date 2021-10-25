# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:51:51 2021

@author: markf
"""

#Programa que identifica el tipo de dato de un valor ingresado por el usuario
#variables

cnt=0
for cnt in [0,1,2,3,4]:
    var1=input("Ingrese un valor cualquiera: ")
    print("Este tipo de dato en Python es: \n",type(var1))
    cnt+=1
    print(var1)
print("¡YA NO SE HARÁN MÁS INTERACCIONES!")