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
2. **Reddit Threads**  
   [Link to dataset](https://snap.stanford.edu/data/reddit_threads.html)  

These datasets provide subreddit hyperlink networks, including temporal, sentiment, and text data for analysis.

---

## Goals
- Develop an intuitive and interactive dashboard.
- Enable filtering by sentiment, time, and network properties.
- Provide insights into subreddit relationships and sentiment trends.

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
