import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3])

H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_node(H)

G.add_edge(1,2)
e = (2,3)
G.add_edge(*e)
G.add_edges_from([(1,2), (1,3)])

G.add_edges_from(H.edges)

G.add_edge(1,3)
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print(list(G.nodes))
print(list(G.edges))
print(list(G.adj[1]))  # or list(G.neighbors(1))
print(G.degree[1])  # the number of edges incident to 1

G.remove_node(2)
G.remove_nodes_from("spam")
G.remove_edge(1,3)

G.clear()

G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print(list(nx.connected_components(G)))
print(sorted(d for n, d in G.degree()))
print(nx.clustering(G))