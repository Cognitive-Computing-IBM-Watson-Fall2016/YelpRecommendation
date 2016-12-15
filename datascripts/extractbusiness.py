import json
outfile=open('business.json','w')
myfile=open('yelp_academic_dataset_business.json')
types=set()
categories=set()
count=0
cities=set()
pc=0
for line in myfile:
    js=json.loads(line)
    type=js["type"]
    category=js["categories"]
    reviews=js["review_count"]
    city=js["city"]
    cities.add(city)
    for c in category:
        if c.lower()=='restaurants':
            count=count+1
            id=js["business_id"]
            outfile.write(json.dumps(js)+'\n')
            if pc<4:
##                    print json.dumps(js)
                att=js["attributes"]
                print json.dumps(js)
##                    print json.dumps(att)
                print '***************************************************'
                pc=pc+1
            break
        categories.add(c)
    types.add(type)

print 'No of restaurants in Pittsburg with reviews: ',count
    
