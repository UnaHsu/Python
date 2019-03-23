import requests
import json
import jieba

corpus = [];
token="EAAFDsWZAS5iYBAI3pDLFB9V4J0iub9sa8sXp07yol54fluCWtHURIQGE4E64gspLxZAwuICaQGQaawOChzDvvEmTNmT1sQg0FzXopKBGP0MIDwzkQQM0h6KZAWD79pWZAz8ZCTSZAstzp4T8VgZBk5waRVx6HdsIpeGShRET4kNL5wVhtZCO4qyBEf66XKSdZC6Gknbisk1siwgZDZD";
data = requests.get("https://graph.facebook.com/me/posts?since=145160640&limit=100&access_token=" + token);
jd = json.loads(data.text);


#print(jd["data"][0]["id"]);

while "paging" in jd:
    print("==========")
    for post in jd["data"]:
        if "message" in post:
            corpus += jieba.cut(post["message"]);
        	#print(post["message"]);
			#print("，".join(jieba.cut(post["message"])));	

    data = requests.get(jd["paging"]["next"]);
    jd = json.loads(data.text);

dic = {};
for ele in corpus:
    if ele not in dic:
        dic[ele] = 1;
    else:
        dic[ele] += 1;

for ele in dic.items():
    if len(ele[0]) >= 2:
        print(ele[0], ele[1]);