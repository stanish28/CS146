import heapq

def minCostToSupplyWater(n, wells, pipes):
   
    adj = {i: [] for i in range(n + 1)}
    
    for i in range(1, n + 1):
        adj[0].append((wells[i - 1], i))
        adj[i].append((wells[i - 1], 0))
    
    for house1, house2, cost in pipes:
        adj[house1].append((cost, house2))
        adj[house2].append((cost, house1))
    
    mst_cost = 0
    visited = set()
    edges = [(0, 0)] 
    heapq.heapify(edges)
    
    while edges and len(visited) < n + 1:
        cost, house = heapq.heappop(edges)
        if house in visited:
            continue
      
        mst_cost += cost
        visited.add(house)
        
        for next_cost, neighbor in adj[house]:
            if neighbor not in visited:
                heapq.heappush(edges, (next_cost, neighbor))
    
    return mst_cost
