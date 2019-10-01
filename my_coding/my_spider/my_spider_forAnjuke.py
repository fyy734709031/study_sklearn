import request as rq
from lxml import etree
import matplotlib
import re

class spiderForAnjuke(object):
    '''
    https://weifang.anjuke.com/prop/view/A1830357369?from=filter&spread=commsearch_p&uniqid=pc5d74c3fcdfee43.66604440&position=1&kwtype=filter&now_time=1567933436
    https://weifang.anjuke.com/prop/view/A1786689621?from=filter&spread=commsearch_p&uniqid=pc5d74c3fcdff472.24714147&position=3&kwtype=filter&now_time=1567933436
    https://weifang.anjuke.com/prop/view/A1786689621?from=filter&spread=commsearch_p&uniqid=pc5d74c3fcdff472.24714147&position=3&kwtype=filter&now_time=1567933436
    '''
    def __init__(self):
        self.url = "https://bj.fang.anjuke.com/?from=navigation"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "referer": "https://beijing.anjuke.com/sale/?from=navigation"
        }


