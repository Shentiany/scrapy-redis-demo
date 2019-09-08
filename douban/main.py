
import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","yjspider","-o","yj.csv"])
# execute(["scrapy","crawl","cnki","-s","LOG_FILE=lunwen.log"])
# execute(["scrapy","crawl","movie"])
execute(["scrapy", "crawl", "movie", "-o", "movie.csv"])


