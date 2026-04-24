import math

# Haversine distance (km)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)

    a = (
        math.sin(dLat/2)**2 +
        math.cos(math.radians(lat1)) *
        math.cos(math.radians(lat2)) *
        math.sin(dLon/2)**2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


def decode_polyline(polyline):
    coords = []
    index, lat, lng = 0, 0, 0

    while index < len(polyline):
        shift, result = 0, 0
        while True:
            b = ord(polyline[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20:
                break
        dlat = ~(result >> 1) if result & 1 else (result >> 1)
        lat += dlat

        shift, result = 0, 0
        while True:
            b = ord(polyline[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20:
                break
        dlng = ~(result >> 1) if result & 1 else (result >> 1)
        lng += dlng

        coords.append((lat / 1e5, lng / 1e5))

    return coords


def find_nearest_station(point, stations):
    lat, lng = point
    best = None
    best_score = float("inf")

    for s in stations:
        dist = haversine(lat, lng, s["lat"], s["lng"])
        score = dist * s["price"]  # distance + price optimization

        if score < best_score:
            best_score = score
            best = s

    return best


def generate_stops(distance, geometry, stations):
    route_points = decode_polyline(geometry)

    stops = []
    interval = 500  # miles
    current = interval

    step = max(1, len(route_points) // int(distance))

    for i in range(0, len(route_points), step):
        if current <= distance:
            point = route_points[i]
            station = find_nearest_station(point, stations)

            stops.append({
                "distance": round(current, 2),
                "station": station
            })

            current += interval

    return stops