"""
Problem 19
https://projecteuler.net/problem=19

Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

DAYS_PER_MONTH = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
    ]

def main():
    count_of_sundays_on_first = 0

    dow_first = 1     # 01/01/1900 is Monday
    for y in range(1900, 2001):
        for m in range(12):
            if y == 1900 and m == 0:
                continue

            dow_first = dow_of_first(dow_first_last_month=dow_first,
                month=m, year= y)

            if y > 1900:
                if dow_first == 0:
                    count_of_sundays_on_first += 1

            # print(m, y, dow_first)

    print(count_of_sundays_on_first)


def is_leap_year(year: int):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

def dow_of_first(dow_first_last_month: int, month: int, year: int):
    # print(month)
    if month == 0:
        days = DAYS_PER_MONTH[11]
    elif month == 2:
        if is_leap_year(year=year):
            days = 29
        else:
            days = DAYS_PER_MONTH[month - 1]
    else:
        days = DAYS_PER_MONTH[month - 1]


    return ((dow_first_last_month + (days % 7)) % 7)


if __name__ == "__main__":
    main()
