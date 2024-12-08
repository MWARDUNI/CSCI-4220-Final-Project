from pyvis.network import Network
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import pandas as pd



def create_graph_from_dataframe(df):
    required_columns = {'source', 'target', 'sentiment'}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"DataFrame must contain the following columns: {required_columns}")
    
    # Ensure sentiment column is numeric
    df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')
    if df['sentiment'].isnull().any():
        raise ValueError("Sentiment column contains non-numeric values that could not be converted.")
    
    graph = nx.DiGraph()
    for _, row in df.iterrows():
        graph.add_edge(row['source'], row['target'], sentiment=row['sentiment'])
    return graph




def calculate_sentiment_score(graph):
    for node in graph.nodes():
        in_edges = graph.in_edges(node, data=True)
        out_edges = graph.out_edges(node, data=True)
        in_sentiment = sum(edge[2]['sentiment'] for edge in in_edges)
        out_sentiment = sum(edge[2]['sentiment'] for edge in out_edges)
        graph.nodes[node]['sentiment_score'] = in_sentiment - out_sentiment


def calculate_degree_centrality(graph):
    degree_centrality = nx.degree_centrality(graph)
    nx.set_node_attributes(graph, degree_centrality, 'degree_centrality')


def calculate_betweenness_centrality(graph):
    betweenness_centrality = nx.betweenness_centrality(graph)
    nx.set_node_attributes(graph, betweenness_centrality, 'betweenness_centrality')


def calculate_closeness_centrality(graph):
    closeness_centrality = nx.closeness_centrality(graph)
    nx.set_node_attributes(graph, closeness_centrality, 'closeness_centrality')


def calculate_eigenvector_centrality(graph):
    eigenvector_centrality = nx.eigenvector_centrality(graph)
    nx.set_node_attributes(graph, eigenvector_centrality, 'eigenvector_centrality')


def calculate_pagerank(graph):
    pagerank = nx.pagerank(graph)
    nx.set_node_attributes(graph, pagerank, 'pagerank')


def calculate_centrality_measures(graph):
    calculate_degree_centrality(graph)
    calculate_betweenness_centrality(graph)
    calculate_closeness_centrality(graph)
    calculate_eigenvector_centrality(graph)
    calculate_pagerank(graph)


def get_top_nodes(graph, measure, top_n=10):
    centrality_scores = nx.get_node_attributes(graph, measure)
    sorted_nodes = sorted(centrality_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_nodes[:top_n]


def get_communities(graph):
    return list(greedy_modularity_communities(graph))


def visualize_communities(graph, communities, out_file='communities.html'):
    net = Network(notebook=True, height='2000px', width='100%',
                  directed=True, neighborhood_highlight=True,
                  select_menu=True, filter_menu=True,
                  bgcolor='#222222', font_color='white',
                  cdn_resources='in_line'
                )

    net.from_nx(graph)

    # Assign colors to nodes based on community
    color_palette = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']
    for i, community in enumerate(communities):
        color = color_palette[i % len(color_palette)]
        for node in community:
            net.get_node(node)['color'] = color

    net.show(out_file)


def calculate_community_sentiment(graph, communities):
    community_sentiment = {}
    for i, community in enumerate(communities):
        sentiment_scores = [
            graph.nodes[node].get('sentiment_score', 0) for node in community
        ]
        if len(sentiment_scores) > 0:
            average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        else:
            average_sentiment = 0
        community_sentiment[i] = average_sentiment
    return community_sentiment

def calculate_betweeness_centrality(graph):
    betweenness_centrality = nx.betweenness_centrality(graph)
    nx.set_node_attributes(graph, betweenness_centrality, 'betweenness_centrality')

def calculate_closeness_centrality(graph):
    closeness_centrality = nx.closeness_centrality(graph)
    nx.set_node_attributes(graph, closeness_centrality, 'closeness_centrality')

def calculate_eigenvector_centrality(graph):
    eigenvector_centrality = nx.eigenvector_centrality(graph)
    nx.set_node_attributes(graph, eigenvector_centrality, 'eigenvector_centrality')

def calculate_pagerank(graph):
    pagerank = nx.pagerank(graph)
    nx.set_node_attributes(graph, pagerank, 'pagerank')

def calculate_centrality_measures(graph):
    calculate_degree_centrality(graph)
    calculate_betweenness_centrality(graph)
    calculate_closeness_centrality(graph)
    calculate_eigenvector_centrality(graph)
    calculate_pagerank(graph)

def get_top_nodes(graph, measure, top_n=10):
    centrality_scores = nx.get_node_attributes(graph, measure)
    sorted_nodes = sorted(centrality_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_nodes[:top_n]

def get_communities(graph):
    return list(greedy_modularity_communities(graph))


def visualize_graph(graph, out_file='network.html'):
    net = Network(
        notebook=True, height='1000px', width='100%', 
        directed=True, neighborhood_highlight=True, 
        select_menu=True, filter_menu=True, 
        bgcolor='#222222', font_color='white',
        cdn_resources='in_line'
    )
    
    # Load the graph into Pyvis
    net.from_nx(graph)

    # Customize nodes
    for node in net.nodes:
        node['title'] = node.get('label', node['id'])
        node['value'] = graph.degree(node['id'])
        node['size'] = graph.degree(node['id'])
        node['color'] = '#00ff1e'

    # Customize edges
    for edge in net.edges:
        # Get edge data from the NetworkX graph
        edge_data = graph.get_edge_data(edge['from'], edge['to'], default={})
        sentiment = edge_data.get('sentiment')
        if isinstance(sentiment, (int, float)):  # Ensure sentiment is numeric
            edge['color'] = 'green' if sentiment > 0 else 'red'
            edge['width'] = abs(sentiment) * 2

    # Save the visualization to an HTML file
    net.show(out_file)



if __name__ == '__main__':
    
    title_graph = create_graph_from_dataframe(df_title)
    body_graph = create_graph_from_dataframe(df_body)

    calculate_centrality_measures(title_graph)
    calculate_centrality_measures(body_graph)

    top_title_nodes = get_top_nodes(title_graph, 'pagerank')
    top_body_nodes = get_top_nodes(body_graph, 'pagerank')

    print("Top Title Nodes:")
    for node, score in top_title_nodes:
        print(f"{node}: {score}")

    print("\nTop Body Nodes:")
    for node, score in top_body_nodes:
        print(f"{node}: {score}")

    title_communities = get_communities(title_graph)
    body_communities = get_communities(body_graph)

    visualize_communities(title_graph, title_communities, out_file='title_communities.html')
    visualize_communities(body_graph, body_communities, out_file='body_communities.html')

    title_community_sentiment = calculate_community_sentiment(title_graph, title_communities)
    body_community_sentiment = calculate_community_sentiment(body_graph, body_communities)

    visualize_graph(title_graph, out_file='title_network.html')
    visualize_graph(body_graph, out_file='body_network.html')

    print("\nTitle Community Sentiment:")
    for community, sentiment in title_community_sentiment.items():
        print(f"Community {community}: {sentiment}")

    print("\nBody Community Sentiment:")
    for community, sentiment in body_community_sentiment.items():
        print(f"Community {community}: {sentiment}")