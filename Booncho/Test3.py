# Example after you run Test3.py
# Please enter the edges in the format (node1, node2, weight). Type 'done' when finished:
# 1,2,1 inut colon also
# 2,3,2
# 1,3,4
# 3,4,1
# done //after finish you type "done"
# Please enter the start node: 1
# Please enter the end node: 4
# The shortest path length is: 4
import heapq

def dijkstra(edges, start, end):

    graph = {}
    for edge in edges:
        u, v, w = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))  
    
  
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        

        if current_distance > distances[current_node]:
            continue
        
       
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
           
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances[end]
def get_input():
    edges = []
    print("Please enter the edges in the format (node1, node2, weight). Type 'done' when finished:")
    while True:
        edge_input = input()
        if edge_input.lower() == 'done':
            break
        try:
            edge = tuple(map(int, edge_input.split(',')))
            edges.append(edge)
        except ValueError:
            print("Invalid input. Please enter the edge in the format (node1, node2, weight).")
    
    start = int(input("Please enter the start node: "))
    end = int(input("Please enter the end node: "))
    
    return edges, start, end

edges, start, end = get_input()


result = dijkstra(edges, start, end)
print("The shortest path length is:", result)

