#Step 4

import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from matplotlib import pyplot


#pyplot.gca().invert_yaxis()
#pyplot.gca().invert_xaxis()

g = nx.Graph()
g.add_node('Charlotteseville', pos=(38.0673201, -78.4930928)) # 8 Superchargers
g.add_node('Chester', pos = (37.3674726,-77.416648)) # 8 Superchargers
g.add_node('Glen_Allen', pos =(37.6697846, -77.4616425))# 20 superchaergers
g.add_node('Lexington', pos = (37.7973062, -79.4186505)) # 6 Superchargers 
g.add_node('Mt_Jackson', pos = (38.7602417,	-78.6311195))# 8 Superchargers
g.add_node('Norfolk', pos = (36.8605204, -76.2073749)) # 6 superchargers 
g.add_node('Richmond', pos = (37.5280639, -77.3554433)) # 20 superchargers
g.add_node('South_Hill', pos =(36.7483035,	-78.1036949))# 6 Superchargers
g.add_node('Strasburg', pos = (39.0052144, -78.3378302)) # 6 Superchargers
g.add_node('Woodbridge', pos = (38.6408382,	-77.2963031)) #10 Superchargers
g.add_node('Wytheville', pos = (36.9462562, -81.0548087)) #6 Superchargers
#Weighted Nodes
#With Weights Edges 101, 131, 142, 45, 86 (p=5) (-10 to get to the actual Number)
'''
g.add_node('Martinsville', pos =(36.68377756,-79.8654368))
g.add_node('Russell', pos = (36.93363198, -82.09416184))
g.add_node('Gloucester', pos =(37.43738723,	-76.54385427))
g.add_node('Stafford', pos =(38.42248789, -77.46005923))
g.add_node('Prince_William', pos =(38.70453558, -77.48111347))
'''
#UnWeighted Nodes
#Without Weights Edges 12, 113, 133, 30 , 64 (p=5)

g.add_node('Henry', pos =(36.68405319, -79.87400618))
g.add_node('Hampton', pos =(37.05019338,-76.36758735))
g.add_node('Middlesex', pos =(37.63470068, -76.57988891))
g.add_node('Southampton', pos =(36.72649424,-77.10727935))
g.add_node('Norton', pos =(36.94090281,-82.60945802))




nodes = ['Charlotteseville','Chester','Glen_Allen','Lexington','Mt_Jackson','Norfolk','Richmond','South_Hill','Strasburg','Woodbridge','Wytheville']
WeightedNodes = ['Martinsville', 'Russell', 'Gloucester', 'Stafford', 'Prince_William']
NonWeigthedNodes = ['Henry', 'Hampton', 'Middlesex', 'Southampton', 'Norton']
g.add_nodes_from(NonWeigthedNodes)
f = g.add_nodes_from(nodes)

#g=nx.complete_graph()



print("Nodes of graph: ")
print(g.nodes())

g.add_edge('Wytheville','Lexington', distance = 107.4)
g.add_edge('Lexington','Charlotteseville', distance = 53.8)
g.add_edge('Lexington','Mt_Jackson', distance = 79.1)
g.add_edge('Charlotteseville','Mt_Jackson', distance = 48.5)
g.add_edge('Mt_Jackson','Strasburg', distance = 23.1)
g.add_edge('Strasburg','Woodbridge', distance = 61.5)
g.add_edge('Woodbridge','Glen_Allen', distance = 67.7)
g.add_edge('Glen_Allen','Richmond', distance = 11.4)
g.add_edge('Richmond','Chester', distance = 11.6)
g.add_edge('Richmond','Norfolk', distance = 78.2)
g.add_edge('Chester','South_Hill', distance = 57.1)
g.add_edge('Wytheville','South_Hill', distance = 163.7)

''''
#With Weights Edges 101, 131, 142, 45, 86 (p=5) (-10 to get to the actual Number)
#35
g.add_edge('Martinsville', 'Wytheville', distance = 68.24 )
#76
g.add_edge('Martinsville', 'South_Hill', distance = 97.67 )
#91
g.add_edge('Russell', 'Wytheville', distance = 57.40)
#121
g.add_edge('Stafford','Woodbridge', distance = 121.68)
#132
g.add_edge('Stafford','Glen_Allen', distance = 88.78)
g.add_edge('Gloucester','Richmond', distance = 44.93)
g.add_edge('Gloucester','Woodbridge', distance =92.68)
'''

#Without Weights Edges 12, 113, 133, 30 , 64 (p=5)


g.add_edge('Norton','Wytheville',distance =85.84)
g.add_edge('Henry','Wytheville',distance = 67.78)
g.add_edge('Henry','South_Hill',distance = 98.14)
g.add_edge('Southampton','South_Hill',distance = 78.99)
g.add_edge('Southampton','Norfolk',distance = 1.50)
g.add_edge('Middlesex','Glen_Allen', distance = 48.29)
g.add_edge('Middlesex','Hampton', distance = 137.48)
g.add_edge('Hampton','Norfolk', distance =1.50)


pos = {city:(long, lat) for (city, (lat,long)) in nx.get_node_attributes(g, 'pos').items()}
nx.draw(g, pos, with_labels=True, node_size=50)
#red current superchargers
nx.draw_networkx_nodes(g,pos,node_color='r',node_size=50,alpha=0.4)
#Blue new superchargers
print (nx.dijkstra_path(g, 'Wytheville','Woodbridge'))


plt.show()
