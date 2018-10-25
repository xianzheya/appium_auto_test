# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch import helpers
from pprint import pprint

es = Elasticsearch(hosts='')
res = es.get(index="vacation", doc_type="vacationDetail", id="_search")
pprint(res)
