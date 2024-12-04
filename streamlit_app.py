import os
import streamlit as st
from read_tsvs import TSVLoader, generate_props_map

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
    if uploaded_file is not None:
        tsv_reader = TSVLoader()
        reddit_data = tsv_reader.load_data(uploaded_file)
        
        # Show DataFrame
        df = tsv_reader.to_dataframe(reddit_data)
        st.write("Loaded DataFrame:")
        st.dataframe(df)
        
        # Visualize graph
        if st.button("Generate Graph Visualization"):
            graph = tsv_reader.to_networkx_graph(reddit_data)
            tsv_reader.pyvis_visualizer(graph, "streamlit_graph.html")
            with open("streamlit_graph.html", "r") as f:
                html = f.read()
                st.components.v1.html(html, height=800, scrolling=True)

if __name__ == "__main__":
    main()
