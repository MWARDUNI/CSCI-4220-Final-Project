from pyvis.network import Network
import networkx as nx


def visualize_graph(graph, out_file='network.html'):
    # translate the networkx graph to pyvis graph
    net = Network(notebook=True, height='1000px', width='100%', 
                  directed=True, neighborhood_highlight=True, 
                  select_menu=True, filter_menu=True,
                  bgcolor='#222222', font_color='white')
    
    net.from_nx(graph)

    # apply customizations to the pyvis graph
    for node in net.nodes:
        node['title'] = node['label']
        node['value'] = graph.degree(node['id'])
        node['size'] = graph.degree(node['id'])
        node['color'] = '#00ff1e'

    for edge in net.edges:
        edge['sentiment'] = graph[edge['source']][edge['dest']]['sentiment']
        if 'sentiment' in edge:
            edge['color'] = 'green' if edge['sentiment'] > 0 else 'red'
            edge['width'] = abs(edge['sentiment']) * 2
        

    # save the pyvis graph to an HTML file
   

    net.show(out_file)
