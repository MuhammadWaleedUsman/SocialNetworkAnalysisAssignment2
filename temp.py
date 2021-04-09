import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from collections import Counter, defaultdict
import networkx as nx

g = nx.read_edgelist("data/CA-AstroPh1.txt", nodetype=int)
g1 = nx.DiGraph(g)
# g2 = nx.erdos_renyi_graph(n=1000, p=1,  seed=None, directed=True)
# g2 = nx.DiGraph(g2)
# g3 = nx.watts_strogatz_graph(n=1000, k=2, p=0.1, seed=None)
# g3 = nx.DiGraph(g3)


# Degree Distribution
def plot_degree_dist(G, i):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()
    # plt.savefig('Degree Distribution ' + str(i) + '.png')


# plot_degree_dist(g1, 1)
# plot_degree_dist(g2, 2)
# plot_degree_dist(g3, 3)


# WCC Distribution
def plot_wcc_distribution(_g, i):
    """Plot weakly connected components size distributions
    :param _g: Transaction graph
    :param _plot_img: WCC size distribution image (log-log plot)
    :return:
    """
    all_wcc = nx.weakly_connected_components(_g)
    wcc_sizes = Counter([len(wcc) for wcc in all_wcc])
    size_seq = sorted(wcc_sizes.keys())
    size_hist = [wcc_sizes[x] for x in size_seq]

    plt.figure(figsize=(16, 12))
    plt.clf()
    plt.loglog(size_seq, size_hist, 'ro-')
    plt.title("WCC Size Distribution")
    plt.xlabel("Size")
    plt.ylabel("Number of WCCs")
    plt.savefig('Wcc Distribution ' + str(i) + '.png')


# plot_wcc_distribution(g1, 1)
# plot_wcc_distribution(g2, 2)
# plot_wcc_distribution(g3, 3)


# Shortest Length Distribution
def plot_shortest_length_distribution(_g, j):
    list_shortest_paths = []
    shortest_paths = dict(nx.shortest_path_length(_g))
    for value in shortest_paths.values():
        for key, item in value.items():
            list_shortest_paths.append(key)
    plt.hist(list_shortest_paths)
    plt.show()
    # plt.hist(y)
    # plt.show()
    # shortest_path = dict(nx.shortest_path_length(_g))
    # all_shortest_path = shortest_path
    # my_list = [val for key, val in all_shortest_path.items() for _ in range(key)]
    # plt.clf()
    # plt.hist(y)
    # plt.show()
    # plt.savefig('Shortest Length Distribution ' + str(j) + '.png')
    # pathlengths = []
    #
    # print("source vertex {target:length, }")
    # for v in G.nodes():
    #     spl = dict(nx.single_source_shortest_path_length(G, v))
    #     print(f"{v} {spl} ")
    #     for p in spl:
    #         pathlengths.append(spl[p])
    #
    # print()
    # print(f"average shortest path length {sum(pathlengths) / len(pathlengths)}")
    #
    # # histogram of path lengths
    # dist = {}
    # for p in pathlengths:
    #     if p in dist:
    #         dist[p] += 1
    #     else:
    #         dist[p] = 1
    #
    # print()
    # print("length #paths")
    # verts = dist.keys()
    # for d in sorted(verts):
    #     print(f"{d} {dist[d]}")
    #
    # print(f"radius: {nx.radius(G)}")
    # print(f"diameter: {nx.diameter(G)}")
    # print(f"eccentricity: {nx.eccentricity(G)}")
    # print(f"center: {nx.center(G)}")
    # print(f"periphery: {nx.periphery(G)}")
    # print(f"density: {nx.density(G)}")
    #
    # nx.draw(G, with_labels=True)
    # plt.show()


plot_shortest_length_distribution(g1, 1)
# plot_shortest_length_distribution(g2, 2)
# plot_shortest_length_distribution(g3, 3)


# Clustering Distribution
def plot_clustering_distribution(_g, j):
    plt.clf()
    gc = g.subgraph(max(nx.weakly_connected_components(_g)))
    lcc = nx.clustering(gc)
    cmap = plt.get_cmap('autumn')
    norm = plt.Normalize(0, max(lcc.values()))
    node_colors = [cmap(norm(lcc[node])) for node in gc.nodes]
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 4))
    nx.draw_spring(gc, node_color=node_colors, with_labels=True, ax=ax1)
    fig.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Clustering', shrink=0.95, ax=ax1)
    ax2.hist(lcc.values(), bins=10)
    ax2.set_xlabel('Clustering')
    ax2.set_ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('Clustering Coefficent Distribution ' + str(j) + '.png')

#
# plot_clustering_distribution(g1, 1)
# plot_clustering_distribution(g2, 2)
# plot_clustering_distribution(g3, 3)
