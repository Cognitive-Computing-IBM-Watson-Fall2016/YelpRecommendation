import sys
import json
#cursr.execute("""SELECT * FROM NETWORKS""")

def main():
	names={}
	with open('cust_busi.json', 'r') as fp:
		data = json.load(fp)

	for i in range(1,6):
		perfile=open('personality'+str(i)+'.json')
		for line in perfile:
			try:
				js=json.loads(line)
			except ValueError :
				continue
			name=str(js["user_id"])
			d={}
			d["Businesses"]=data[name]
			d["Big 5"]=[]
			for a in range(0,5):
				d["Big 5"].append(js['personality']['tree']['children'][0]['children'][0]['children'][a]['percentage'])
			d["Values"]=[]
			for b in range(0,5):
				d["Values"].append(js['personality']['tree']['children'][2]['children'][0]['children'][b]['percentage'])
			d["Needs"]=[]
			for c in range(0,12):
				d["Needs"].append(js['personality']['tree']['children'][1]['children'][0]['children'][c]['percentage'])
			names[name]=d
		perfile.close()	

	with open('user_per_busi.json', 'w') as fw:
		json.dump(names, fw, sort_keys=True, indent=4)



if __name__ == "__main__":
    main();