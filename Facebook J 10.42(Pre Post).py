import facebook
import json
import time
from PIL import Image

def mostrar_posts(token):
    """ Pre: Ingresa el token por parámetro
        Post: Devuelve el posteo
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    posteos = graph.get_object(id = "105670634828356",fields = "posts")
    return posteos

def mostrar_comentario(token):
    """ Pre: Ingresa el token por parámetro
        Post: Imprime los comentarios del posteo elegido
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comments = graph.get_connections(id='105670634828356_107086578020095', connection_name='comments')
    print(comments)

def comentar(token,mensaje,id):
    """ Pre: Ingresa el token,el mensaje que desea el usuario y el id del post por parámetro
        Post: Comenta el post con lo que el usuario ingresó
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comment = graph.put_object(parent_object= id, connection_name='comments',message=mensaje)
    print(comment) 

def likear(token,id):
    """ Pre: Ingresa el token y el id del post por parámetro
        Post: Likea el post 
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    graph.put_like(object_id=id)
    
    
def posteo(token,mensaje):
    """ Pre: Ingresa el token y el mensaje que acompaña el mismo por parámetro
        Post: Publica un estado en Facebook
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    post=graph.put_object(parent_object='me', connection_name='feed',message=mensaje)
    print(post)

def postear_foto(token,mensaje,imagen):
    """ Pre: Ingresa el token, un mensaje y una imagen por parámetro
        Post: Publica una foto con un mensaje en Facebook
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    foto = graph.put_photo(image=open(imagen, 'rb'),message=mensaje)
    
def obtener_id(token):
    """ Pre: Ingresa el token por parámetro
        Post: Devuelve el ID de la persona misma
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    id_propio = graph.get_object(id = 'me', fields = 'id')
    return id_propio

# def main():
#     token = "EAAFvxufavv0BAJnIyPLGgQbGoE9ZCTYOH6WOEgYLSL6jJaGKOGESvzOKV6J2jtRbVZCkkHusKZBQ9duCwqZAOsv6iTfxl5T8fGGtWcjeob2DbT2T9jTUFLzmJholsQ1QZAZBv07YddJIgcmKjZCHOhAQg1jBeDVT9cnKzGyKQ96VG1stVOrRsrajUdxle82Ehsj8Ln96c6zoQZDZD"
#     print(obtener_id(token))


# main()    