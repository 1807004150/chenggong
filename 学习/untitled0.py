from bs4 import BeautifulSoup
import requests
def get_url(url):
    try:
        r=requests.get(url,timeout=30)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "ERROR"
def get_content(url):
    url_list=[]
    html=get_url(url)
    soup=BeautifulSoup(html,"lxml")
    find_list1=soup.find_all("div",class_="index_toplist mright mbottom")
    find_list2=soup.find_all("div",class_="index_toplist  mbottom")
    for item in find_list1:
       name=item.find("div",class_="toptab").span.string
       with open("noval_list.txt","a+") as f:
           f.write("小说种类:{}\n".format(name))
       books=item.find("div",style="display: block;")
       book_list=books.find_all("li")
       for book in book_list:
           link=url+book.a["href"]
           title=book.a["title"]
           url_list.append(link)
           with open("noval_list.txt","a+") as f:
               f.write("小说名：{:<} \t 小说链接：{:<} \n ".format(title,link))
    for item in find_list2:
       name=item.find("div",style="display: block;").span.string
       with open("noval_list.txt","a+") as f:
           f.write("小说种类:{}\n".format(name))
       books=item.find_all("div",class_="topbooks")
       book_list=books.find_all("li")
       for book in book_list:
           link=url+book.a["href"]
           title=book.a["title"]
           url_list.append(link)
           with open("noval_list.txt","a+") as f:
               f.write("小说名：{:<} \t 小说链接：{:<} \n".format(title,link)) 
    return url_list

def get_text(url,url_list1):
    url_list=[]
    html=get_url(url)
    soup=BeautifulSoup(html,"lxml")
    item=soup.find_all("dd")
    text_name=soup.find("h1").text
    writer=soup.find("div",id="info").p.text
    text_name1=text_name+"--------"+writer
    with open("/Users/24308/Desktop/小说/{}.txt".format(text_name1),"a+",encoding='utf-8') as f:
        f.write("小说标题：{} \n".format(text_name1))
    for link in item:
        url_list.append(url_list1+link.a["href"])
    return url_list,text_name1
def get_one_txt(url,text_name):
    html=get_url(url)
    soup=BeautifulSoup(html,"lxml")
    try:
        txt1 = soup.find('div', id='content').text.replace("chaptererror();","")
        title = soup.find('title').text
        print(txt1)
        print("\n",title)
        print("\n",type(title))
        txt1=str(txt1)
        print("\n",type(txt1))
        print(txt1)
        with open('C:\\Users\\24308\\Desktop\\小说\\{}.txt'.format(text_name), "a+",encoding='utf-8') as fw:#没将encoding设为文件的encoding
            fw.write("{:<15}".format(txt1))
        print('当前小说：{} 当前章节{} 已经下载完毕'.format(text_name, title))
    except:
        print('someting wrong')

url="http://www.qu.la/"
url_list1=get_content(url)   
count=0

for link in url_list1:
    if count==0:
     url_list2,text_name=get_text(link,url_list1[0])
    count=count+1
count1=1
for url in url_list2:
    if count1==1:
        print(url)
        get_one_txt(url,text_name)
    count1=count1+1    
