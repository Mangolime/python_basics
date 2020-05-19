time = int(input('Time: '))
time_hours = time // 3600
time_rest = time % 3600
time_minutes = time_rest // 60
time_seconds = time_rest % 60
print(f"{time_hours}:{time_minutes}:{time_seconds}")
