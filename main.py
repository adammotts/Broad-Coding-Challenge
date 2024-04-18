# Broad Institute Coding Challenge

import random
from operations.routes import get_routes_of_types
from operations.stops import get_stops_of_route_id
from algorithm import find_path

def main():

    ######################### Question 1 #########################

    routes = get_routes_of_types(["0", "1"])
    
    routes_long_names = [route["attributes"]["long_name"] for route in routes]
    print(f'\n\nSubway Routes: {", ".join(routes_long_names)}')
    
    ######################### Question 2 #########################
    
    route_to_stops = {
        route["attributes"]["long_name"]: set(
            stop["attributes"]["name"]
            for stop in get_stops_of_route_id([route["id"]])
        ) for route in routes
    }
    
    route_with_most_stops = max(
        route_to_stops,
        key=lambda route: len(route_to_stops[route])
    )
    
    print(f'\n\nRoute With Most Stops: {route_with_most_stops}')
    
    
    route_with_least_stops = min(
        route_to_stops,
        key=lambda route: len(route_to_stops[route])
    )
    
    print(f'\n\nRoute With Least Stops: {route_with_least_stops}')
    
    
    all_stops = get_stops_of_route_id([route["id"] for route in routes])
    
    all_stops_names = [stop["attributes"]["name"] for stop in all_stops]
    
    stops_to_routes = {
        stop_name: [route_name for route_name in routes_long_names if stop_name in route_to_stops[route_name]]
        for stop_name in all_stops_names
    }
    
    two_or_more = {stop_name: routes for stop_name, routes in stops_to_routes.items() if len(routes) >= 2}
    
    print(f'\n\nStops Connecting Two or More Routes:')
    
    for stop_name, routes in two_or_more.items():
        print(f'- {stop_name}: {", ".join(routes)}')
        
    ######################### Question 3 #########################
    
    routes_to_neighboring_routes = {
        route_name: set() for route_name in routes_long_names
    }
    
    for stop_name, routes in stops_to_routes.items():
        for route in routes:
            routes_to_neighboring_routes[route].update(routes)
            routes_to_neighboring_routes[route].remove(route)
    
    starting_stop = random.choice(all_stops_names)
    ending_stop = random.choice(all_stops_names)
    
    starting_route = stops_to_routes[starting_stop][0]
    ending_route = stops_to_routes[ending_stop][0]
    
    path = find_path(starting_route, ending_route, routes_to_neighboring_routes)
    
    print(f'\n\nPath from {starting_stop} to {ending_stop}: {", ".join(path)}\n\n')
        
    
if __name__ == "__main__":
    main()