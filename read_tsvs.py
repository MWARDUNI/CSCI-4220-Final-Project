import csv
import pandas as pd
import networkx as nx
from pyvis.network import Network
import io


class TSVLoader():
    def __init__(self) -> None:
        self.prop_map = self._read_prop_map()
        self.test = False

    def _read_prop_map(self) -> list:
        try:
            with open("props_mapping/props_map.csv", "r") as props_file:
                reader = csv.reader(props_file)
                for line in reader:
                    return line
        except FileNotFoundError:
            print("props_map.csv not found. Generating it now...")
            generate_props_map("source/post_props.csv", "props_mapping/props_map.csv")
            return self._read_prop_map()
        except Exception as e:
            print(f"Error reading props_map.csv: {e}")
            return []



    def load_data(self, file) -> dict:
        reddit = {}
        try:
            # Decode binary file-like object from Streamlit
            if hasattr(file, "read"):
                file = io.TextIOWrapper(file, encoding="utf-8")

            reader = csv.reader(file if isinstance(file, str) else file, delimiter="\t")
            for idx, line in enumerate(reader):
                print(f"Row {idx}: {line}")  # Debug: Print each row
                if idx == 0 or len(line) < 2:  # Skip header and invalid rows
                    continue
                source = line[0]
                target = line[1]
                post_id = line[2] if len(line) > 2 else None
                ts = line[3] if len(line) > 3 else None
                sentiment = line[4] if len(line) > 4 else None
                props = line[5] if len(line) > 5 else ""
                if source not in reddit.keys():
                    reddit[source] = []
                reddit[source].append({
                    "target": target, 'post_id': post_id, 'ts': ts, 
                    "sentiment": sentiment,
                    "props": {self.prop_map[i]: x for i, x in enumerate(props.split(","))}
                })
        except Exception as e:
            print(f"Error processing file: {e}")
        return reddit


    def to_dataframe(self, reddit_data: dict) -> pd.DataFrame:
        rows = []
        for source, posts in reddit_data.items():
            for post in posts:
                row = {
                    "source": source,
                    "target": post["target"],
                    "post_id": post["post_id"],
                    "timestamp": post["ts"],
                    "sentiment": post["sentiment"],
                }
                row.update(post["props"])  # Add the properties as individual columns
                rows.append(row)
        return pd.DataFrame(rows)

    def to_networkx_graph(self, reddit_data: dict) -> nx.DiGraph:
        graph = nx.DiGraph()
        for source, posts in reddit_data.items():
            for post in posts:
                graph.add_edge(source, post["target"], post_id=post["post_id"],
                               timestamp=post["ts"], sentiment=post["sentiment"],
                               **post["props"])
        return graph

    def pyvis_visualizer(self, graph: nx.DiGraph, outfile: str = "graph.html"):
        net = Network(notebook=True, directed=True, cdn_resources="in_line")
        for node in graph.nodes:
            net.add_node(node, label=node)

        for source, target, data in graph.edges(data=True):
            label = f"Sentiment: {data['sentiment']}"
            net.add_edge(source, target, label=label)

        net.show(outfile)

def generate_props_map(input_file: str, output_file: str):
    columns = []
    with open(input_file, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=".")
        for line in reader:
            columns.append(line[1].strip())
    
    with open(output_file, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)


# main
if __name__ == "__main__":
    tsv_reader = TSVLoader()
    reddit_title_data = tsv_reader.load_data("datasets/soc-redditHyperlinks-title.tsv")
    reddit_body_data = tsv_reader.load_data("datasets/soc-redditHyperlinks-body.tsv")
    
    # Convert to pandas DataFrames
    df_title = tsv_reader.to_dataframe(reddit_title_data)
    df_body = tsv_reader.to_dataframe(reddit_body_data)
    
    # Output DataFrame info
    print(df_title.head(10))
    print(df_body.head(10))
