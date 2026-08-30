#!/usr/bin/python
import json
import math


import math

def latlon_to_pixels(lat, lon, zoom=4, tile_size=256):
    """
    Translates Latitude/Longitude coordinates into pixel coordinates (x, y)
    for a specific Leaflet zoom level.
    """
    # 1. Total dimensions of the world map at this zoom level
    map_dim = tile_size * (2 ** zoom)

    # 2. X coordinate translation (linear mapping for longitude)
    x = (lon + 180.0) / 360.0 * map_dim

    # 3. Y coordinate translation (Web Mercator projection for latitude)
    lat_rad = math.radians(lat)
    # Clip latitude to prevent infinity at poles (-85.0511 to 85.0511)
    lat_rad = max(min(lat_rad, 1.48442222963), -1.48442222963)
    y = (1.0 - (math.log(math.tan(lat_rad) + (1.0 / math.cos(lat_rad))) / math.pi)) / 2.0 * map_dim

    return x, y

def pixels_to_latlon(x, y, zoom=4, tile_size=256):
    """
    Translates pixel coordinates (x, y) back into Latitude/Longitude coordinates
    for a specific Leaflet zoom level.
    """
    map_dim = tile_size * (2 ** zoom)

    # 1. Longitude calculation
    lon = (x / map_dim) * 360.0 - 180.0

    # 2. Latitude calculation
    y_norm = 1.0 - (2.0 * y / map_dim)
    lat_rad = math.atan(math.sinh(y_norm * math.pi))
    lat = math.degrees(lat_rad)

    return lat, lon

with open('markers.json') as f:
    j = json.load(f)


for it, it_v in j.items():
    for marker in it_v['markers']:
        if not 'tiles' in marker:
            x, y = latlon_to_pixels(marker['coords'][0], marker['coords'][1])
            x *= 0.788574
            y *= 0.788574
            x += 789
            y += 808
            lat, lon = pixels_to_latlon(x, y)
            marker['coords'][0] = lat
            marker['coords'][1] = lon

print(json.dumps(j, indent=4))
