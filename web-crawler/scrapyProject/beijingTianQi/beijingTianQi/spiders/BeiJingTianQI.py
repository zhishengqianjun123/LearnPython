# -*- coding: utf-8 -*-
import scrapy

from beijingTianQi.items import BeijingtianqiItem


class BeijingtianqiSpider(scrapy.Spider):
    name = 'BeiJingTianQI'
    citys = ['beijing','jinan']
    allowed_domains = ['beijing.tianqi.com']
    start_urls = []
    for city in citys:
        start_urls.append('http://' + city + '.tianqi.com/')

    def parse(self, response):
        subselector = response.xpath('//div[@class="tqshow1"]')
        items = []
        for sub in subselector:
            item = BeijingtianqiItem()
            cityDates = ''
            for cityDate in sub.xpath('./h3//text()').extract():
                cityDates += cityDate

            item['cityDate'] = cityDates
            item['week'] = sub.xpath('./p//text()').extract()[0]
            item['img'] = sub.xpath('./ul/li[1]/img/@src').extract()[0]
            temps = ''
            for temp in sub.xpath('./ul/li[2]//text()').extract():
                temps += temp
            item['temperature'] = temps
            item['weather'] = sub.xpath('./ul/li[3]//text()').extract()[0]
            item['wind'] = sub.xpath('./ul/li[4]//text()').extract()[0]
            items.append(item)
        return items




