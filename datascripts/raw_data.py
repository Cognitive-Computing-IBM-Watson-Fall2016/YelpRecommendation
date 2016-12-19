import sys
import json
import pickle
import csv
import random
#cursr.execute("""SELECT * FROM NETWORKS""")

big5=['Openness',
'Conscientiousness',
'Extraversion',
'Agreeableness',
'Neuroticism'
]
values=[
'Conservation',
'Openness to change',
'Hedonism',
'Self-enhancement',
'Self-transcendence'
]
needs=['Challenge',
'Closeness',
'Curiosity',
'Excitement',
'Harmony',
'Ideal',
'Liberty',
'Love',
'Practicality',
'Self-expression',
'Stability',
'Structure'
]

def main():
	
	resW=open('raw.csv','w')
	rwr=csv.writer(resW, delimiter=',',quoting=csv.QUOTE_MINIMAL)
	rwr.writerow(big5+needs+values)

	with open('user_per_busi.json', 'r') as m:
		userMain=json.load(m)

	with open('detailed_busi_dict.json','r') as n:
		busi=json.load(n)

	for i in userMain:
		j1=userMain[i]
		c=j1["Big 5"]+j1["Needs"]+j1["Values"]
		rwr.writerow(c)
				
	
	resW.close()


if __name__ == "__main__":
    main();