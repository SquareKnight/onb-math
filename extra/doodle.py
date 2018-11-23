import datetime

list_of_date_params = [(y, m, 1) for m in range(1, 13) for y in range(1901, 2001)]
list_of_dates = [d for d in [datetime.date(y, m, d) for (y, m, d) in list_of_date_params] if d.weekday() == 6]
print(len(list_of_dates))