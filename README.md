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
- A tool for users to identify trends and relationships across vast communities.
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
2. **Reddit Threads**  
   [Link to dataset](https://snap.stanford.edu/data/reddit_threads.html)  

These datasets provide subreddit hyperlink networks, including temporal, sentiment, and text data for analysis.

---

## Goals
- Develop an intuitive and interactive dashboard.
- Enable filtering by sentiment, time, and network properties.
- Provide insights into subreddit relationships and sentiment trends.

---

## Project Milestones
### Step 1: Scope and Requirements
- **Objectives**:
  - Build network structure from datasets.
  - Build an intuitive dashboard.
  - Allow filtering by sentiment, time, and network properties.
  - Provide actionable insights on subreddit relationships and sentiment trends.
- **Identify Key Features**:
  - Sentiment-based filtering.
  - Network visualization (e.g., clusters, node importance).
  - Temporal filtering for trends over time.

### Step 2: Environment
- **Development Environment**:
  - Required libraries: `networkx`, `csv`, `plotly`, `pyvis`, `vaderSentiment`, `pandas`, `numpy`, others tbd...
  - Recommend running in a python venv.

### Step 3: Datasets
- **Reddit Hyperlink Social Network Dataset**: Directed subreddit connections with sentiment and timestamps.

### Step 4: Analyze and Preprocess Data
- **Create Subreddit Graph**:
  - Construct a directed graph using `networkx`.
  - Add node and edge attributes:
    - Nodes: subreddit embeddings, activity level, etc.
    - Edges: sentiment, timestamp, link strength.
- **Temporal Aggregation**:
  - Organize data by time intervals for trend analysis.
- **Sentiment Analysis**:
  - Extract sentiment labels or compute new ones if necessary (e.g. Vader Sentiment Analysis)
  - Aggregate sentiments per edge or node for better insights.

### Step 5: Build Interactive Visualizations
- **Network Visualization with Pyvis**:
  - Use `networkx` to create the network structure.
  - Integrate `pyvis` for an interactive, browser-based network display.
  - Add features:
    - Node size based on centrality or degree?
    - Edge color/width for sentiment or weight?
- **Trends and Filtering with Plotly**:
  - Create interactive graphs (e.g., time-series sentiment trends)?
  - Add dropdowns/sliders for filtering by sentiment, time, or network properties.
- **Dashboard Integration**:
  - Combine `pyvis` and `plotly` outputs into a single dashboard using `Streamlit`.

### Step 6: Develop Analytical Tools
- **Metrics**:
  - Compute centrality metrics (e.g., degree, betweenness).
  - Identify communities using clustering algorithms.
- **Sentiment Trends**:
  - Analyze sentiment trends within and across communities.

### Step 7: Test and Refine
- **Test Filters and Interactions**:
  - Ensure filters (e.g., sentiment, time) work.
  - Validate network visualization for accuracy and usability.
- **Optimize Performance**:
  - Minimize latency in rendering graphs or applying filters.
  - Handle large datasets by sampling or summarization.

### Step 8: Deployment
- **Package the Application**:
  - Use a platform like `Streamlit` or `Dash` to create a deployable app.
  - Test for cross-platform compatibility (e.g., desktop, mobile).
- **Host the Dashboard**:
  - Host the application on a cloud platform (e.g., Heroku, AWS).
  - Ensure access to the datasets is seamless and secure.

### Step 9: Document and Share
- **Write Documentation**:
  - Include steps to set up the environment and use the dashboard.
  - Provide insights on how users can benefit from the tool.
- **Publish Insights**:
  - Highlight interesting trends or patterns discovered during analysis.

### Tools & Technologies Checklist
1. **Python Libraries**:
   - `pandas`, `numpy`, `matplotlib` for data processing and basic plots?
   - `networkx`, `pyvis` for network analysis and visualization.
   - `plotly` for interactive charts.
2. **Visualization Framework**:
   - `Streamlit` for dashboard creation.

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
