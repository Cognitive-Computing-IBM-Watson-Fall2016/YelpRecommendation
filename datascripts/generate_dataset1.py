import sys
import json
import pickle
import csv
import random
#cursr.execute("""SELECT * FROM NETWORKS""")

ambience=["casual",
"classy",
"divey",
"hipster",
"intimate",
"romantic",
"touristy",
"trendy",
"upscale"]

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
att="Ambience"
Attribute=[att]
def main():
	
	resW=open('ambience.csv','w')
	rwr=csv.writer(resW, delimiter=',',quoting=csv.QUOTE_MINIMAL)
	rwr.writerow(big5+needs+values+Attribute)

	with open('user_per_busi.json', 'r') as m:
		userMain=json.load(m)

	with open('detailed_busi_dict.json','r') as n:
		busi=json.load(n)

	for i in userMain:
		j1=userMain[i]
		c=j1["Big 5"]+j1["Needs"]+j1["Values"]

		for k in j1["Businesses"]:
			if k in busi:
				j2=busi[k]
				j3=j2["attributes"]
				num='NA'
			
				#if att in j3:
				#	if j3[att]:
				#		num=1
			

				#if att in j3:
				#	if j3[att]=='free':
				#		num=1

				#if att in j3:
				#	num=j3[att]

				if att in j3:
					att_dict=j3[att]
					num=random.choice(ambience)
					for amb in att_dict:						
						if att_dict[amb]:
							num=amb
							break

				rwr.writerow(c+[num])
				
	
	resW.close()


if __name__ == "__main__":
    main();