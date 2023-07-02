from sys import argv

__all__ = ['check_date', 'check_leap_year']


def check_date(date):
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            if 1 <= day <= 28 + check_leap_year(year):
                return True
    return False


def check_leap_year(year):
    return not year % 4 != 0 or year % 100 == 0 and year % 400 != 0


if __name__ == "__main__":
    name, *arg = argv
    print(check_leap_year(2012))
    print(check_date('31.04.2002'))
