import heapq

def dijkstra(source, V, weightedAdj):
    # distance from souce to vertex i 
    distTo = [float('inf')] * V
    distTo[source] = 0

    # use a heapq to store the vertex that need to process
    pq = []
    heapq.heappush(pq, (0, source))

    while pq:
        d, u = heapq.heappop(pq)

        for v, weight in weightedAdj[u]:
            if d + weight < distTo[v]:
                distTo[v] = d + weight
                heapq.heappush(pq, (distTo[v], v))
    
    return distTo