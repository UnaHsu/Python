import requests
import json

token="EAAFDsWZAS5iYBAGZCo9ZCZCX5UlhVTra3KUafcBriKIf1OrkuAkWZBkBTbr4TqapRsp4VhtzZBKD0ZA2o2qX4mHpd8XHfrr0J8W7DfZBRFKhGUKVucMGFuFCQ5lbFzZBRghvSXUT5s28nTrbXCmOeyM0dpUheMiyfId8k5trv2BvP4LtZBynKt4O2H2nWd9qDOk00ZD";

data = requests.get("https://graph.facebook.com/me/posts?access_token=" + token);
jd = json.loads(data.text);

print(jd[data][0][message]);

for post in jd[data]:
	print(post[id]);

