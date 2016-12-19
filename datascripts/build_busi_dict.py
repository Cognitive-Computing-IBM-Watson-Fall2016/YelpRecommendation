import sys
import json
import pickle
#cursr.execute("""SELECT * FROM NETWORKS""")

def main():
	busi=set()
	with open('user_per_busi.json', 'r') as fp:
		data = json.load(fp)

	for i in data:
		j=data[i]
		for k in j["Businesses"]:
			busi.add(k)


	with open('reviewd_busi.p', 'wb') as fw:
		pickle.dump(busi, fw)



if __name__ == "__main__":
    main();