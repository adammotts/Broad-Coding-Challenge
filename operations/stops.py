from route import ENDPOINT, API_KEY, get_data

def get_stops_of_route_id(
    route_id: list[str]
) -> list[dict]:
    
    return get_data(
        ENDPOINT,
        f'stops/?filter[route]={",".join(route_id)}',
        API_KEY
    )