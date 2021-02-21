import facebook
import json
    
def instagram(token):
    """ Pre: Ingresa el token y el id de Facebook por parámetro
        Post: Devuelve el id de Instagram
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    id_ig = graph.get_object(id = "me",fields = "instagram_business_account") 
    id = id_ig["instagram_business_account"]["id"]
    return id 
    
def media(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Devuelve un diccionario con ids de publicaciones de instagram
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    post = graph.get_object(id = id_instagram,fields = "media") 
    posteos = post["media"]["data"]
    return posteos

def mostrar_mediatype(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime el tipo de media
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    media = graph.get_object(id = id_post,fields = "media_type")
    print("\nEl tipo de posteo es: ",media["media_type"])

def mostrar_url(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime la url de dicho post
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    url = graph.get_object(id = id_post,fields = "media_url")
    print("\nLa URL del post que eligió es: ",url["media_url"])

def mostrar_owner(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime el id de la persona que lo posteó
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    owner = graph.get_object(id = id_post,fields = "owner")
    print("\nEl id del dueño del post es: ",owner["owner"]["id"])

def mostrar_comments(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime la cantidad de comentarios de dicho post
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comments = graph.get_object(id = id_post,fields = "comments_count")
    print("\nLa cantidad de comentarios en el posteo son: ",comments["comments_count"])
    
def mostrar_likes(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime la cantidad de likes de dicho post
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    likes = graph.get_object(id = id_post,fields = "like_count")
    print("\nLa cantidad de likes en el posteo es: ",likes["like_count"])
    
def mostrar_tiempo(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime el tiempo en el que fue posteado"
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    tiempo = graph.get_object(id = id_post,fields = "timestamp")
    print("\nLa fecha de publicación es: ",tiempo["timestamp"])
    
def mostrar_followers(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la cantidad de followers que tiene dicho perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    followers = graph.get_object(id = id_instagram,fields = "followers_count")
    print("\nLa cantidad de seguidores es: ",followers["followers_count"])

def mostrar_follows(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la cantidad de follows que tiene dicho perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    follows = graph.get_object(id = id_instagram,fields = "follows_count")
    print("\nLa cantidad de seguidos es: ",follows["follows_count"])

def mostrar_biografia(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la biografía que tiene dicho perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    biografia = graph.get_object(id = id_instagram,fields = "biography")
    print("\nLa biografia es: ",biografia["biography"])

def mostrar_nombre(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime el nombre del usuario
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    nombre = graph.get_object(id = id_instagram,fields = "name")
    print("\nEl nombre de usuario es: ",nombre["name"])
    
def mostrar_mediacount(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la cantidad de media que tiene el perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    cantidad_publicaciones = graph.get_object(id = id_instagram,fields = "media_count")
    print("\nLa cantidad de publicaciones es: ", cantidad_publicaciones["media_count"])
    
def mostrar_fotoperfil(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la url de la foto de perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    fotoperfil = graph.get_object(id = id_instagram,fields = "profile_picture_url")
    print("\nLa URL de la foto de perfil es: ",fotoperfil["profile_picture_url"])
    
   
