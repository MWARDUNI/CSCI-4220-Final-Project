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

def main():
    st.title("Reddit Hyperlink Network Visualization")
    
    # Dynamically resolve file paths
    base_dir = os.path.abspath(os.path.dirname(__file__))  # Directory of this script
    post_props_path = os.path.join(base_dir, "props_mapping", "post_props.csv")
    props_map_path = os.path.join(base_dir, "props_mapping", "props_map.csv")
    
    # Check file existence
    if not os.path.exists(post_props_path):
        st.error(f"File not found: {post_props_path}")
        return
    
    # Generate props map if needed
    if st.button("Generate Props Map"):
        try:
            generate_props_map(post_props_path, props_map_path)
            st.success("Props map generated successfully!")
        except FileNotFoundError:
            st.error(f"File not found: {post_props_path}")
        except Exception as e:
            st.error(f"An error occurred while generating the props map: {e}")
    
    # File upload
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


    # UPLOADS ONLY FIRST 10 NODES TO DF!!
    # if uploaded_file is not None:
    #     tsv_reader = TSVLoader()
    #     reddit_data = tsv_reader.load_data(uploaded_file)
        
    #     # Convert to DataFrame
    #     df = tsv_reader.to_dataframe(reddit_data)
        
    #     # Display the first 500 rows only
    #     st.write("First 500 Nodes in DataFrame:")
    #     df_first_500 = df.head(500)
    #     st.dataframe(df_first_500)

    #     # Visualize graph
    #     if st.button("Generate Graph Visualization"):
    #         # Filter the graph data to only include the first 50 nodes
    #         filtered_data = {}
    #         for index, row in df_first_500.iterrows():
    #             source = row["source"]
    #             target = row["target"]
    #             if source not in filtered_data:
    #                 filtered_data[source] = []
    #             filtered_data[source].append({
    #                 "target": target,
    #                 "post_id": row["post_id"],
    #                 "ts": row["timestamp"],
    #                 "sentiment": row["sentiment"],
    #                 "props": {key: row[key] for key in row.index if key not in ["source", "target", "post_id", "timestamp", "sentiment"]}
    #             })

    #         # Generate graph using the filtered data
    #         graph = tsv_reader.to_networkx_graph(filtered_data)
    #         tsv_reader.pyvis_visualizer(graph, "streamlit_graph.html")
    #         with open("streamlit_graph.html", "r") as f:
    #             html = f.read()
    #             st.components.v1.html(html, height=800, scrolling=True)

    if uploaded_file is not None:
        tsv_reader = TSVLoader()
        reddit_data = tsv_reader.load_data(uploaded_file)
        
        # Convert to DataFrame
        # df = tsv_reader.to_dataframe(reddit_data)
        # df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')
        # if df['sentiment'].isnull().any():
        #     st.error("The sentiment column contains invalid values. Please clean the data and try again.")
        #     return
        
        df = tsv_reader.to_dataframe(reddit_data)
        df.loc[:, 'sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')
        if df['sentiment'].isnull().any():
            st.warning("Some sentiment values are missing or invalid. Setting them to 0.")
            df.loc[:, 'sentiment'] = df['sentiment'].fillna(0)
            return
        
        # Display the first 10 rows
        st.write("First 1000 Nodes in DataFrame:")
        df_first_1000 = df.head(1000)
        st.dataframe(df_first_1000)

        # Graph generation
        if st.button("Analyze and Visualize Graph"):
            # Create graph from filtered DataFrame
            graph = create_graph_from_dataframe(df_first_1000)
            
            # Calculate centrality measures
            calculate_centrality_measures(graph)
            
            # Get top nodes by PageRank
            top_nodes = get_top_nodes(graph, 'pagerank')
            st.write("Top Nodes by PageRank:")
            for node, score in top_nodes:
                st.write(f"{node}: {score}")
            
            # Identify communities
            communities = get_communities(graph)
            st.write(f"Identified {len(communities)} communities.")
            
            # Community sentiment
            community_sentiment = calculate_community_sentiment(graph, communities)
            st.write("Community Sentiment Scores:")
            for community, sentiment in community_sentiment.items():
                st.write(f"Community {community}: {sentiment}")
            
            # Visualize communities
            st.write("Community Visualization:")
            visualize_communities(graph, communities, out_file="communities.html")
            with open("communities.html", "r") as f:
                st.components.v1.html(f.read(), height=800, scrolling=True)
            
            # Visualize graph
            st.write("Graph Visualization:")
            visualize_graph(graph, out_file="network.html")
            with open("network.html", "r") as f:
                st.components.v1.html(f.read(), height=800, scrolling=True)


if __name__ == "__main__":
    main()
