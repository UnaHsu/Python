#pip install beautifulsoup4
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body></html>
""";

soup = BeautifulSoup(html , 'html.parser');
#標籤(tag)
print(soup.head);
print(soup.body);
print(soup.a);
print(soup.a.attrs);  #屬性(attrs)
print(soup.a["href"]); #標籤(tag) 屬性(attrs)
print(soup.a.prettify()); #html階層顯示
print(soup.p.string); #標籤(tag)字串顯示
print(soup.select("a")); #Css選擇器 tag 
print(soup.select(".title")); #Css選擇器 class
html ="https//i.gbc.tw/gb_img/s495x660/28555624.jpg";
print(html.split("/"));

