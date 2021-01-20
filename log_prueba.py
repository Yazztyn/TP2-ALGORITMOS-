import time

def log(mensaje):
    #escribir en el archivo de log
    fecha = time.strftime("%d/%m/%y")
    hora = time.strftime("%H:%M:%S")
    with open("archivo.log","a") as otro_archivo:
        otro_archivo.write(fecha + "," + hora +"," + mensaje +"\n") 

def main():
    entrada = input("Usuario: ").lower()
    log("Usuario: " + entrada)
    respuesta = input("Crux: ").lower()
    print("Crux: ",respuesta)
    log("Crux: " + respuesta)        

main()    