#!/usr/bin/env python3
import os 
from colorama import init, Fore, Back, Style
init()

print(Style.BRIGHT+Fore.RED+"""
Author:      Hans Saldias
Creador:    Viernes 07 de julio
Uso :          Sacar promedios
motivo:      Practica de programacion
lenguaje:    python

\n\n""")


os.system("clear")  
print(Style.BRIGHT+Fore.RED+"Script creado por H.saldias\n ")
print("solicita la contraseña en @UnLugarParaProgramar")
contra = input("\n\nIngrese contraseña para usar Script: ")
print("\n"*2)
if contra == "user123":
    print("Axeso online")
    while True:
         print("""
                                      ############
                                      ||     GEO IP WEB  ||
                                      ############
                                CREATED BY: H.SALDIAS
              
             opteniendo ya la ip a buscar o rastrear elige la opcion y 
             
                               comienza a usar la herramienta       
                               
                               [1]              GRABIFY
                               
                               [2]             NUMERIFY
                               
                               [3]             IPLOGGER
                               
                               [4]           CUAL ES MI IP
                               
                               [0]                 SALIR
                                                  
                                                                                        
        """)
    
         op = input("Ingresa la opcion $  ")
        
         if op == "1":
             os.system("termux-open https://grabify.link/")
         elif op == "2":
             os.system("termux-open https://numverify.com/")
         elif op == "3":
             os.system("termux-open https://iplogger.org/es/")
         elif op == "4":
             os.system("termux-open https://www.cual-es-mi-ip.net/geolocalizar-ip-mapa")
         elif op == "0":
             print("Gracias por usar mi script Crador: H.Saldias")         
             break
         else:
             os.system("clear")
             print("La opcion ingresada no es valida, intente nuevamente")
             
else:
    print("Contraseña incorrecta, Contacte al canal del creador =>\n")
    con = input("contactar al creador (y/n) $ ")
    if con == "y":
        os.system("termux-open https://youtube.com/@UnLugarParaProgramar")
    else:
        print("\nGracias por usar mi script: H.saldias ^")

