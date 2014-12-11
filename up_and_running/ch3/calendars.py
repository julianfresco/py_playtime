# Note, when you don't use the "from __ import __", then you are telling
# python to get all of the contents of the library

import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)  # uses Sunday as first day
# c = calendar.TextCalendar(calendar.MONDAY)  # uses Monday as first day
str = c.formatmonth(2014, 12, 0, 0)
print str

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
str = hc.formatmonth(2014, 12)
print str

# loop over days of a given month
# zeroes meant that the day of the week is in an overlapping month
for i in c.itermonthdays(2014, 12):
  print i

# The calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
  print name

for day in calendar.day_name:
  print day

# Calculate days based on a rule: For example, condiser a team
# meeting on the first Friday of every month. To figure out what
# days that would be, we can use this script:
for m in range(1, 13):
  # returns an array of weeks that represent the month
  cal = calendar.monthcalendar(2014, m)
  # The first Friday has to be within the first two weeks
  weekone = cal[0]
  weektwo = cal[1]

  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]

  print "%10s %2d" % (calendar.month_name[m], meetday)

  