import scrapy
from scrapy.selector import Selector
from patu.items import PatuItem

class JandanPicSpider(scrapy.Spider):
    name = "JandanPic"
    allowed_domains = ["jandan.com", "sinaimg.cn"]
    start_urls = [
        "http://jandan.net/pic"
    ]

    for i in range(7020, 7040):
        start_urls.append("http://jandan.net/pic/page-" + str(i))

    # start_urls = [
    #     "http://www.163.com"
    # ]

    def parse(self, response):
        items=[]
        filename = 'pic_url.txt'
        pic_url = open(filename, 'wb')
        pic_url.write("Start")
        sel = Selector(response)
        pics = sel.xpath('//*[@id="comments"]/ol/li')
        pic_url.write('Version: 0.2')
        for pic in pics:

            ooRate = pic.xpath('div[1]/div/div[2]/*[@class="vote"]/span[2]/text()').extract()
            if len(ooRate) > 0 and int(ooRate[0]) > 150:
                item = PatuItem()
                item['support_rate'] = ooRate[0]
                pic_url.write(str(pic.xpath('div[1]/div/div[2]/p/img/@src').extract()) + '\n')
                if pic.xpath('div[1]/div/div[2]/p/img/@org_src'):
                    item['image_urls'] = pic.xpath('div[1]/div/div[2]/p/img/@org_src').extract()
                else:
                    item['image_urls'] = pic.xpath('div[1]/div/div[2]/p/img/@src').extract()
                item['images'] = ''
                # print(pic.xpath('div[1]/div/div[2]/p/img/@src').extract())
                items.append(item)
                yield item
        
        pic_url.write("End")
        pic_url.close()


class JandanOOXXSpider(scrapy.Spider):
    name = "JandanOOXX"
    allowed_domains = ["jandan.com", "sinaimg.cn"]
    start_urls = [
        "http://jandan.net/ooxx"
    ]

    for i in range(1470, 1492):
        start_urls.append("http://jandan.net/ooxx/page-" + str(i))

    # start_urls = [
    #     "http://www.163.com"
    # ]

    def parse(self, response):
        items=[]
        filename = 'pic_url.txt'
        pic_url = open(filename, 'wb')
        pic_url.write("Start")
        sel = Selector(response)
        pics = sel.xpath('//*[@id="comments"]/ol/li')
        pic_url.write('Version: 0.2')
        for pic in pics:

            ooRate = pic.xpath('div[1]/div/div[2]/*[@class="vote"]/span[2]/text()').extract()
            if len(ooRate) > 0 and int(ooRate[0]) > 100:
                item = PatuItem()
                item['support_rate']=ooRate
                pic_url.write(str(pic.xpath('div[1]/div/div[2]/p/img/@src').extract()) + '\n')
                if pic.xpath('div[1]/div/div[2]/p/img/@org_src'):
                    item['image_urls'] = pic.xpath('div[1]/div/div[2]/p/img/@org_src').extract()
                else:
                    item['image_urls'] = pic.xpath('div[1]/div/div[2]/p/img/@src').extract()
                item['images'] = ''
                # print(pic.xpath('div[1]/div/div[2]/p/img/@src').extract())
                items.append(item)
                yield item
        
        pic_url.write("End")
        pic_url.close()