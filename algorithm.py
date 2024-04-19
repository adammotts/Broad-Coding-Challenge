# Use DFS to find a path that exists between a start and end route in a graph represented by an adjacency list.
def find_path(
    starting_route: str,
    ending_route: str,
    adjacency_list: dict[str, set[str]],
) -> list[str]:
    
    # Keep track of a set of visited routes to prevent infinite traversal
    visited = set()
    
    # Keep track of the path that has been traversed so far
    path = []
    
    # Recursive function to traverse the graph
    def dfs(
        current_route: str,
        accumulated_path: list[str]
    ) -> list[str]:
        
        # If the destination has been reached, return the path
        if current_route == ending_route:
            return accumulated_path + [current_route]
        
        # Mark the current route as visited
        visited.add(current_route)
        
        # Traverse each of the neighbors of the current route
        for neighbor in adjacency_list[current_route]:
            
            # If the neighbor has not been visited, recursively traverse it
            if neighbor not in visited:
                new_path = dfs(neighbor, accumulated_path + [current_route])
                
                # If a path has been found, return it
                if new_path:
                    return new_path
                
        # If no path has been found, return an empty list
        return []
    
    return dfs(starting_route, path)