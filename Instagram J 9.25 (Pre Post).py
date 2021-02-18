import facebook
import json

def accounts(token):
    """ Pre: Ingresa el token por parámetro
        Post: Devuelve el id de la página de Facebook
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    id_fb= graph.get_object(id = "me",fields = "accounts")
    return(id_fb["accounts"]["data"][0]["id"])
    
def instagram(token,id_facebook):
    """ Pre: Ingresa el token y el id de Facebook por parámetro
        Post: Devuelve el id de Instagram
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    id_ig = graph.get_object(id = id_facebook,fields = "instagram_business_account") 
    return(id_ig["instagram_business_account"]["id"])
    
def media(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Devuelve la id (de un post de Instagram) elegida por el usuario
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    id_post = graph.get_object(id = id_instagram,fields = "media") 
    variable =id_post["media"]["data"]
    for diccionarios in range(len(variable)):
        print((diccionarios) , ":" ,  variable[diccionarios])
    eleccion_comentar = int(input("\nIngrese el número de posteo que desea comentar: "))
    while eleccion_comentar >  len(variable)-1:
        eleccion_comentar = int(input("\nIngrese un número valido: "))
    print(("Su eleccion fue: ") , variable[eleccion_comentar]["id"])
    return variable[eleccion_comentar]["id"]

def mostrar_mediatype(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime el tipo de media
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    media = graph.get_object(id = id_post,fields = "media_type")
    print(media)

def mostrar_url(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime la url de dicho post
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    url = graph.get_object(id = id_post,fields = "media_url")
    print(url)

def mostrar_owner(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime el id de la persona que lo posteó
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    owner = graph.get_object(id = id_post,fields = "owner")
    print(owner)

def mostrar_comments(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime la cantidad de comentarios de dicho post
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comments = graph.get_object(id = id_post,fields = "comments_count")
    print(comments)
    
def mostrar_likes(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime la cantidad de likes de dicho post
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    likes = graph.get_object(id = id_post,fields = "like_count")
    print(likes)
    
def mostrar_tiempo(token,id_post):
    """ Pre: Ingresa el token y el id del post de Instagram por parámetro
        Post: Imprime el tiempo en el que fue posteado
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    tiempo = graph.get_object(id = id_post,fields = "timestamp")
    print(tiempo)
    
def mostrar_followers(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la cantidad de followers que tiene dicho perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    followers = graph.get_object(id = id_instagram,fields = "followers_count")
    print(followers)

def mostrar_follows(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la cantidad de follows que tiene dicho perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    follows = graph.get_object(id = id_instagram,fields = "follows_count")
    print(follows)

def mostrar_biografia(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la biografía que tiene dicho perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    biografia = graph.get_object(id = id_instagram,fields = "biography")
    print(biografia)

def mostrar_nombre(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime el nombre del usuario
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    nombre = graph.get_object(id = id_instagram,fields = "name")
    print(nombre)
    
def mostrar_mediacount(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la cantidad de media que tiene el perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    mediacount = graph.get_object(id = id_instagram,fields = "media_count")
    print(mediacount)
    
def mostrar_fotoperfil(token,id_instagram):
    """ Pre: Ingresa el token y el id del perfil de Instagram por parámetro
        Post: Imprime la url de la foto de perfil
    """
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    fotoperfil = graph.get_object(id = id_instagram,fields = "profile_picture_url")
    print(fotoperfil)
    
def main():
    token="EAAFvxufavv0BAHscCPliGZCAkLZCkxVqg3kHBFZCB37MOatzj4tshMSciBC3hlPxAZCH0XKT30Ef3T3oJUmgkaqZCZAmjPPE8j1a8L2CdK2KEibU1olqVkYCENmkTgWKMaGqih68JN70uK8Hrab7FvOZCSqzrpyL2ivlqT3kGvRAA4lZBagr8schQexiGZAdg5AUZD"
    id_facebook = accounts(token)
    id_instagram = instagram(token,id_facebook)
    id_post = media(token, id_instagram)
    mostrar_mediatype(token,id_post)
    mostrar_url(token,id_post)
    mostrar_owner(token,id_post)
    mostrar_comments(token,id_post)
    mostrar_likes(token,id_post)
    mostrar_tiempo(token,id_post)
    mostrar_followers(token,id_instagram)
    mostrar_follows(token,id_instagram)
    mostrar_biografia(token,id_instagram)
    mostrar_nombre(token,id_instagram)
    mostrar_mediacount(token,id_instagram)
    mostrar_fotoperfil(token,id_instagram)
    
main()