<h1 align="center">scrapy-redis-demo</h1>
<p align="center">
    <em>✨以豆瓣电影top250为例</em>
</p>

## 准备工作
1. 下载安装redis
2. [下载](https://github.com/rmax/scrapy-redis) src下的scrapy-redis
3. 安装redis、scrapy-redis
```bash
pip install redis
pip install scrapy-redis
```
## 修改
1. 在settings中添加:
```python
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
```
2. 修改spider:
```python
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
    name = 'myspider'

    def parse(self, response):
        # do stuff
        pass
```
## 运行
```bash
redis-cli lpush myspider:start_urls http://google.com
```
