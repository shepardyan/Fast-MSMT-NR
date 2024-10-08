from GraphModule import solvePGM
import numpy as np
import networkx as nx

def read_case(case_path: str):
    graph = np.loadtxt(f"{case_path}/graph.txt")
    src = np.loadtxt(f"{case_path}/src.txt")
    rel = np.loadtxt(f"{case_path}/rel.txt")
    return graph, src, rel

if __name__ == "__main__":
    graph, src, rel = read_case("./data/AreaGK")
    res = solvePGM(graph, src, rel)  # Output the LOLP of nodes. If you want EENS, provide load level data.
    
    G = nx.Graph()
    G.add_edges_from(graph[:, [1, 2]].tolist())
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")


