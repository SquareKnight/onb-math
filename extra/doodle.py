import datetime

d = datetime.date(1901, 1, 1)

count_sundays = 0
while d.year < 2001:
    count_sundays += (d.weekday() == 6)
    d = datetime.date(d.year + (d.month==12), (d.month + 1) if d.month < 12 else 1, 1)

print(count_sundays)