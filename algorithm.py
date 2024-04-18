def find_path(
    starting_route: str,
    ending_route: str,
    adjacency_list: dict[str, set[str]],
) -> list[str]:
    
    visited = set()
    path = []
    
    def dfs(
        current_route: str,
        accumulated_path: list[str]
    ) -> list[str]:
        
        if current_route == ending_route:
            return accumulated_path + [current_route]
        
        visited.add(current_route)
        
        for neighbor in adjacency_list[current_route]:
            if neighbor not in visited:
                new_path = dfs(neighbor, accumulated_path + [current_route])
                
                if new_path:
                    return new_path
                
        return []
    
    return dfs(starting_route, path)