import facebook
import json

token="EAAFvxufavv0BAKikiusMALIM0FYNpzGEQZA3GxEEDnngiNTLabHeYkwNn9f7FhunGZArCktGkt1yynt1438aySeFJTZCtaBKOlfoSzU4obG6JP38NigZCIqZCzoOtkfy2wVxJep78gQoI0QdhCdKfHKa0tPByJnLEKMk6I869YHgeWuEqLYHVZBhCovz7JpKGttOpyYsCQDgZDZD"
graph = facebook.GraphAPI(access_token=token, version="2.8")
post = graph.get_object(id='17898838012771448', fields='id,media_type,media_url,owner,timestamp,ig_id,comments_count,like_count,comments')
print(post['media_type'])
print(post['id'])
print(post['media_url'])
print(post['owner'])
print(post['ig_id'])
print(post['comments_count'])
print(post['like_count'])
print(post['timestamp'])
