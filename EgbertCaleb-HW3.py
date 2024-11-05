#Caleb Egbert

# 12

# 11/5/2024

#Sources, help given to/received from


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def is_valid_date(month, day, year):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if is_leap_year(year):
        month_days[2] = 29

    if month < 1 or month > 12 or day < 1 or day > month_days.get(month, 0):
        return False
    return True

def jan_first_day(year):
    y = year - 1
    return (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7

def day_of_week(month, day, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29

    jan_1st_day = jan_first_day(year)

    days_passed = sum(days_in_month[:month - 1]) + (day - 1)
    return (jan_1st_day + days_passed) % 7

def main():
    date = input("Enter a date (MM/DD/YYYY): ")
    try:
        month, day, year = map(int, date.split('/'))
    except ValueError:
        print(f"{date} Invalid Date")
        return

    if not is_valid_date(month, day, year):
        print(f"{date} Invalid Date")
        return

    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_of_week_index = day_of_week(month, day, year)
    print(f"{date} {week_days[day_of_week_index]}")

if __name__ == "__main__":
    main()
