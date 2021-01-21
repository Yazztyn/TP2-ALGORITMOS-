import facebook
import json
import time

def login(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    app_id = "404375060791037"
    canvas_url = "https://domain.com/that-handles-auth-response/"
    perms = ["manage_pages","publish_pages"]
    fb_login_url = graph.get_auth_url(app_id, canvas_url, perms)
    print(fb_login_url)


def mostrar_comentario(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comments = graph.get_connections(id='105670634828356_107086578020095', connection_name='comments')
    print(comments)

def comentar(token,mensaje):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comment = graph.put_object(parent_object='106233258085979_107833407925964', connection_name='comments',message=mensaje)
    print(comment) 

def likear(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    like = graph.put_like(object_id='105670634828356_108396174555802')
    print(like)
    
def posteo(token,mensaje):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    post=graph.put_object(parent_object='me', connection_name='feed',message=mensaje)
    print(post)

def postear_foto(token):    
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    foto = graph.put_photo(image=open('foto.jpeg', 'rb'),message='FOTON!')
    print(foto)




