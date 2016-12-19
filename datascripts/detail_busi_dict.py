import sys
import json
import pickle
#cursr.execute("""SELECT * FROM NETWORKS""")

def main():
	busi={}
	
	busiset=set()
	with open('user_per_busi.json', 'r') as fp:
		data = json.load(fp)

	for i in data:
		j=data[i]
		for k in j["Businesses"]:
			busiset.add(k)

	for i in busiset:
		busi[i]=[]

	busfi=open('business.json','r')
	for line in busfi:
		try:
			js=json.loads(line)
		except ValueError :
			continue
		name=js["business_id"]
		if name in busi:
			busi[name]=js

	with open('detailed_busi_dict.json','w') as fw:
		json.dump(busi,fw,sort_keys=True, indent=4)


if __name__ == "__main__":
    main();