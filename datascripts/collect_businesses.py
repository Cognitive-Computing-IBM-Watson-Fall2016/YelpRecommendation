import sys
import json
#cursr.execute("""SELECT * FROM NETWORKS""")

def main():
	res={}
	usf=open("uids.txt","r")
	c=0
	for line in usf:
		res[str(line.rstrip('\n'))]=[]
	usf.close()
	rvs=open("filtered_reviews.json","r")
	for line in rvs:
		c=c+1
		print(c*100/1630660)
		js=json.loads(line)
		u=js["user_id"]
		if js["user_id"] in res:
			if int(js["stars"]>2):
				res[js["user_id"]].append(js["business_id"])

	rvs.close()

	with open("cust_busi.json","w") as f:
		json.dump(res,f)









if __name__ == "__main__":
    main();