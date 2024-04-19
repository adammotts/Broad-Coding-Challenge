# Get all long names for a list of route objects
def get_long_names(
    routes: list[dict]
) -> list[str]:
    
    return [route["attributes"]["long_name"] for route in routes]

# Get all ids for a list of route objects
def get_ids(
    routes: list[dict]
) -> list[str]:
    
    return [route["id"] for route in routes]