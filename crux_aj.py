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
    
    token = "EAAFvxufavv0BAM0AVZCIuvyvu0tMNSR00KaOwCpB9WikZAkd4yZByDVXYGKbkCm98sZAW5EpE2a9hZCyrLTew7hMHnou8PibZBknQuaD0zL9uxY3amNarntnhm2uMLGJbHFUH7dOgFUvdKTBS2H9Iv1XdnbBAO28ZCDm16DQQaQ2mJlfsFf1lxQCehhYbkw8ieoX3ZCjFl1t3gZDZD"
    
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

    print("\n¿Desea ver la lista de preguntas y respuestas de Crux?, si/no")
    eleccion = input("\nEscriba 'si' o 'no', segun lo que desea hacer: ").lower()

    if eleccion == "si":

        for frase in range(len(training)):
            
            if frase % 2 == 0:
                print("\nIngreso del usuario: ",training[frase])
            
            else:
                print("\nRespuesta de Crux: ", training[frase])    
    
    while eleccion != "si" and eleccion != "no":
        print("\nError, intente nuevamente")
        print("\n¿Desea ver la lista de preguntas y respuestas de Crux?")
        eleccion = input("\nEscriba 'si' o 'no', segun lo que desea hacer: ")
    
    usuario = input("\nIngrese su nombre: ").capitalize()
    
    print(f"\n\n¡¡{usuario}, bienvenido a Crux!!\nPara empezar escriba cualquier cosa que desea.")

    while continuar:
        
        entrada = input(f"\n{usuario}: ").lower()
        user = usuario + ":" + " " + entrada
        log(user)

        if "chau" in entrada or "salir" in entrada:
            respuesta = chatbot.get_response(entrada)
            bot = "Crux: " + str(respuesta) 
            log(bot)
            print("Crux: ",respuesta)
    
            continuar = False

        elif "menu de opciones" in entrada or "menu" in entrada or "opciones" in entrada:
            
            menu.menu(token)
        
        elif "que hora es" in entrada or "hora" in entrada:
            
            hora = time.strftime("%H:%M:%S")
            respuesta = chatbot.get_response(entrada)
            respuesta = str(respuesta) + " " + str(hora)
            bot = "Crux: " + respuesta
            log(bot)
            print("Crux: ",respuesta)

        elif "que dia es hoy" in entrada or "fecha" in entrada or "que fecha es hoy" in entrada:

            fecha = time.strftime("%d/%m/%y")
            respuesta = chatbot.get_response(entrada)
            respuesta = str(respuesta) + " " + str(fecha)
            bot = "Crux: " + respuesta
            log(bot)
            print("Crux: ",respuesta)
            
        else: 
            respuesta = chatbot.get_response(entrada)
            bot = "Crux: " + str(respuesta) 
            log(bot)
            print("\nCrux: ",respuesta)

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

            else: 
                respuesta = chatbot.get_response(entrada)
                bot = "Crux: " + str(respuesta) 
                log(bot)
                print("\nCrux: ",respuesta)

        except facebook.GraphAPIError or requests.exceptions.ConnectionError or urllib3.exceptions.MaxRetryError or urllib3.exceptions.NewConnectionError or socket.gaierror:

            if facebook.GraphAPIError:
                print("\nToken de acceso de página incorrecto o expirado.\nIntente ingresando un nuevo token.\n\nRecuerde que hay una explicacion en actualizacion_token.pdf.")
                token = input("\n\nIngrese el nuevo token: ")    

            else:
                print("\n\nError de conexión.\nChequee que tenga conexión a internet e inténtelo nuevamente.")    

        
main()