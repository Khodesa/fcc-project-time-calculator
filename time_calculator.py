def add_time(start, duration, day=False):
  hr, min = start.split(":")
  min, anno = min.split(" ")
  hr, min = int(hr), int(min)
  durHr, durMin = duration.split(":")
  durHr, durMin = int(durHr), int(durMin)
  n = 0
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  min += durMin

  if min > 59:
    min, hr = min % 60, hr + min // 60

  hr += durHr
  for x in range(hr // 12):
    if anno == "PM":
      anno = "AM"
      n += 1
    elif anno == "AM":
      anno = "PM"
      
  if hr % 12 == 0:
    hr = 12
  elif hr > 12:
    hr = hr % 12
        
  if min < 10:
    min = f"0{min}"
    
  new_time = f'{hr}:{min} {anno}'

  if day:
    m = 0
    i = days.index(day.lower())
    if i + n > 6:
      m = (i + n) % 7
      new_time += f", {days[m].capitalize()}"
    else:
      new_time += f", {days[i + n].capitalize()}"

  if n:
    if n == 1:
      new_time += " (next day)"
    else:
      new_time += f" ({n} days later)"
        
  return new_time