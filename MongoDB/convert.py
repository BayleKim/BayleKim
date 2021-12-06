#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json
data = json.load(open("/home/cs143/data/nobel-laureates.json", "r"))
file = open('laureates.import', 'w',encoding='utf-8') 
for i in range(len(data["laureates"])):
    laureate = data["laureates"][i]
    file.write(json.dumps(laureate)+'\n')      # write() method only accept string type data
