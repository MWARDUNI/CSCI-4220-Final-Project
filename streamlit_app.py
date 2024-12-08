import os
import streamlit as st
import scipy as sp
import pandas as pd
from read_tsvs import TSVLoader, generate_props_map
from translate_graph import (
    create_graph_from_dataframe,
    calculate_betweenness_centrality, 
    calculate_centrality_measures, 
    calculate_community_sentiment, 
    calculate_closeness_centrality,
    calculate_pagerank, 
    calculate_eigenvector_centrality, 
    calculate_degree_centrality, 
    calculate_sentiment_score,
    get_communities, 
    get_top_nodes, 
    visualize_communities,
    visualize_graph, 
)


st.set_page_config(layout="wide")


def main():
    st.title("Reddit Hyperlink Network Visualization")
    
    # resolve file paths
    base_dir = os.path.abspath(os.path.dirname(__file__))  # Directory of this script
    post_props_path = os.path.join(base_dir, "props_mapping", "post_props.csv")
    props_map_path = os.path.join(base_dir, "props_mapping", "props_map.csv")
    
  
    if not os.path.exists(post_props_path):
        st.error(f"File not found: {post_props_path}")
        return
    
    # generate props map
    if st.button("Generate Props Map"):
        try:
            generate_props_map(post_props_path, props_map_path)
            st.success("Props map generated successfully!")
        except FileNotFoundError:
            st.error(f"File not found: {post_props_path}")
        except Exception as e:
            st.error(f"An error occurred while generating the props map: {e}")
    

    uploaded_file = st.file_uploader("Upload a TSV file", type=["tsv"])

    # UPLOADS THE ENTIRE DATASET TO THE DF!!
    # if uploaded_file is not None:
    #     tsv_reader = TSVLoader()
    #     reddit_data = tsv_reader.load_data(uploaded_file)
        
    #     # Show DataFrame
    #     df = tsv_reader.to_dataframe(reddit_data)
    #     st.write("Loaded DataFrame:")
    #     st.dataframe(df)

    #     # Visualize graph
    #     if st.button("Generate Graph Visualization"):
    #         graph = tsv_reader.to_networkx_graph(reddit_data)
    #         tsv_reader.pyvis_visualizer(graph, "streamlit_graph.html")
    #         with open("streamlit_graph.html", "r") as f:
    #             html = f.read()
    #             st.components.v1.html(html, height=800, scrolling=True)



    if uploaded_file is not None:
        tsv_reader = TSVLoader()
        reddit_data = tsv_reader.load_data(uploaded_file)

        
        df = tsv_reader.to_dataframe(reddit_data)
        df.loc[:, 'sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')
        if df['sentiment'].isnull().any():
            st.warning("Some sentiment values are missing or invalid. Setting them to 0.")
            df.loc[:, 'sentiment'] = df['sentiment'].fillna(0)
            return
        
        # set the number of nodes to display
        n_nodes = 2000

        # display the first 2000 rows
        st.write(f"First {n_nodes} Nodes in DataFrame:")
        df_n_nodes = df.head(n_nodes)
        st.dataframe(df_n_nodes)

        # graph generation
        if st.button("Analyze and Visualize Graph"):
            
            graph = create_graph_from_dataframe(df_n_nodes)
            
            # calc centrality measures
            calculate_centrality_measures(graph)
            calculate_degree_centrality(graph)
            
            # get top nodes by PageRank
            top_nodes = get_top_nodes(graph, 'pagerank')
            st.write("Top Nodes by PageRank:")
            for node, score in top_nodes:
                st.write(f"{node}: {score}")
            
            # ID communities
            communities = get_communities(graph)
            st.write(f"Identified {len(communities)} communities.")
            
            # community sentiment
            community_sentiment = calculate_community_sentiment(graph, communities)
            st.write("Community Sentiment Scores:")
            for community, sentiment in community_sentiment.items():
                st.write(f"Community {community}: {sentiment}")
            
            # visualize communities
            st.write("Community Visualization:")
            visualize_communities(graph, communities, out_file="communities.html")
            with open("communities.html", "r") as f:
                st.components.v1.html(f.read(), height=800, scrolling=True)
            
            # visualize graph
            st.write("Graph Visualization:")
            visualize_graph(graph, out_file="network.html")
            with open("network.html", "r") as f:
                st.components.v1.html(f.read(), height=800, scrolling=True)


if __name__ == "__main__":
    main()
