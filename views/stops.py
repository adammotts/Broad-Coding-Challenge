# Get all names for a list of stop objects
def get_names(
    stops: list[dict]
) -> list[str]:
    
    return [stop["attributes"]["name"] for stop in stops]