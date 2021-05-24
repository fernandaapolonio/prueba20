import time
from os import sysitem

atbash = { 'A' : 'Z' , 'B' : 'Y' , 'C' : 'X' , 'D' : 'W' , 'E' : 'V' ,
        'F' : 'U' , 'G' : 'T' , 'H' : 'S' , 'I' : 'R' , 'J' : 'Q' ,
        'K' : 'P' , 'L' : 'O' , 'M' : 'N' , 'N' : 'M' , 'O' : 'L' ,
        'P' : 'K' , 'Q' : 'J' , 'R' : 'I' , 'S' : 'H' , 'T' : 'G' ,
        'U' : 'F' , 'V' : 'E' , 'W' : 'D' , 'X' : 'C' , 'Y' : 'B' , 'Z' : 'A' , '. ' : '?' , '?' : '.' }

def atbash_cypher(message):
    finalMessage = ""
    for letter in message.upper():
        if letter != " ":
            finalMessage += atbash[letter]
        else:
            finalMessage += " "

    finalMessage = finalMessage.lower().capitalize()
    
    return finalMessage
    
def procesando (message):
    system("clear")
    y = message
    conunter = 0
    puntos = 0
    
    print(y)
    time.sleep(1)
    system("clear")
    while counter < 7:
        if puntos < 3:
            y += "."
            puntos += 1
            print(y)
            time.sleep(1)
            system("clear")
        else:
            y = message
            puntos = 0
            print(y)
            time.sleep(1)
            system("clear")
        
        counter += 1
        
        
def menu ():
    print("Hola niña")
    time.sleep(3)
    print("Aqui puedes decifrar los mensajes que te envie")
    time.sleep(5)                                         
    inputVale = str(input("Pegalo aquí: "))               
    mensaje = atbash_cypher(inputVale)                    
    print("---------------------------------------------------------------")
    time.sleep(2)
    procesando("Procesando")
    procesando("Ya casi")
    procesando("Falta poco")
    procesando("AGHHHHH")
    print("----------------------------------------------------")
    print("Mensaje: ", mensaje)
    print("----------------------------------------------------")
    
    menu ()
