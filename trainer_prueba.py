def ingreso(frase):    

    with open("trainer.txt", "a") as archivo:
        archivo.write(frase + "\n")
    return archivo

def listar_frases():
    lista = []
    with open("trainer.txt","r") as archivo:
        for linea in archivo:
            lista.append(linea.strip("\n"))        
    return lista 

def main():  

    print("\nBienvenido al trainer de 'Crux'")

    print("\n1- Ingresar palabra o frase nueva.\n2- Ver listado de palabras o frases hasta el momento.\n3- Salir.")

    opcion = input("\nIngrese el numero de la opcion que eligio: ")

    while opcion != "1" and opcion != "2" and opcion != "3":
        
        print("\n¡ERROR!, ingreso equivocado.\n\nIntente nuevamente.")
        
        print("\n1- Ingresar palabra o frase nueva.\n2- Ver listado de palabras o frases hasta el momento.\n3- Salir.")

        opcion = int(input("\nIngrese el numero de la opcion que eligio: "))
    
    if opcion == "1":

        continuar = True

        while continuar:
            
            frase = input("\n\nIngrese la palabra o frase que desea agregar: ")
            ingreso(frase) 
            respuesta = input("\n\nIngrese la palabra o frase que desea que responda el bot: ")
            ingreso(respuesta)
            eleccion = input("\n¿Desea seguir agregando palabras o frases? (Si/No): ").lower()
            
            while eleccion != "si" and eleccion != "no":
                print("\n¡ERROR!, ingreso equivocado.\n\nIntente nuevamente.")
                eleccion = input("\n¿Desea seguir agregando palabras o frases? (Si/No): ").lower()

            if eleccion == "no":
                continuar = False    

    elif opcion == "2":
       
        lista_frases = listar_frases()
        print("\n\nLista de frases y/o palabras:")
        print()
        for frase in lista_frases:
            print(frase)

main()    
