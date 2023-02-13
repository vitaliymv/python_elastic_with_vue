import csv
from io import StringIO
from elasticsearch import Elasticsearch
import re

client = Elasticsearch(hosts=['elasticsearch:9200'], http_auth=('elastic', 'changeme'))

customers = list()
id_es = 0
with open('test.csv', newline='', encoding="utf-8") as csvfile:
    content = csvfile.read().replace('"', '')
    reader = csv.DictReader(StringIO(content), doublequote=False, escapechar='\\')
    for row in reader:
        res = client.index(index="sample-index", id=id_es, body=dict(row))
        customers.append(dict(row))
        id_es += 1


def get_name(dictionary):
    return dictionary['customers_firstname']


def get_date(dictionary):
    if dictionary["customers_date_added"] is None:
        return ''
    return dictionary['customers_date_added']


# sort by customers_firstname
customers.sort(key=get_name)
# sort by customers_date_added
customers.sort(key=get_date)

# all data with .ru
r = re.compile(".*.ru.*")
# all data with start letter S with ignorecase
r_s = re.compile(r"\bS\w+", flags=re.IGNORECASE)
# all email ru
r_email_ru = re.compile(r"([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9_.+-]+\.ru")

for customer in customers:
    try:
        # if len(list(filter(r.match, customer.values()))) != 0:
        #     print(list(filter(r.match, customer.values())))
        # if len(list(filter(r_s.match, customer.values()))) != 0:
        #     print(list(filter(r_s.match, customer.values())))
        if len(list(filter(r_email_ru.match, customer.values()))) != 0:
            print(list(filter(r_email_ru.match, customer.values())))
    except:
        continue

