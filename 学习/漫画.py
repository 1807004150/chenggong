import os
import requests
from selenium import webdriver
import time
def mkdir(path):
    '''
    防止目录存在
    '''
    if not os.path.exists(path):
        os.mkdir(path)


def SavePic(filename,url,count):
    '''
    通过requests库
    将抓取到的图片保存到本地
    '''
    content = requests.get(url).content
    
    with open("C:\\Users\\24308\\Desktop\\绝世妖帝\\"+filename+"\\"+str(count)+".png",'wb') as f:
        f.write(content)
    print("下载完成")
def get_TOF(index_url):
    '''
    获取漫画的目录中的每一章节的url连接
    并返回一个字典类型k：漫画名 v：章节链接
    '''
    url_list = []

    # 模拟浏览器并打开网页
    
    browser.get(index_url)
    browser.implicitly_wait(3)

    # 找到漫画标题 并创建目录
    title = browser.title.split('_')[0]
    mkdir(title)

    # 找到漫画章节，注意，漫画可能会有多种篇章
    # 例如番外，正文，短片等等
    comics_lists = browser.find_elements_by_class_name('comic_main_list')

    # 寻找、正文等
    for part in comics_lists:
        # 找到包裹链接的links
        links = part.find_elements_by_tag_name('a')
        # 找到每个单独的章节链接
        for link in links:
            url_list.append(link.get_attribute('href'))

    # 关闭浏览器

    Comics = dict(name=title, urls=url_list)

    return Comics
def get_pic(Comics):
    '''
    打开每个章节的url，
    找到漫画图片的地址，
    并写入到本地
    '''
    comic_list = Comics['urls']

    
    for url in comic_list:
        browser.get(url)
        browser.implicitly_wait(3)

        # 创建章节目录
        dirname =browser.title.split('_')[1]
        mkdir(dirname)

        # 找到该漫画一共有多少页
        for i in range(7):
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3) 
        
        src=(browser.find_elements_by_xpath("//div[1]/img[@*]"))
        count=1
        for i in range(len(src)):
            link=src[i].get_attribute("src")
            SavePic(dirname,link,count)
            count=count+1
            
        
       

    browser.quit()
    print('所有章节下载完毕')
url="https://mm.sfacg.com/"
browser=webdriver.Firefox()
browser.get(url)
class_=browser.find_element_by_xpath("//ul/li[3]/a")
link=class_.get_attribute("href")
browser.get(link)
type_=[]
for count in range(4,8):
    type_.append(browser.find_element_by_xpath(("//ul/li[%d]")%count).text)
for i in range(1,5):
    if i== 1:
        url=link+"\%d"%i
        browser.get(url)
        text_lk=browser.find_element_by_xpath("//ul[1]/a").get_attribute("href")
        comics=get_TOF(text_lk)
        get_pic(comics)
        