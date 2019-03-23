import requests as req
import json

token=“EAAFDsWZAS5iYBAC0O1bZAXVQZAnFQQRi7eWZCMn3GZCtikNJbr1n5vG6ttZCUy0bN6CT441zawvCqWXktzZCIcO2ESlwUTDniGiZAkAWA0549UiXoPh5NhkRVFPWX5lFQ4Jwfpx5bctEYnZAZCh7atkc7K5mizlEeVIq27evgiT7ZAHUFmbZBGzngAMmPJkmNLiLrBAZD”;

data = req.get(“http://graph.facebook.com/me/posts?access_token=” + token);
jd = json.loads(data);

print(data);