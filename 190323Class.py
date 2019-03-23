import requests
import json

token="EAAFDsWZAS5iYBAErQ61de1l1Ge9BzKhn1IOHvZCrHgaRllkfwyc5njZALievlY0YZBoi6NEiK4TmHnZAlNdLYGCPEb26jGeU4RIFsZAwK1rhZAiuyonLuia4FfDaY6kEdkKPS5U8ycWdTgGoUNwxPeZCuAnZCCZBZATBPOkUyfvTqBh1ZAQxssFfwljCm9ZB9Wh1yGIgZD";
data = requests.get("https://graph.facebook.com/me/posts?since=145160640&limit=100&access_token=" + token);
jd = json.loads(data.text);


#print(jd["data"][0]["id"]);

while "paging" in jd:
    print("==========")
    for post in jd["data"]:
        if "message" in post:
            print(post["message"]);
    data = requests.get(jd["paging"]["next"]);
    jd = json.loads(data.text);