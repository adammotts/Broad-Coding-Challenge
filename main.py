# Broad Institute Coding Challenge

import random
from tests import tests
from operations.routes import get_routes_of_types
from operations.stops import get_stops_of_route_ids
from views.routes import get_long_names, get_ids
from views.stops import get_names
from algorithm import find_path

def main():

    ################################################## Question 1 ##################################################

    '''
    In this instance, it's best to use the MBTA API's abstractions to get the data we need, as
    handling the data processing from our end is slower, more error-prone, and also exposes us
    to data that we do not necessarily need. Furthermore, the MBTA data required for Question 2
    cannot be gathered without using URL parameters.
    '''

    routes: list[dict] = get_routes_of_types(["0", "1"])
    
    routes_long_names: list[str] = get_long_names(routes)
    
    print(f'\n\nSubway Routes: {", ".join(routes_long_names)}')
    
    ################################################## Question 2 ##################################################
    
    route_ids: list[str] = get_ids(routes)
    
    route_to_stops: dict[str, set[str]] = {
        route_name: set(
            get_names(
                get_stops_of_route_ids([route_id])
            )
        ) for route_id, route_name in zip(route_ids, routes_long_names)
    }
    
    route_with_most_stops: str = max(
        route_to_stops,
        key=lambda route: len(route_to_stops[route])
    )
    
    print(f'\n\nRoute With Most Stops: {route_with_most_stops}')
    
    
    route_with_least_stops: str = min(
        route_to_stops,
        key=lambda route: len(route_to_stops[route])
    )
    
    print(f'\n\nRoute With Least Stops: {route_with_least_stops}')
    
    
    all_stops: list[dict] = get_stops_of_route_ids(route_ids)
    
    all_stops_names: list[str] = get_names(all_stops)
    
    stops_to_routes: dict[str, list[str]] = {
        stop_name: [route_name for route_name in routes_long_names if stop_name in route_to_stops[route_name]]
        for stop_name in all_stops_names
    }
    
    two_or_more: dict[str, list[str]] = {stop_name: routes for stop_name, routes in stops_to_routes.items() if len(routes) >= 2}
    
    print(f'\n\nStops Connecting Two or More Routes:')
    
    for stop_name, routes in two_or_more.items():
        print(f'- {stop_name}: {", ".join(routes)}')
        
    ################################################## Question 3 ##################################################
    
    routes_to_neighboring_routes: dict[str, set[str]] = {
        route_name: set() for route_name in routes_long_names
    }
    
    for stop_name, routes in stops_to_routes.items():
        for route in routes:
            routes_to_neighboring_routes[route].update(routes)
            routes_to_neighboring_routes[route].remove(route)
    
    print(f'\n\nExamples of Finding Paths:')
    
    for _ in range(10):
        starting_stop = random.choice(all_stops_names)
        ending_stop = random.choice(all_stops_names)
        
        starting_route = stops_to_routes[starting_stop][0]
        ending_route = stops_to_routes[ending_stop][0]
        
        path = find_path(starting_route, ending_route, routes_to_neighboring_routes)
        
        print(f'- {starting_stop} to {ending_stop} -> {", ".join(path)}')
        
    print(f'\n')
        
    
if __name__ == "__main__":
    tests()
    main()