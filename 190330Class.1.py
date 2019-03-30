import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.1111.com.tw/job-bank/job-index.asp?si=1&ss=s&ks=%E5%A4%A7%E6%95%B8%E6%93%9A&page=149');


# 確認是否下載成功
#if r.status_code == requests.codes.ok:
#soup = BeautifulSoup(r.text, "html.parser");
soup = BeautifulSoup(r.text, "lxml");  #pip3 install lxml


while soup.select(".begin") != []:
    for li in soup.select(".halfbox")[0].select("li"):
        a = li.a;
        if str(type(a)) != "<class 'NoneType'>":
            if a["href"].split("/")[5] == "":
                r1 = requests.get("http:" + a["href"]);
                soup1 = BeautifulSoup(r1.text);
                if str(type(soup1.select(".listContent")[0].a)) != "<class 'NoneType'>":
                    a_tag = soup1.select(".listContent")[0].a.extract();
                print(soup1.select(".listContent")[0].string);
                print(soup1.h1.string, soup1.select(".logoSubTitle")[0].string);    
    print("================================================================================")
    url = "https://www.1111.com.tw/job-bank/job-index.asp" + soup.select(".begin")[0]["href"];
    print(url);
    r = requests.get(url);
    soup = BeautifulSoup(r.text, "lxml");
    
