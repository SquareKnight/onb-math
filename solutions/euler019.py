"""Counting Sundays

#Date
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.

- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.

- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""


import datetime


def attempt_4():
    date_params = [(y, m, 1) for y in range(1901, 2001) for m in range(1, 13)]
    dates = [d for d in [datetime.date(y, m, d) for (y, m, d) in date_params] if d.weekday()==6]
    return len(dates)


def attempt_3():
    return (1/7)*12*100//1



def attempt_2():
    d = datetime.date(1901, 1, 1)
    total = 0
    while d.year < 2001:
        total += 1 if d.weekday() == 6 else 0
        y, m = d.year, d.month
        if m == 12:
            y += 1
            m = 1
        else:
            m += 1
        d = datetime.date(y, m, 1)

    return total


def attempt_1():
    total = 0
    d = 1       # mondays are 1 in our count
    year = 1900 # and we start at January (1900) because we know that's a monday
    month = 0   # NOTE that jan == 0 and feb == 1  ... dec == 11 because we use it as an array index

    adds = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0

    while i < (12*101):
        i += 1
        if d % 7 == 0 and i > 12:   # if we are on a sunday and the year is 1901 or later
            total += 1

        if month == 1: #feb
            if year % 400 == 0:
                d = d + 29
            elif year % 100 == 0:
                d = d + 28
            elif year % 4 == 0:
                d = d + 29
            else:
                d = d + 28
        else:
            d = d + adds[month]
            if month == 11:
                month = -1
                year += 1
        month = month + 1

    return total


def run():
    return attempt_4()


if __name__ == '__main__':
    print(run())