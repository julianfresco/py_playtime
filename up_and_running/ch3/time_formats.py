from datetime import datetime

def main():
  now = datetime.now()

  ### DATE FORMATTING using strftime()
  # %y/%Y - Year
  # %a/%A - Weekday
  # %b/%B - Month
  # %d    - day of month
  print now.strftime("%Y") # full year with century
  print now.strftime("%a, %d %B, %y") # abbrev. day, num, full month, abbrev. year  -  EX: Sun, 07 December, 14

  ### Locale's datetime formatting
  # %c - locale's date and time
  # %x - locale's date
  # %X - locale's time
  print now.strftime("%c")
  print now.strftime("%x")
  print now.strftime("%X")
  
  ### Locale's time formatting
  # %I/%H - 12/24 Hour
  # %M    - minute
  # %S    - second
  # %p    - locale's AM/PM
  print now.strftime("%I:%M:%S %p") # 12-hour:Minute:Second:AM
  print now.strftime("%H:%M") # 24-hour:Minute
  


if __name__ == "__main__":
  main();
