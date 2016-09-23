from urllib.request import urlopen
import json
import sys
import datetime
import psycopg2


url = "http://finance.google.com/finance/info?client=ig&q=" + sys.argv[1]
r = urlopen(url)
res = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8').replace("//",""))
print(datetime.date.today())
print(datetime.datetime.utcnow())
print(sys.argv[1])
print(sys.argv[2])
print(res[0]["l"])