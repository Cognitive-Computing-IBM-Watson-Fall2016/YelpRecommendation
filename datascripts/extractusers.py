import json
##outfile=open('users.json','w')
##myfile=open('yelp_academic_dataset_user.json')
##types=set()
##categories=set()
##count=0
##pc=10
##for line in myfile:
##    js=json.loads(line)
##    reviews=js["review_count"]
##    if(reviews>=pc):
##        count=count+1
##        outfile.write(json.dumps(js)+'\n')
##myfile.close()
##outfile.close()
##print 'No of reviewers for: ',pc,' reviews is',count
bizfile=open('business.json')
bids=set()
for line in bizfile:
    try :
        js=json.loads(line)
    except ValueError:
        continue
    ids=js["business_id"]
    bids.add(ids)
print '*****************'
bizfile.close()
print '*****************'
c=0
myfile=open('yelp_academic_dataset_review.json')
rfile=open('filtered_reviews.json','w')
for line in myfile:
    js=json.loads(line)
    ids=js["business_id"]
    if ids in bids:
        rfile.write(json.dumps(js)+'\n')
        c=c+1
rfile.close()
print 'No of reviews: ',c
##bizfile=open('restaurant_reviews.json')
##bids=set()
##for line in bizfile:
##    try :
##        js=json.loads(line)
##    except ValueError:
##        continue
##    ids=js["business_id"]
##    bids.add(ids)
##print '*****************'
##bizfile.close()
##print '*****************'
##c=0
##myfile=open('yelp_academic_dataset_tip.json')
##rfile=open('tips.json','w')
##for line in myfile:
##    js=json.loads(line)
##    ids=js["business_id"]
##    if ids in bids:
##        likes=js["likes"]
##        if likes>=0:
##            rfile.write(json.dumps(js)+'\n')
##            c=c+1
##rfile.close()
##print 'No of tips: ',c

        
