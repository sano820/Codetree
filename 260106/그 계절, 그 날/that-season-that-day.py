Y, M, D = map(int, input().split())

# Please write your code here.
def is_youn(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def is_valid_date(y, m, d):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_youn(y):
        days_in_month[2] = 29

    if 1 <= m <= 12 and 1 <= d <= days_in_month[m]:
        return True
    return False


def get_season(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    else:
        return "Winter"


if not is_valid_date(Y, M, D):
    print(-1)
else:
    print(get_season(M))
