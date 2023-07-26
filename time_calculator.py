day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, day=""):

  #no time has passed
  if duration == "0:00":
    return start
    
  hr = int(start[:start.index(':')])
  min = int(start[start.index(':')+1:-3])
  time_of_day = start[-2:]
  
  hr_add = int(duration[:duration.index(':')])
  min_add = int(duration[duration.index(':')+1:])
  elapsed_days = int(hr_add/24)

  if (time_of_day == "PM") & (hr < 12):
    hr += 12
  
  new_hr = hr + hr_add%12
  new_min = min + min_add%60
  
  if new_min >= 60:
    new_hr += 1
    new_min = new_min%60

  if new_hr == 12:
    time_of_day = "PM"
  elif new_hr == 24:
    new_hr = 12
    time_of_day = "AM"
    elapsed_days += 1

  if new_hr > 24:
    time_of_day = "AM"
    new_hr = new_hr%24
    elapsed_days += 1

  elif new_hr > 12:
    time_of_day = "PM"
    new_hr = new_hr%12

  

  
  new_time = str(new_hr) + ":"

  if new_min < 10:
    new_time += "0" + str(new_min)
  else:
    new_time += str(new_min)

  new_time += " " + time_of_day

  if day:
    day = day.lower().capitalize()
    day = day_names[(day_names.index(day)+elapsed_days)%7]
    new_time += ", " + day

  if elapsed_days == 0:
    return new_time
  elif elapsed_days == 1:
    new_time += " (next day)"
  else:
    new_time += " (" + str(elapsed_days) + " days later)"

  return new_time