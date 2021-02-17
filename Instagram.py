import facebook
import json
    
def mostrar_mediatype(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    media = graph.get_object(id = "17898838012771448",fields = "media_type")
    print(media)

def mostrar_url(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    url = graph.get_object(id = "17898838012771448",fields = "media_url")
    print(url)

def mostrar_owner(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    owner = graph.get_object(id = "17898838012771448",fields = "owner")
    print(owner)

def mostrar_comments(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    comments = graph.get_object(id = "17898838012771448",fields = "comments_count")
    print(comments)
def mostrar_likes(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    likes = graph.get_object(id = "17898838012771448",fields = "like_count")
    print(likes)
def mostrar_tiempo(token):
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    tiempo = graph.get_object(id = "17898838012771448",fields = "timestamp")
    print(tiempo)


def main():
    token="EAAFvxufavv0BAGmrQfWm3Yq71QlNM4XYIMYVz4ZCctqCc1LXgKLX04noguBWyWAAr6nJaskMJ4Gy7ekmp5CVlyHaRfZBzZB0cqZC1LOHpHmqry1ZAQL3zH6643SU1dgtc6BuDpZC0IKGEDrOt3QqZCqjAaGgSdvGH00gsu5ZB1QZBnPtu4vyLbdleM0aXU8cHPnwZD"
    mostrar_mediatype(token)
    mostrar_url(token)
    mostrar_owner(token)
    mostrar_comments(token)
    mostrar_likes(token)
    mostrar_tiempo(token)
   
    
  
    
    
main()