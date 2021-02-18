import facebook_crux
import facebook
import instagram_crux
from PIL import Image
import urllib3
from urllib.request import urlopen
import requests

def menu(token):

    continuar = True
    
    while continuar:
        try:
            menu_instagram =  """
                1) Mostrar URL de un posteo.
                2) Mostar informacion de un posteo.
                3) Mostrar cantidad de seguidores.
                4) Mostrar cantidad de seguidos.
                5) Mostar nombre,biografia y URL del perfil.
                6) Mostrar cantidad de posteos.

                """

            menu_facebook = """
                1) Dar "like" a posteo.
                2) Mostrar posteos.
                3) Subir posteo.
                4) Cantidad de seguidores.
                5) Comentar un posteo.
                6) Postear una foto.
                """

            #el usuario elige si facebook o instagram
            print("\n¿Que red social deseda utilizar?\n1- Facebook\n2- Instagram.")
            eleccion_red_social = int(input("\nIngrese el numero de la opcion que desea: "))
            
            if eleccion_red_social == 1:
                print(menu_facebook)
                eligio =int(input("\nIngrese el numero de la opcion que desea: "))

                # Según lo que haya ingresado, le damos lo que pidió
                
                if eligio== 1:
                    
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
                    
                    continuar = False
                
                elif eligio== 2:
                    
                    print("\nUsted eligió: Mostrar posteos.")
                    post = facebook_crux.mostrar_posts(token)
                    
                    posteo = post["posts"]["data"]
                    
                    for diccionario in range(len(posteo)):
                        try:
                            fecha = posteo[diccionario]["created_time"]
                            texto = posteo[diccionario]["message"]
                            print(str(diccionario) + "\t" + texto + "\t\t" + "--Fecha: " + fecha)
                        except KeyError:
                            print(str(diccionario) + "\t" + "Este posteo no tiene ningun texto " + "--Fecha: " + fecha) 
                    continuar = False

                elif eligio== 3:

                    print("\nUsted eligió: Subir posteo.")
                    mensaje = input("Ingrese e texto que quiere postear: ")
                    facebook_crux.posteo(token,mensaje)
                    
                    continuar = False
                
                elif eligio == 4:
                    
                    print("\nUsted eligió: Listar a los seguidores/amigos")
                    continuar = False

                elif eligio == 5:

                    print(" \nUsted eligió: Comentar un posteo")
                    post = facebook_crux.mostrar_posts(token) 
                    posteo = post["posts"]["data"]
                    
                    for diccionario in range(len(posteo) - 3):
                        print(str(diccionario) + ":" + posteo[diccionario]["message"])
                        
                    eleccion_comentar = int(input("\nIngrese el número de posteo que desea comentar: ")) 
                    id = posteo[eleccion_comentar]["id"]
                    mensaje = input("\nIngrese el texto que quiere comentar: ")
                    facebook_crux.comentar(token,mensaje,id)
                    
                    continuar = False 

                elif eligio == 6:
                    
                    print("\nUsted eligió; Postear una foto.")
                    
                    imagen = input("\nIngrese el nombre de la imagen que desea subir (no olvide añadir .jpg o .png): ")

                    mensaje = input("\nIngrese el texto que quiere publicar junto con la foto: ")

                    facebook_crux.postear_foto(token,mensaje,imagen)

                    img = Image.open(imagen,'r')

                    img.show()

                    continuar = False

                while eligio > 6 or not str(eligio).isnumeric():
                    
                    print("\nError: El ingreso no es el correcto. Vuelva a intentarlo")
                    print(menu_facebook)
                    eligio =int(input("\nIngrese el numero de la opcion que desea: "))
            
            
            else:
                
                print(menu_instagram)    
                eligio =int(input("Ingrese el numero de la opcion que desea: "))

                if eligio == 1:
                    
                    print("Usted eligió mostrar URL de un posteo.")
                    id_facebook = instagram_crux.id_pagina(token)
                    id_instagram = instagram_crux.instagram(token,id_facebook)
                    posteos = instagram_crux.media(token,id_instagram)

                    for diccionarios in range(len(posteos)):
                        print((diccionarios) , ":" ,  posteos[diccionarios])
                    eleccion_comentar = int(input("\nIngrese el número de posteo que desea comentar: "))
                    while eleccion_comentar >  len(posteos)-1 or not str(eleccion_comentar).isnumeric():
                        eleccion_comentar = int(input("\nIngrese un número valido: "))
                    id_post = posteos[eleccion_comentar]["id"]
                    print(("Su eleccion fue: ") , id_post )

                    instagram_crux.mostrar_url(token,id_post)

                elif eligio == 2:
                    
                    print("Usted eligió mostrar la información de un posteo.")
                    id_facebook = instagram_crux.id_pagina(token)
                    id_instagram = instagram_crux.instagram(token,id_facebook)
                    posteos = instagram_crux.media(token,id_instagram)

                    for diccionarios in range(len(posteos)):
                        print((diccionarios) , ":" ,  posteos[diccionarios])
                    eleccion_comentar = int(input("\nIngrese el número de posteo que desea comentar: "))
                    while eleccion_comentar >  len(posteos)-1 or not str(eleccion_comentar).isnumeric():
                        eleccion_comentar = int(input("\nIngrese un número valido: "))
                    id_post = posteos[eleccion_comentar]["id"]
                    print(("Su eleccion fue: ") , id_post )

                    instagram_crux.mostrar_mediatype(token,id_post)
                    instagram_crux.mostrar_url(token,id_post)
                    instagram_crux.mostrar_owner(token,id_post)
                    instagram_crux.mostrar_comments(token,id_post)
                    instagram_crux.mostrar_likes(token,id_post)
                    instagram_crux.mostrar_tiempo(token,id_post)

                elif eligio == 3:
                    
                    print("\nUsted eligió mostrar cantidad de seguidores.")
                    id_facebook = instagram_crux.id_pagina(token)
                    id_instagram = instagram_crux.instagram(token,id_facebook)
                    instagram_crux.mostrar_followers(token,id_instagram)

                elif eligio == 4:

                    print("\nUsted eligió mostrar cantidad de seguidos.")
                    id_facebook = instagram_crux.id_pagina(token)
                    id_instagram = instagram_crux.instagram(token,id_facebook)
                    instagram_crux.mostrar_follows(token,id_instagram)

                elif eligio == 5:

                    print("\nUsted eligió mostar nombre,biografia y URL del perfil.")
                    id_facebook = instagram_crux.id_pagina(token)
                    id_instagram = instagram_crux.instagram(token,id_facebook)
                    instagram_crux.mostrar_biografia(token,id_instagram)
                    instagram_crux.mostrar_nombre(token,id_instagram)
                    instagram_crux.mostrar_fotoperfil(token,id_instagram)    

                elif eligio == 6:

                    print("\nUsted eligió mostrar cantidad de posteos.")
                    id_facebook = instagram_crux.id_pagina(token)
                    id_instagram = instagram_crux.instagram(token,id_facebook)
                    instagram_crux.mostrar_mediacount(token,id_instagram)

                while eligio > 6 or not str(eligio).isnumeric():
                    print("Error: El ingreso no es el correcto. Vuelva a intentarlo")
                    print(menu_instagram) 
                    eligio = int(input("Ingrese el numero de la opcion que desea: "))

        except facebook.GraphAPIError or requests.exceptions.ConnectionError or urllib3.exceptions.MaxRetryError or urllib3.exceptions.NewConnectionError or socket.gaierror:

            if facebook.GraphAPIError:
                print("Token de acceso de página incorrecto o expirado.\nIntente ingresando un nuevo token.\nRecuerde que hay una explicacion en README.txt.")
                token = input("Ingrese el nuevo token: ")    

            else:
                print("\n\nError de conexión.\nChequee que tenga conexión a internet e inténtelo nuevamente.")    