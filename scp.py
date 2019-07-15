import os
import time
import json
import sys
from random import randint as rand
appid = sys.argv[1]
itemname = sys.argv[2]

#print('''curl "https://steamcommunity.com/market/priceoverview/?appid='''+appid+'''&currency=1&market_hash_name=''' + itemname +'''"''')
pricejson = os.popen('''curl "https://steamcommunity.com/market/priceoverview/?appid='''+appid+'''&currency=1&market_hash_name=''' + itemname +'''"''').read() # example Sticker%20|%20Kawaii%20Killer%20Terrorist
#print(pricejson)
pricejson = json.loads(pricejson)
#print("Price is",pricejson["lowest_price"])
#print("=========================================================================")
#print(pricejson["lowest_price"].replace("$",""))
priceincents = pricejson["lowest_price"].replace("$","").replace(".","")
print(priceincents)
