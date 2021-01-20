import facebook
import json
import time


def mostrar_comentario():
    graph = facebook.GraphAPI(access_token="EAAFvxufavv0BAIH4Hol4KiZBGfFe8EYgyP91J76vKLXRLArhQmCwLMd982r3D8tXryqEpJ1vFbGVfoZA8bsCo58KyYve5IZCP5RXbBqudYtP6xxZAHzHryNtRtiFJxHPgJXNZC7L7XUAp07LELolox1ZBA6NT5fROuUXP7odMfgrTkZCZAnULi4uz7CkbnsxJaR0dH5X1aHGpqsS5l0A9yok", version="2.8")
    comments = graph.get_connections(id='105670634828356_107086578020095', connection_name='comments')
    print(comments)

def comentar():
    graph = facebook.GraphAPI(access_token="EAAFvxufavv0BAIH4Hol4KiZBGfFe8EYgyP91J76vKLXRLArhQmCwLMd982r3D8tXryqEpJ1vFbGVfoZA8bsCo58KyYve5IZCP5RXbBqudYtP6xxZAHzHryNtRtiFJxHPgJXNZC7L7XUAp07LELolox1ZBA6NT5fROuUXP7odMfgrTkZCZAnULi4uz7CkbnsxJaR0dH5X1aHGpqsS5l0A9yok", version="2.8")
    comment = graph.put_object(parent_object='105670634828356_108396174555802', connection_name='comments',message='Soy Juli comentando')
    print(comment) 

def likear():
    graph = facebook.GraphAPI(access_token="EAAFvxufavv0BAIH4Hol4KiZBGfFe8EYgyP91J76vKLXRLArhQmCwLMd982r3D8tXryqEpJ1vFbGVfoZA8bsCo58KyYve5IZCP5RXbBqudYtP6xxZAHzHryNtRtiFJxHPgJXNZC7L7XUAp07LELolox1ZBA6NT5fROuUXP7odMfgrTkZCZAnULi4uz7CkbnsxJaR0dH5X1aHGpqsS5l0A9yok", version="2.8")
    like = graph.put_like(object_id='105670634828356_108396174555802')
    print(like)
    
def posteo():
    graph = facebook.GraphAPI(access_token="EAAFvxufavv0BAIH4Hol4KiZBGfFe8EYgyP91J76vKLXRLArhQmCwLMd982r3D8tXryqEpJ1vFbGVfoZA8bsCo58KyYve5IZCP5RXbBqudYtP6xxZAHzHryNtRtiFJxHPgJXNZC7L7XUAp07LELolox1ZBA6NT5fROuUXP7odMfgrTkZCZAnULi4uz7CkbnsxJaR0dH5X1aHGpqsS5l0A9yok", version="2.8")
    post=graph.put_object(parent_object='me', connection_name='feed',message='Holaa soy Juli posteando algo.')
    print(post)

def postear_foto():    
    graph = facebook.GraphAPI(access_token="EAAFvxufavv0BAIH4Hol4KiZBGfFe8EYgyP91J76vKLXRLArhQmCwLMd982r3D8tXryqEpJ1vFbGVfoZA8bsCo58KyYve5IZCP5RXbBqudYtP6xxZAHzHryNtRtiFJxHPgJXNZC7L7XUAp07LELolox1ZBA6NT5fROuUXP7odMfgrTkZCZAnULi4uz7CkbnsxJaR0dH5X1aHGpqsS5l0A9yok", version="2.8")
    foto = graph.put_photo(image=open('foto.jpeg', 'rb'),message='FOTON!')
    print(foto)


