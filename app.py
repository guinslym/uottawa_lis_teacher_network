import json
import networkx as nx
from networkx.readwrite import json_graph

G=nx.Graph()
#all the nodes form Universities

#all the nodes from Teachers.

canadian_i_school = ['University of Toronto','Dalhousie University', 'University of Western Ontario', 'University of British-Columbia',
		     'University of Alberta','Universite de Montreal', 'University McGill', 'University of Ottawa' ]

toronto = 'University of Toronto'
mcmaster = 'McMaster University'
harvard = 'Harvard University'
dalhousie = 'Dalhousie University'
london = 'University of London'
brighton = 'University of Brighton'
middlesex = 'Middlesex University'
sussex = 'University of Sussex'
guelph = 'University of Guelph'
uwo = 'University of Western Ontario'
alberta = 'University of Alberta'
sfu = 'Simon Fraser University'
sorbonne = 'Universite de la Sorbonne'
montreal = 'Universite de Montreal'
regina = 'University of Regina'
lile = 'Universite Libre de Bruxelles'
acadia = 'Acadia University'
carleton = 'Carleton University'
mcgill = 'University McGill'
ottawa = 'University of Ottawa'
concordia = 'Concordia University'
ubc = 'University of British-Columbia'
queens = "Queen's University"
trent = "Trent University"
dublin = 'Dublin University'
manchester = 'University of Manchester'
michigan = 'University of Michigan'
columbia = 'Columbia University'
cambridge = 'University of Cambridge'
osgoode = 'York University'
dict = {
	'Vellino, Andre': [toronto, london], 
	'Dormann, Claire': [brighton, middlesex],
	'Pare, Daniel J.': [sussex, guelph],
	'Morrison, Heather': [sfu, alberta],
	'Alberts, Inge': [montreal, sorbonne],
	'Cavanagh, Mary': [toronto, uwo, regina],
	'Tom Demsley': [harvard, uwo, mcmaster],
	'Tector, Amy': [lile, uwo, acadia],
	'Schellinck, Jennifer': [carleton, dalhousie],
	'Desormeaux, Monique': [uwo, ottawa],
	'Curran, William': [mcgill, ottawa, concordia, montreal],
	'Kerr, Ian': [alberta, uwo],
	'Bailey, Jane': [toronto, trent, queens],
	'Weir, Leslie': [concordia, mcgill],
	'Bowker, Lynne': [ottawa, dublin, manchester],
	'Scassa, Teresa': [concordia, mcgill, michigan],
	'Horava, Tony': [ottawa, mcgill, carleton],
	'Geist, Michael': [osgoode, cambridge, columbia]
}



items = dict.items()
for k,v in items:
    #sch-middle G.add_edge(k, 'school of information')
    for university in v:
        G.add_edge(k, university)
	#normal.png G.add_edge(k, 'school of information')



for n in G:
    G.node[n]['name'] = n
    if 'versit' in G.node[n]['name']:
        G.node[n]['type'] = 'school'
        G.node[n]['university'] = n
        G.node[n]['color'] = '#7CA721'
	G.node[n]['size'] = 10
    else:
        G.node[n]['type'] = 'teacher'
	G.node[n]['size'] = 6
	G.node[n]['color'] = '#8F4139'
    if G.node[n]['name'] in canadian_i_school:
        G.node[n]['color'] = '#DA991C'
	G.node[n]['mls'] = 'vrai'
	G.node[n]['size'] = 13

d = json_graph.node_link_data(G)
json.dump(d, open('professeurs.json','w'))
print('Wrote node-link JSON data to res_a.json')
print(d)


