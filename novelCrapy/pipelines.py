# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class NovelcrapyPipeline:
    def process_item(self, item, spider):
        dir = "C:\\小说\\" + item['novel_topic'] + "\\" + item['novel_name']
        if not os.path.exists(dir):
            os.makedirs(dir)
        filename=dir + "\\" + item['novel_chapter'].replace(" ", "_") + ".txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("".join(item['novel_content']))
        print('ok')
        return item
