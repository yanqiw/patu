# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from patu import settings
import requests
import os

class PatuPipeline(object):
    def process_item(self, item, spider):
        print '-----------pipeline-------------'
        if 'image_urls' in item:
            
            images = []
            dir_path = '%s/%s' % (settings.FILES_STORE, spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for image_url in item['image_urls']:
            	print image_url
                us = image_url.split('/')[3:]
                image_file_name = str(item['support_rate']) + '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images

        return item    
        

    