import facebook_pruebas
import facebook
from PIL import Image
def menu():

    token = "EAAFvxufavv0BAI200L66QecH6kS2U4iIZAALGWOKX2UZCXZB2ywwljavScANopFqLBnU81QhAjCrdUZCWYjdtuafAKibmZBDnwnpZB4kw6mIkIayx4zPIs0cAZBMXka4oODMbM5ZAHWrA77L3xhA9Qo3AkVvI3Fbp1Bz1ZAHhtmZBYI4tL5ZB5NRp6uNYxOd5aScUdnGO5ZAXRy3zd93tImLJdHc"
   
    continuar = True
    
    while continuar:
        # Desplegamos el menú   
        print("""
            1) Dar "like" a posteo.
            2) Mostrar posteos.
            3) Subir posteo.
            4) Listar a los seguidores/amigos.
            5) Enviar mensaje a un usuario.
            6) Comentar un posteo.
            7) Postear una foto.
            """)

        # Leemos lo que ingresó el usuario
        eligio=input("Seleccione un número: ")

        # Según lo que haya ingresado, le damos lo que pidió
        if eligio== "1":
            
            print("Usted eligió: Dar likes a posteo.")
            post = facebook_pruebas.mostrar_posts(token) 
            posteo = post["posts"]["data"]
            
            for diccionario in range(len(posteo) - 3):
                print(str(diccionario) + ":" + posteo[diccionario]["message"])
                
            eleccion_likear = int(input("\nIngrese el número de posteo que desea comentar: ")) 
            id = posteo[eleccion_likear]["id"]
            facebook_pruebas.likear(token,id)
            
            continuar = False
        
        elif eligio== "2":
            
            print("Usted eligió: Mostrar posteos.")
            post = facebook_pruebas.mostrar_posts(token)
            
            posteo = post["posts"]["data"]
            
            for diccionario in range(len(posteo) - 3):
                fecha = posteo[diccionario]["created_time"]
                texto = posteo[diccionario]["message"]
                print(str(diccionario) + "\t" + texto + "\t\t" + "--Fecha: " + fecha)
            
            continuar = False

        elif eligio== "3":

            print("Usted eligió: Subir posteo.")
            mensaje = input("Ingrese e texto que quiere postear: ")
            facebook_pruebas.posteo(token,mensaje)
            
            continuar = False
        
        elif eligio == "4":
            
            print("Usted eligió: Listar a los seguidores/amigos")
            continuar = False
            
        elif eligio == "5":

            print("Usted eligió: Enviar un mensaje a un usuario")
            
            continuar = False

        elif eligio == "6":

            print("Usted eligió: Comentar un posteo")
            post = facebook_pruebas.mostrar_posts(token) 
            posteo = post["posts"]["data"]
            
            for diccionario in range(len(posteo) - 3):
                print(str(diccionario) + ":" + posteo[diccionario]["message"])
                
            eleccion_comentar = int(input("\nIngrese el número de posteo que desea comentar: ")) 
            id = posteo[eleccion_comentar]["id"]
            mensaje = input("Ingrese el texto que quiere comentar: ")
            facebook_pruebas.comentar(token,mensaje,id)
            
            continuar = False 

        elif eligio == "7":
            
            print("Usted eligió; Postear una foto.")
            
            imagen = input("Ingrese el nombre de la imagen que desea subir (no olvide añadir .jpg o .png): ")

            mensaje = input("Ingrese el texto que quiere publicar junto con la foto: ")

            facebook_pruebas.postear_foto(token,mensaje,imagen)

            img = Image.open(imagen,'r')

            img.show()

        
            continuar = False

        else:
            print("Error: El ingreso no es el correcto. Vuelva a intentarlo")