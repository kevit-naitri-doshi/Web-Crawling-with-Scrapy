from check_sitemap import *
from spider import *
from helper_func import *
from config import *

create_project_dir(PROJECT_NAME)

sitemap_list=check_sitemap(complete_url)
if len(sitemap_list)>0:
    link=traverse_sitemaps(sitemap_list)
    write_file(f'{PROJECT_NAME}/urls.json',link)
else:
    process= CrawlerProcess()
    process.crawl(MySpider)
    process.start()