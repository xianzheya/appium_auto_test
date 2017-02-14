# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch import helpers
from pprint import pprint

es = Elasticsearch(hosts='l-activity.wap.beta.cn0.qunar.com:9200')
res = es.get(index="vacation", doc_type="vacationDetail", id="_search")
pprint(res)