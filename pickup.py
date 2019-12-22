import requests
from bs4 import BeautifulSoup

file_name='test_html.htm'
save_name='test_html_a.txt'

f=open(file_name, encoding='UTF-8')
html=f.read()
f.close()

f2=open(save_name,'w',encoding='UTF-8')

soup = BeautifulSoup(html,"html.parser")


#dataにクラスを指定する
data=soup.find_all("span",class_="sf3b2")


# 配列に格納された値をfor文とprint文で出力
for item in data:
    print("------------")
    print(item.getText())


############↑とりあえず変更が全くないところの文字列のみ抜き出している


