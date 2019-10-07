import scrapy
from newscrapy.items import NewscrapyItem 

 
class DemoSpider(scrapy.Spider):
    name="demo"
    allowed_domains=["tainqi.com"]
    start_urls=[]
    citys=["suzhou","taiyuan","xian"]
    for city in citys:
        start_urls.append("http://www.tianqi.com"+"/"+city+"/")
        
    
    
    def parse(self,response):
        items=[]
        week=(response.xpath('//div[@class="day7"]'))
        item=NewscrapyItem ()
        for day in week:#选出其中的兄弟节点
             
             item["date"]=day.xpath('./ul[@class="week"]/li/b/text()').extract()
             item["week"]=day.xpath('./ul[@class="week"]/li/span/text()').extract()
             item["img"]=day.xpath('./ul[@class="week"]/li/img/@src').extract()
             item["weather"]=day.xpath("./ul[@class='txt txt2']/li/text()").extract()
             item["wind"]=day.xpath("./ul[@class='txt']/li/text()").extract()
             te_1=day.xpath("./div[@class='zxt_shuju']/ul/li/b/text()").extract()
             te_2=day.xpath("./div[@class='zxt_shuju']/ul/li/span/text()").extract()
             te=(te_1+te_2)
             print(len(te))
             count=0
             new_list=[]
             for t in te[0:7]:
                 str_1=t+"--"+te[count+7]
                 count=count+1
                 new_list.append(str_1)
             item["temperature"]=new_list
             items.append(item)
        return items