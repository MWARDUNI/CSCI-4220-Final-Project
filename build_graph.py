
import networkx as nx
from read_tsvs import TSVLoader

class GraphBuilder():
    def __init__(self) -> None:
        
        return None
    
    def main(self, nodes: dict):
        G = nx.Graph()
        for n in nodes.keys():
            G.add_node(n)
        
        for n, t in nodes.items():
            # print(n, t)
            # print(len(n), len(t))
            for x in t:
                print(x)
                break
            break
            # print(f"{n}\r", end="")
            # for e in t:
            #     G.add_edge(n, t, object=e)


if __name__ == "__main__":
    
    tsv_loader = TSVLoader()
    loaded_file = tsv_loader.main(f"soc-redditHyperlinks-body.tsv")
    gb = GraphBuilder()
    gb.main(loaded_file)