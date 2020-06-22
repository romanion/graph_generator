from CommonGraphGenerator import CommonGraphGenerator
from GraphGenerator import GraphGenerator
import networkx as nx
import matplotlib.pyplot as plt
from GraphParameters import GraphParameters
from GraphUtils import GraphUtils

###################################################################
#Simple Test Program TODO:Unit tests                              #
###################################################################

#common_graph_generator = CommonGraphGenerator()
#generated_common_graph = common_graph_generator.generate_graph()
##common_graph_generator.show()
##common_graph_generator.list_nodes()

#G = GraphGenerator(generated_common_graph)
#g1 = G.generate_graph()
#nx.write_graphml(g1,"graph1.graphml", prettyprint = True)
#print g1.graph
#print "--------------------"
#G.list_nodes()

#utils = GraphUtils()
#utils.post_process_graphml("./graph1.graphml")
#utils.save_file('./graph2.graphml')


common_graph_generator = CommonGraphGenerator(min_no_of_nodes = 3,
                                              max_no_of_nodes = 4)
generated_common_graph = common_graph_generator.generate_graph()

plt.figure(figsize=(10, 10))
# with nodes colored by degree sized by population
nx.draw(generated_common_graph, with_labels=False)
# common_graph_generator.save_nodes_and_edges("./stats.txt")
# common_graph_generator.show()
