def AdjacencyList(V, edges):
    '''
    V: numebr fo Vertexs
    edges: [[u,v], ..., [ui, vi]]
    '''
    # number of Vertex
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def AdjacentyListWithWeights(V, edges):
    '''
    V: numebr fo Vertexs
    edges: [[u0,v0, w0], ..., [ui, vj, wi]]
    '''
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((v, w))
    return adj