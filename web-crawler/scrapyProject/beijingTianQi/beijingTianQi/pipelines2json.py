# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import time


class BeijingtianqiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.json'
        with codecs.open(fileName, 'a', encoding='utf8') as fp:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            fp.write(line)

        return item
