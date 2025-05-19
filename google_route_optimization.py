import os
import requests


def optimize_route(addresses, api_key=None):
    """Optimize order of stops via Google Directions API.

    Parameters
    ----------
    addresses : list[str]
        List of addresses where the first entry is the origin and the last
        is the final destination. Intermediate addresses will be treated as
        waypoints.
    api_key : str, optional
        Google API key. If omitted, the function will read the key from the
        GOOGLE_MAPS_API_KEY environment variable.

    Returns
    -------
    dict
        Parsed JSON response from the API containing the optimized order and
        route information.
    """
    if api_key is None:
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("Missing Google Maps API key")

    if len(addresses) < 2:
        raise ValueError("At least origin and destination must be provided")

    origin = addresses[0]
    destination = addresses[-1]
    waypoints = addresses[1:-1]

    base_url = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": origin,
        "destination": destination,
        "key": api_key,
    }

    if waypoints:
        params["waypoints"] = "optimize:true|" + "|".join(waypoints)

    response = requests.get(base_url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    import json
    sample_addresses = [
        "1600 Amphitheatre Parkway, Mountain View, CA",
        "1 Infinite Loop, Cupertino, CA",
        "500 Terry Francois Blvd, San Francisco, CA",
    ]
    data = optimize_route(sample_addresses)
    print(json.dumps(data, indent=2))
