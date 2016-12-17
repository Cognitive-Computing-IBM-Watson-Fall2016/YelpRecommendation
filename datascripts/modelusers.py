import json
rfile=open('filtered_reviews.json')
wfile=open('aggregate_reviews.json','w')
ans=dict()
c=0
c1=0
userset=dict()
for r in rfile:
    c=c+1
    js=json.loads(r)
    user=js["user_id"]
    bid=js["business_id"]
    text=js["text"]
    if ans.has_key(user):
        if userset.has_key(user):
            continue
        val=ans.get(user)
        val['text']=val.get('text')+' '+text
        val['wcount']=len(val.get('text').split())
        ans[user]=val
        if val.get('wcount')>600:
            userset[user]="p"
            wr=dict()
            wr['user_id']=user
            wr['text']=val['text']
            wr['business_id']=val['business_id']
            wfile.write(json.dumps(wr)+'\n')
            c1=c1+1
    else:
        val=dict()
        val['text']=text
        val['business_id']=bid
        val['wcount']=len(val['text'].split())
        ans[user]=val
    print c
    if c>50000:
        break
    
wfile.close()
print '################'
print c1
print '################'

rfile.close()
print '***********************'
