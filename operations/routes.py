from route import ENDPOINT, API_KEY, get_data

def get_routes_of_types(
    route_types: list[str]
) -> list[dict]:
    
    return get_data(
        ENDPOINT,
        f'routes/?filter[type]={",".join(route_types)}',
        API_KEY
    )