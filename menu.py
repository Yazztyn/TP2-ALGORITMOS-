def menu():
    condicion = "True"   
    while condicion == "True":
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
            
            """)

        # Leemos lo que ingresó el usuario
        eligio=input("Seleccione un número: ")

        # Según lo que haya ingresado, le damos lo que pidió
        if eligio== "1":
            print("Usted eligió: Buscar usuarios")
            condicion = "False"
        elif eligio== "2":
            print("Usted eligió: Dar likes a posteos")
            condicion = "False"
        elif eligio== "3":
            print("Usted eligió: Leer posteos")
            condicion = "False"
        elif eligio== "4":
            print("Usted eligió: Subir posteos y fotos")
            condicion = "False"
        elif eligio == "5":
            print("Usted eligió: Actualizar un posteo")
            condicion = "False"
        elif eligio == "6":
            print("Usted eligió: Listar a los seguidores/amigos")
            condicion = "False"
        elif eligio == "7":
            print("Usted eligió: Seguir a un usuario/o solicitar amistad")
            condicion = "False"
        elif eligio == "8":
            print("Usted eligió: Enviar un mensaje a un usuario")
            condicion = "False"
        elif eligio == "9":
            print("Usted eligió: Actualizar datos del perfil")
            condicion = "False"
        else:
            print("Error: El numero ingresado no es el correcto. Vuelva a intentarlo")
menu()