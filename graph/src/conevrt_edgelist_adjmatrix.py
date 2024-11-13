def conevrt_edglist_adjmatrix(n, edgelist):
    adjmatrix = [[False]*n for _ in range(n)] 

    for edge in edgelist:
        adjmatrix[edg[0]][edge[1] = True
        adjmatrix[edg[1]][edge[0] = True

    return adjmatrix


