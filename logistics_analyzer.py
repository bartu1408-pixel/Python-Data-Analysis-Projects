# Delivery routes and their transit times in hours
route_transit_times = {
    "Izmir - Munich": 42,
    "Istanbul - Warsaw": 48,
    "Izmir - Vilnius": 55,
    "Ankara - Budapest": 38,
    "Istanbul - Prague": 40
}

FUEL_PER_HOUR = 15

total_hours = 0
slow_routes = []
fuel_consumed_liters = {}

for key, value in route_transit_times.items():
    total_hours += value
    if value > 45:
        slow_routes.append(key)
    fuel = value * FUEL_PER_HOUR
    fuel_consumed_liters[key] = fuel

average_transit_time = total_hours / len(route_transit_times)


print(f"Average transit time: {average_transit_time:.2f} hours")
print(f"Fuel needed liters: {fuel_consumed_liters}")
print(f"Slow routes: {slow_routes}")
