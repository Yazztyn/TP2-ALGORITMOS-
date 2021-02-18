import facebook
import json
import time
from PIL import Image

def mostrar_posts(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    posteos = graph.get_object(id = "105670634828356",fields = "posts")
    return posteos

def mostrar_comentario(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comments = graph.get_connections(id='105670634828356_107086578020095', connection_name='comments')
    print(comments)

def comentar(token,mensaje,id):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comment = graph.put_object(parent_object= id, connection_name='comments',message=mensaje)
    print(comment) 

def likear(token,id):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    graph.put_like(object_id=id)
    
    
def posteo(token,mensaje):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    post=graph.put_object(parent_object='me', connection_name='feed',message=mensaje)
    print(post)

def postear_foto(token,mensaje,imagen):    
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    graph.put_photo(image=open(imagen, 'rb'),message=mensaje)
    
def obtener_id(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    id_propio = graph.get_object(id = 'me', fields = 'id')
    return id_propio

