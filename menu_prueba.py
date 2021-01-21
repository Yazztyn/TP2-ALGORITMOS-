import facebook_pruebas
import facebook

def menu():

    token = "EAAFvxufavv0BAOh41PazAEmjHaiZAqzEhw8TKVZBZBoBHUc5OvJuK57rkMdlah4VZAui3ZBpsZCLZAjCfCSMvy28wMTagAsoDZBurS9LP6ZAkAjh9AfGovrH1ZCR327y88yqF7Sdi0Sj4S8nZC034pqcukiWSOFbzQArb5MEqRldq57BQPmBvsPjtGw6GD66PgCB4cfOU63vEEA1xygsw08wrnZB"
   
    condicion = True
    
    while condicion:
        # Desplegamos el menú   
        print("""
            1) Buscar usarios
            2) Dar "likes" a posteos
            3) Leer posteos
            4) Subir posteos y fotos
            5) Actualizar un posteo
            6) Listar a los seguidores/amigos
            7) Seguir a un usuario/o solicitar amistad
            8) Enviar mensaje a un usuario
            9) Actualizar datos del perfil
            10) Comentar un posteo
            11) Postear una foto.
            """)

        # Leemos lo que ingresó el usuario
        eligio=input("Seleccione un número: ")

        # Según lo que haya ingresado, le damos lo que pidió
        if eligio== "1":
            print("Usted eligió: Buscar usuarios")
            condicion = False
        elif eligio== "2":
            print("Usted eligió: Dar likes a posteos")
            facebook_pruebas.likear(token)
            condicion = False
        elif eligio== "3":
            print("Usted eligió: Leer posteos")
            condicion = False
        elif eligio== "4":
            print("Usted eligió: Subir posteo")
            mensaje = input("Ingrese e texto que quiere postear: ")
            facebook_pruebas.posteo(token,mensaje)
            condicion = False
        elif eligio == "5":
            print("Usted eligió: Actualizar un posteo")
            condicion = False
        elif eligio == "6":
            print("Usted eligió: Listar a los seguidores/amigos")
            condicion = False
        elif eligio == "7":
            print("Usted eligió: Seguir a un usuario/o solicitar amistad")
            condicion = False
        elif eligio == "8":
            print("Usted eligió: Enviar un mensaje a un usuario")
            condicion = False
        elif eligio == "9":
            print("Usted eligió: Actualizar datos del perfil")
            condicion = False
        elif eligio == "10":
            print("Usted eligió: Comentar un posteo")
            mensaje = input("Ingrese el texto que quiere comentar: ")
            facebook_pruebas.comentar(token,mensaje)
            condicion = False 
        elif eligio == "11":
            facebook_pruebas.postear_foto(token)
        else:
            print("Error: El numero ingresado no es el correcto. Vuelva a intentarlo")