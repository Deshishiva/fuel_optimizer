from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

from .services.route_service import get_route
from .services.fuel_service import generate_stops
from .fuel_data import fuel_stations


@api_view(['POST'])
def optimize_route(request):
    try:
        start = request.data.get("start")
        end = request.data.get("end")

        if not start or not end:
            return Response({"error": "Start and End required"}, status=400)

        cache_key = f"{start}-{end}"
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        distance, geometry = get_route(start, end)

        stops = generate_stops(distance, geometry, fuel_stations)

        total_cost = 0
        gallons_per_stop = 500 / 10  # 50 gallons

        for stop in stops:
            total_cost += gallons_per_stop * stop["station"]["price"]

        response = {
            "distance_miles": round(distance, 2),
            "fuel_stops": stops,
            "total_cost": round(total_cost, 2),
            "route": geometry
        }

        cache.set(cache_key, response, timeout=3600)

        return Response(response)

    except Exception as e:
        return Response({"error": str(e)}, status=500)