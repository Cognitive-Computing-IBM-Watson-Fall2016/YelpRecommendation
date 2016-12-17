import json
import requests
import logging
import time
logging.captureWarnings(True)
rfile=open('part5.json')
wfile=open('personality5.json','w')
js=0
c=0
for r in rfile:
    js=json.loads(r)
    text=js["text"].rstrip()
    try:
        response = requests.post("https://gateway.watsonplatform.net/personality-insights/api/v2/profile",
             auth=("username","password"),
             headers = {"content-type": "text/plain"},
             data=text
             )
    except ValueError:
        continue
    person = json.loads(response.text)
    usr=dict()
    usr['user_id']=js["user_id"]
    usr['personality']=person
    wfile.write(json.dumps(usr)+'\n')
    print json.dumps(person,indent=4,sort_keys=True)
    print c
    print'--------------------------------------------------------------'
    time.sleep(1)
    c=c+1
    if c>100:
        break
