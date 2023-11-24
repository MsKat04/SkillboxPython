import re
import doctest

def is_valid_date(input_str):
        """
        >> > is_valid_date("20 января 1806")
        True
        >> > is_valid_date("1924, July 25")
        True
        >> > is_valid_date("26/09/1635")
        True
        >> > is_valid_date("3.1.1506")
        True
        >> > is_valid_date("25.08-1002")
        False
        >> > is_valid_date("декабря 19, 1838")
        False
        >> > is_valid_date("8.20.1973")
        False
        >> > is_valid_date("Jun 7, -1563")
        False
        >> > is_valid_date("31 февраля 2023")
        False
        >> > is_valid_date("31 июня 2015")
        False

        """


        date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])[-./](0[1-9]|1[0-2])[-./](\d{4})$')
        match = date_pattern.match(input_str)

        if match:
            day, month, year = map(int, match.groups())
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return 1 <= day <= 31
            elif month in [4, 6, 9, 11]:
                return 1 <= day <= 30
            elif month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    return 1 <= day <= 29
                else:
                    return 1 <= day <= 28
        return False


doctest.testmod()

print(is_valid_date("14.09.2022"))#True
