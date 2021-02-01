import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import menu_prueba
import time

def log(mensaje):
   
    fecha = time.strftime("%d/%m/%y")
    hora = time.strftime("%H:%M:%S")
    with open("archivo.log_bot","a") as otro_archivo:
        otro_archivo.write(fecha + "," + hora +"," + mensaje +"\n") 


def main():
    chatbot = ChatBot("Tester")

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
        respuesta = chatbot.get_response(entrada)
        bot = "Crux: " + str(respuesta) 
        log(bot)
        print("Crux: ",respuesta)
        
        
        if entrada == "chau":
            respuesta = chatbot.get_response(entrada)
            bot = "Crux: " + str(respuesta) 
            log(bot)
            print("Crux: ",respuesta)
        
            continuar = False


        elif entrada == "menu":
            respuesta = chatbot.get_response(entrada)
            bot = "Crux: " + str(respuesta) 
            log(bot)
            print("Crux: ",respuesta)
        
            menu_prueba.menu()
main()           
            