# put your python code here
walk_hours = int(input())
walk_minutes = int(input())
walk_seconds = int(input())
rain_hours = int(input())
rain_minutes = int(input())
rain_seconds = int(input())
walk_time = walk_hours*3600 + walk_minutes*60 + walk_seconds
rain_time = rain_hours*3600 + rain_minutes*60 + rain_seconds
print(rain_time - walk_time)
