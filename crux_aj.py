import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import menu
import time
import facebook
import facebook_crux
from PIL import Image
import urllib3
from urllib.request import urlopen
import requests

def log(mensaje):
   
    fecha = time.strftime("%d/%m/%y")
    hora = time.strftime("%H:%M:%S")
    with open("archivo.log_bot","a") as otro_archivo:
        otro_archivo.write(fecha + "," + hora +"," + mensaje +"\n") 


def main():
    
    token = "EAAFvxufavv0BAFEfNjsWKR4kaGy7oYQu0eXmNmf2TL6gX1nEjxzkvZBAGBpY59AoFwZARLHkT2ZAaZBMg35LZCpaG0uIOy6SrHjHbVMh4SZBHaazDKMZC3ZCt6VR0JcE2PFAK0OP3aN4vUuXoHI0WUbiZCseLaZB2OVP1ZCBeq1ZCFnt3XA0PGNvD2JfvTp16kQWR7EZD"
    
    no_entendio = "Disculpe no comprendo lo que escribió, no estoy lo suficientemente entrenado para entender.\nIntente nuevamente con algo diferente."
    
    chatbot = ChatBot("Tester",
                  logic_adapters=[
                    {
                        'import_path': 'chatterbot.logic.BestMatch'
                        ,
                        'default_response': no_entendio
                    }
                ])

    training = []
    with open("trainer.txt","r") as archivo:
        for linea in archivo:
            training.append(linea.strip("\n"))

    trainer = ListTrainer(chatbot)

    trainer.train(training)

    continuar = True

    while continuar:
        
        entrada = input("Usuario: ").lower()
        user = "Usuario: " + entrada
        log(user)

        if "chau" in entrada or "salir" in entrada:
            respuesta = chatbot.get_response(entrada)
            bot = "Crux: " + str(respuesta) 
            log(bot)
            print("Crux: ",respuesta)
    
            continuar = False


        elif "menu de opciones" in entrada or "menu" in entrada or "opciones" in entrada:
            menu.menu(token)
        
        try:

            if "postear foto fb" in entrada:
                
                try:
                    print("\nUsted eligió; Postear una foto.")
                        
                    imagen = input("\nIngrese el nombre de la imagen que desea subir (no olvide añadir .jpg o .png o .jpeg): ")

                    mensaje = input("\nIngrese el texto que quiere publicar junto con la foto: ")

                    facebook_crux.postear_foto(token,mensaje,imagen)

                    img = Image.open(imagen,'r')

                    img.show()
                    
                except FileNotFoundError:
                    print("\nEl archivo que ingresó debe estar en la misma carpeta que Crux.py, o no existe.\nIntente nuevamente.")

            elif "postear texto fb" in entrada:
                
                print("\nUsted eligió: Subir posteo.")
                mensaje = input("\nIngrese e texto que quiere postear: ")
                facebook_crux.posteo(token,mensaje)

            elif "like fb" in entrada:
                
                print("\nUsted eligió: Dar likes a posteo.")
                post = facebook_crux.mostrar_posts(token) 
                posteo = post["posts"]["data"]
                
                for diccionario in range(len(posteo)):
                    try:
                        fecha = posteo[diccionario]["created_time"]
                        texto = posteo[diccionario]["message"]
                        print(str(diccionario) + "\t" + texto + "\t\t" + "--Fecha: " + fecha)
                    except KeyError:
                        print(str(diccionario) + "\t" + "Este posteo no tiene ningun texto " + "--Fecha: " + fecha) 
                    
                eleccion_likear = int(input("\nIngrese el número de posteo que desea comentar: ")) 
                id = posteo[eleccion_likear]["id"]
                facebook_crux.likear(token,id)
            
            elif "comentar fb" in entrada:

                print(" \nUsted eligió: Comentar un posteo")
                post = facebook_crux.mostrar_posts(token) 
                posteo = post["posts"]["data"]
                
                for diccionario in range(len(posteo) - 3):
                    print(str(diccionario) + ":" + posteo[diccionario]["message"])
                    
                eleccion_comentar = int(input("\nIngrese el número de posteo que desea comentar: ")) 
                id = posteo[eleccion_comentar]["id"]
                mensaje = input("\nIngrese el texto que quiere comentar: ")
                facebook_crux.comentar(token,mensaje,id)

        except facebook.GraphAPIError or requests.exceptions.ConnectionError or urllib3.exceptions.MaxRetryError or urllib3.exceptions.NewConnectionError or socket.gaierror:

            if facebook.GraphAPIError:
                print("Token de acceso de página incorrecto o expirado.\nIntente ingresando un nuevo token.\nRecuerde que hay una explicacion en README.txt.")
                token = input("Ingrese el nuevo token: ")    

            else:
                print("\n\nError de conexión.\nChequee que tenga conexión a internet e inténtelo nuevamente.")    

        respuesta = chatbot.get_response(entrada)
        bot = "Crux: " + str(respuesta) 
        log(bot)
        print("Crux: ",respuesta)

main()