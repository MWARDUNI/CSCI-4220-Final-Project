# Interactive Reddit Network Visualization with Sentiment Filtering

**Course:** CSCI 4220 Social Networking and Informatics  _University of Colorado_

## Contributors
- _Ernesto Rivera Dominguez_ -  [GitHub](https://github.com/ErnestoRiDo)  [LinkedIn](https://www.linkedin.com/in/ernestoriv/)
- _Brian Hagerty_ -  [GitHub](https://github.com/CashBandicoot)  [LinkedIn](https://www.linkedin.com/in/brian-hagerty-ba3699119/)
- _Matthew Ward_ -  [GitHub](https://github.com/MWARDUNI)  [LinkedIn](https://www.linkedin.com/in/m4tth3w-w4rd/)

---

## Introduction
Our project aims to build an **interactive dashboard** to visualize subreddits within the Reddit network. This dashboard will allow viewers to filter subreddit connections by:
- Temporal evolution  
- Sentiment analysis  
- Network structure  
- Subreddit attributes  
- Content similarity  

---

## Motivation
Reddit hosts a vast array of specialized subreddits that act as a melting pot of social interests and sentiments. This makes it an ideal platform for exploring community interactions. By visualizing subreddit connections and filtering by sentiment, we aim to offer:
- A tool for professionals and researchers to identify trends and relationships across communities.
- A platform for casual users to explore common topics and emotional tones that bind or divide communities of interest.

---

## Implementation
Using the **[NetworkX](https://networkx.org/)** package in Python, we will develop the dashboard with the following technologies:
- **[Python](https://www.python.org/)** for data processing and analytics  
- **[Plotly](https://plotly.com/)** for interactive visualizations  
- **[Pyvis](https://pyvis.readthedocs.io/)** for network visualizations  
- Additional tools to support visualization and analysis  

---

## Dataset
Our project will utilize the following datasets:
1. **Reddit Hyperlink Social Network**  
   [Link to dataset](https://snap.stanford.edu/data/soc-RedditHyperlinks.html)  
   This dataset provides detailed information about hyperlinks shared between subreddits. Each record includes:
   - SOURCE_SUBREDDIT: The subreddit where the hyperlink originated.
   - TARGET_SUBREDDIT: The subreddit that the hyperlink points to.
   - PROPERTIES: A collection of metadata, including timestamps and          precomputed sentiment scores (positive, negative, and compound) from the VADER sentiment analysis tool.

   These features allow us to construct a directed graph where subreddits are represented as nodes, and hyperlinks between them act as edges. The inclusion of source and target subreddits is vital for:
	- Node Visualization: By mapping subreddits as nodes, we can illustrate the interconnected structure of the Reddit network.
	- Edge Attributes: Sentiment scores for links between subreddits enable filtering and visualizing emotional tones within connections.

2. **Reddit Threads**  
   [Link to dataset](https://snap.stanford.edu/data/reddit_threads.html)  

   This dataset complements the hyperlink dataset by providing text content from individual Reddit posts and comments. The text data is analyzed for sentiment to:
	- Identify emotional tones within subreddit threads.
	- Compare sentiment trends across subreddit titles and post bodies.

These datasets provide subreddit hyperlink networks, including temporal, sentiment, and text data for analysis.

---

## Goals
- Develop an intuitive and interactive dashboard.
- Enable filtering by sentiment, time, and network properties.
- Provide insights into subreddit relationships and sentiment trends.

---

## Implementation methods

**Importing the Data**

The implementation for importing data involves reading subreddit interactions from TSV files and converting it into usable formats such as pandas DataFrames and network graphs. A mapping file ensures property consistency, and a directed graph is created using NetworkX to represent relationships. The PyVis library is then used to generate interactive visualizations of the subreddit connections for exploration and analysis.

**Graph Analysis and Interactive Visualization**

This implementation processes subreddit interaction data into directed graphs using NetworkX, applying advanced metrics like PageRank, degree centrality, and modularity-based community detection to uncover patterns of influence and structure within the network. Calculated metrics, including sentiment scores, enable insights into node-level and community-level dynamics. Through Streamlit, users can interact with PyVis-generated visualizations, exploring detailed graph structures, sentiment trends, and community relationships in an intuitive, browser-based interface.

**Sentiment Anaylsis**

The sentiment extraction implementation leverages VADER to analyze the sentiment of Reddit posts and titles. By preprocessing text to remove noise and applying VADER’s sentiment analysis, positive, negative, and compound sentiment scores are calculated. These scores are then aggregated to provide insights into the emotional tone of subreddit interactions, enabling trend tracking and comparison across communities.

---

## Results and Discussion
**Results**

  Through the implementation of our project, we successfully visualized the network of subreddit interactions, showcasing how communities are connected through shared hyperlinks. By representing subreddits as nodes and their connections as edges, we were able to explore the structure of these interactions and identify patterns of influence and connectivity within the network. Metrics such as centrality were incorporated to highlight key subreddits and their roles within the broader system. This visualization demonstrates the potential of our approach to uncover meaningful insights about community dynamics and relationships across Reddit.

   Additionally, we incorporated sentiment analysis to enhance user engagement and exploration. By analyzing potential Reddit thread titles or posts provided by users, we can offer sentiment predictions based on the content. This functionality allows users to understand the emotional tone of their input before posting. Furthermore, we provide real-time sentiment insights for subreddits by calculating the sentiment scores of the most recent 100 posts. This feature enables users to see how a subreddit is currently perceived, offering a unique way to track sentiment trends and community reactions over time.



**Where Can We Go From Here?**  

An exciting direction for this project is exploring the clustering and dynamics of subreddit communities. By identifying groups of subreddits that are closely connected, we can gain insights into how communities naturally form and interact. Observing these connections over time could provide a deeper understanding of how communities evolve, merge, or dissolve, offering a richer perspective on the fluid nature of online interactions. This approach would allow us to capture the broader lifecycle of subreddit relationships and highlight the underlying patterns that drive community dynamics on Reddit.


---

## References
- [Reddit Hyperlink Social Network Dataset](https://snap.stanford.edu/data/soc-RedditHyperlinks.html)
   - #### BibTeX Citation

```bibtex
@inproceedings{kumar2018community,
  title={Community interaction and conflict on the web},
  author={Kumar, Srijan and Hamilton, William L and Leskovec, Jure and Jurafsky, Dan},
  booktitle={Proceedings of the 2018 World Wide Web Conference on World Wide Web},
  pages={933--943},
  year={2018},
  organization={International World Wide Web Conferences Steering Committee}
}
```

- [Reddit Threads Dataset](https://snap.stanford.edu/data/reddit_threads.html)
   - #### BibTeX Citation

```bibtex
@inproceedings{karateclub,
    title = {{Karate Club: An API Oriented Open-source Python Framework for Unsupervised Learning on Graphs}},
    author = {Benedek Rozemberczki and Oliver Kiss and Rik Sarkar},
    year = {2020},
    pages = {3125–3132},
    booktitle = {Proceedings of the 29th ACM International Conference on Information and Knowledge Management (CIKM '20)},
    organization = {ACM},
  }
```

- [NetworkX Documentation](https://networkx.org/)  
- [Plotly Documentation](https://plotly.com/)  
- [Pyvis Documentation](https://pyvis.readthedocs.io/)
