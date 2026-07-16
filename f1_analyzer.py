race_data = {
    "Verstappen": [82.5, 81.3, 82.1, 80.8, 81.0, 81.5],
    "Hamilton": [83.1, 81.9, 81.5, 81.2, 80.9, 81.1],
    "Alonso": [82.8, 82.0, 81.1, 81.0, 80.7, 81.4],
    "Leclerc": [83.5, 82.1, 81.8, 81.9, 81.2, 81.0],
    "Norris": [82.1, 81.5, 81.0, 80.9, 80.8, 81.1],
    "Perez": [83.0, 82.5, 82.1, 81.8, 81.9, 82.0],
    "Sainz": [82.9, 81.8, 81.4, 81.1, 81.3, 81.0],
    "Russell": [83.2, 82.0, 81.7, 81.5, 81.1, 81.3]
}
fasted_lap_time = 999.0
fastest_driver = ""
average_laps = {}

for driver, laps in race_data.items():
    average_lap_time = sum(laps) / len(laps)
    for lap in laps:
        if lap < fasted_lap_time:
            fasted_lap_time = lap
            fastest_driver = driver
        average_laps[driver] = round(average_lap_time, 2)



print(f"The average lap time is {average_laps}")
print(f"The fastest driver is {fastest_driver} with a lap time of {fasted_lap_time:.2f} seconds")
