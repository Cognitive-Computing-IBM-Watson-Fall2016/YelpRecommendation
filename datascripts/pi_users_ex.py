import networkx
import pyodbc
import sys
import json
import numpy.linalg
import matplotlib.pyplot as plt
import collections

cnxn = pyodbc.connect('Driver={SQL Server};Server=disengsqlpr1;Database=Columbia;Uid=columbia;Pwd=C_login1;')
cursr = cnxn.cursor()
hops=2
minDist="2"
structStrig="\'MH\'"
structure=["\'MH\'"]
padStruct=[]
facilities=[]
histograms=[]
primes=[2,3,5,7,11,13,17,19,23,29,31,37]
#cursr.execute("""SELECT * FROM NETWORKS""")

def bijectiveMapper(vec):
	count=0
	val=1
	while (count<len(vec)):
		val=val*(primes[count]**vec[count])
		count=count+1
	return val


def addNeighbours(hop, fromFac, grph):
	#print("at AN:",grph is None)
	round=hop
	if round==0:
		return
	else:
		cursr.execute(""" SELECT c.ToFacilityKey,
			c.Id,
			c.ToFacilityType, 
			c.BuiltDate,
			c.Length,
			c.SetCount,
			c.ConductorCount,
			c.ConductorSize,
			c.ConductorMaterial,
			c.InsulationMaterial,
			c.MainServiceIndicator,
			c.UndergroundOverheadIndicator,
			c.PhaseNeutralIndicator
		 from Cables as c
		 join Facilities as A on (c.FromFacilityKey=A.FacilityKey)
		 join Facilities as B on (c.FromFacilityKey=B.FacilityKey)
		 Where 
		 c.FromFacilityKey="""+fromFac""" and c.ToFacilityType in (\'MH\',\'SB\')"""
		 )
		rows=cursr.fetchall()
		#print("Query count", len(rows))
		if rows is None or len(rows)==0:
			return
		else:
			for row in rows:
				#if (not(row.ToFacilityKey in grph.neighbors(fromFac))):
				attributes = {'BuiltDate': row.BuiltDate,
						'Hop':round,
						'Type': row.ToFacilityType,
						'Length': row.Length,
						'Build_Date':row.BuiltDate,
						'SetCount': row.SetCount,
						'ConductorCount': row.ConductorCount,
						'ConductorSize': row.ConductorSize,
						'ConductorMaterial': row.ConductorMaterial,
						'InsulationMaterial': row.InsulationMaterial,
						'MainServiceIndicator': row.MainServiceIndicator,
						'UndergroundOverheadIndicator': row.UndergroundOverheadIndicator,
						'PhaseNeutralIndicator': row.PhaseNeutralIndicator }
				grph.add_edge(fromFac, row.ToFacilityKey, attributes)
				addNeighbours(round-1, row.ToFacilityKey, grph)
			


def main():
	graphs=[]
	i=1
	histnames=['density', 'Eulerian', 'number of edges', 'number of nodes', 'Chordal']
	while i < len(sys.argv):
	    if sys.argv[i] == "--hops":
	        hops = int(sys.argv[i+1])
	        i=i+2
	    elif sys.argv[i] == "--maxDist":
	        minDist = sys.argv[i+1]
	        i=i+2
	    elif sys.argv[i] == "--structures":
	        structStrig = sys.argv[i+1]
	        structure = structStrig.split(',')
	        i=i+2
	    else:
	        print("Invalid argument: "+sys.argv[i])
	        exit(-1)
	 	i=i+1
		
	for s in structure :
		padStruct.append("\'"+s+"\'")

	structStrig=",".join(padStruct)

	cursr.execute("""SELECT distinct top(100) FromFacilityKey from Cables where FromFacilityKey is not null and FromFacilityType in (\'MH\')""")

	for row in cursr.fetchall():
		graphlet=networkx.Graph()
		graphlet.add_node(row.FromFacilityKey)
		addNeighbours(hops, row.FromFacilityKey, graphlet)
		filledGraph=graphlet
		#print(filledGraph is not None)
		if filledGraph is not None and networkx.number_of_edges(filledGraph)>0:
			
			L = networkx.normalized_laplacian_matrix(filledGraph)
			e = numpy.linalg.eigvals(L.A)			
			

			ms_dict=networkx.get_edge_attributes(filledGraph,'MainServiceIndicator')
			pn_dict=networkx.get_edge_attributes(filledGraph,'PhaseNeutralIndicator')
			uo_dict=networkx.get_edge_attributes(filledGraph,'UndergroundOverheadIndicator')
			cm_dict=networkx.get_edge_attributes(filledGraph,'ConductorMaterial')
			im_dict=networkx.get_edge_attributes(filledGraph,'InsulationMaterial')
			bd_dict=networkx.get_edge_attributes(filledGraph,'Build_Date')
			rd_dict=networkx.get_edge_attributes(filledGraph,'Hop')
			ty_dict=networkx.get_edge_attributes(filledGraph,'Type')
			


			bd_list=bd_dict.values()
			bd_list.sort()
			c=collections.Counter(ms_dict.values())
			mains=c.get('M')
			service=c.get('S')
			c=collections.Counter(pn_dict.values())
			phase=c.get('P')
			neutral=c.get('N')
			c=collections.Counter(uo_dict.values())
			under=c.get('U')
			over=c.get('O')
			c=collections.Counter(im_dict.values())
			dom_ins=c.most_common(1)[0][0]
			c=collections.Counter(cm_dict.values())
			dom_cond=c.most_common(1)[0][0]

			sb=[0,0]
			mh=[0,0]

			for k in rd_dict.keys():
				if ty_dict.get(k)=='MH':
					mh[rd_dict.get(k)-1]+=1
				elif ty_dict.get(k)=='SB':
					sb[rd_dict.get(k)-1]+=1



			features={
				'GraphInfo': networkx.info(filledGraph),
				'density': networkx.density(filledGraph),
				'histogram': networkx.degree_histogram(filledGraph),
				'average degree':networkx.average_neighbor_degree(filledGraph),
				'number of edges':networkx.number_of_edges(filledGraph),
				'number of nodes':networkx.number_of_nodes(filledGraph),
				'strong connectedness':networkx.is_strongly_connected(filledGraph),
				#'clustering coeff': cc,
				'eigen values': bijectiveMapper(e.tolist()),
				'eigenkey': bijectiveMapper(e.tolist()),
				'Eulerian': networkx.is_eulerian(filledGraph),
				'Chordal': networkx.is_chordal(filledGraph),
				'No. of Triangles': networkx.triangles(filledGraph),
				'Earliest_Date':bd_list[0],
				'Total_mains':mains,
				'Total_neutral': neutral,
				'Total_phase':phase,
				'Total_service': service,
				'Total_underground':under,
				'Total_over':over,
				'Dominant_Insulator':dom_ins,
				'Dominant_Conductor':dom_cond,
				'Service Box Hop 1': sb[0],
				'Service Box Hop 2': sb[1],
				'Manhole Hop 1': mh[0],
				'Manhole Hop 2': mh[1]
			}
			graphs.append(features)

	    
	with open('features2.json', 'w') as f:
    		json.dump(graphs, f)		

	print len(graphs)
	#collating full features
	for s in histnames:
		print s
		t_feature=[o.get(s) for o in graphs]
		plt.figure()
		plt.hist(t_feature)
		plt.title('HISTOGRAM OF '+s)
		plt.xlabel(s)			
		plt.ylabel('no. of structures')
		plt.savefig('.\\'+s+'_hist.jpg')	
		plt.close()



	cnxn.close()



if __name__ == "__main__":
    main();