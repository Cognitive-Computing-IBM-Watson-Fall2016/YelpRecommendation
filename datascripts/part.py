import json
rfile=open('aggregate_reviews.json')
wfile1=open('part1.json','w')
wfile2=open('part2.json','w')
wfile3=open('part3.json','w')
wfile4=open('part4.json','w')
wfile5=open('part5.json','w')
c=1
for r in rfile:
    js=json.loads(r)
    if c<=100:
        wfile1.write(json.dumps(js)+'\n')
    elif c>100 and c<=200:
        wfile2.write(json.dumps(js)+'\n')
    elif c>200 and c<=300:
        wfile3.write(json.dumps(js)+'\n')
    elif c>300 and c<=400:
        wfile4.write(json.dumps(js)+'\n')
    elif c>400 and c<=500:
        wfile5.write(json.dumps(js)+'\n')
    c=c+1
    if(c>500):
        break
wfile1.close()
wfile2.close()
wfile3.close()
wfile4.close()
wfile5.close()

    
    


