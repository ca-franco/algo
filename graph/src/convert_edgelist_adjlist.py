def convert_edgelist_adjlist(n,edge_list):
    adjlist = []
    for edge in edge_list:
        adjlist[edge[0]]).append(edge[1])
        adjlist[edge[1]]append(edge[0])

    for edglist in adjlist:
        edglist.sort()

    return adjlist


