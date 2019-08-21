from igraph import *
import numpy as np
import cairo
from igraph import Graph as IGraph


file_path=open('each_year/most_interactive_merge_2017.csv','r')
content=file_path.readlines()
user_dic={}
index=0
edges=[]
weights=[]
user_names=[]
weight_dic={}
for line in content:
	line_lst=line.split(',')
	user1=line_lst[0]
	user2=line_lst[1]
	if '\n' in line_lst[2]:
		weight=int(line_lst[2][:-1])
	else:
		weight=int(line_lst[2])
	if weight>5:
		if user1 not in user_dic:
			user_dic[user1]=index
			user_names.append(user1)
			index+=1
		if user2 not in user_dic:
			user_dic[user2]=index
			user_names.append(user2)
			index+=1
		edges.append((user_dic[user1],user_dic[user2]))
		weights.append(weight)


# Create the graph
g = Graph(edges=edges)
g.vs["label"]=user_names
g.es["weight"]=weight



community = g.community_multilevel(weights=weights)
# community = g.community_multilevel()
# community = g.community_fastgreedy()
# community = g.community_edge_betweenness(directed=True, weights=weights)
# print g.vs["label"]

group=community.membership

result_community={}
for num in range(0,len(group)):
	if group[num] in result_community:
		result_community[group[num]].append(user_names[num])
	else:
		result_community[group[num]]=[user_names[num]]


communities=result_community.keys()
print result_community
for c in communities:
	print len(result_community[c])
# 	print result_community[c]
# layout = g.layout('kk')
color_list = ['red','blue','green','cyan','yellow','orange','grey','pink','white','black','purple']
colors=[color_list[int(x)] for x in group]
plot(g, vertex_color=colors)


# #=======Got the centralize nodes======#
# btvs = []
# for p in zip(g.vs, g.betweenness()):
#     btvs.append({"label": p[0]["label"], "bt": p[1]})

# # print pgvs
# print sorted(btvs, key=lambda k: k['bt'], reverse=True)[:20]


#[{'bt': 2097.7104849059615, 'label': 'funkywb78'}, {'bt': 1807.48945983875, 'label': 'FashionablyFake'}, {'bt': 1659.7864779390525, 'label': 'GoodGuyNeoNazi'}, {'bt': 1005.8162900015506, 'label': 'street_philatelist'}, {'bt': 623.6697614043655, 'label': 'OxyJay'}, {'bt': 588.0453457879707, 'label': 'GoodGuyNeoNazi'}, {'bt': 516.9406733724276, 'label': 'timbf'}, {'bt': 421.78903536763283, 'label': 'jmkogut'}, {'bt': 398.00456480199824, 'label': 'jmkogut'}, {'bt': 297.98866693404415, 'label': 'Southern_psychonaut'}]


# #=======Got the communities by using Latapy & Pons.======#
# clusters = IGraph.community_walktrap(g, weights="weight").as_clustering()
# # community_walktrap: Community detection algorithm of Latapy & Pons, based on random walks.
# # Pascal Pons, Matthieu Latapy: Computing communities in large networks using random walks, 
# # http://arxiv.org/abs/physics/0512106.
# nodes = [{"label": node["label"]} for node in g.vs]
# community = {}
# for node in nodes:
#     idx = g.vs.find(label=node["label"]).index
#     node["community"] = clusters.membership[idx]
#     if node["community"] not in community:
#         community[node["community"]] = [node["label"]]
#     else:
#         community[node["community"]].append(node["label"])
# for c,l in community.items():
#     print("Community ", c, ": ", l)