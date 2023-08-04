def is_leap_year(year):
    """Is this year a leap year?"""

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    

def days_in_month(date):
    "How many days are there in a month?"

    # initialize a dict with months and corresponding days as key-value pairs
    days_dict = {
        '01': 31,
		'02': 29,
		'03': 31,
		'04': 30,
		'05': 31,
		'06': 30,
		'07': 31,
		'08': 31,
		'09': 30,
		'10': 31,
		'11': 30,
		'12': 31
    }

    # separate the month and date
    month_date_split = date.split()
    month = month_date_split[0]
    year = month_date_split[1]

    # use the month as a key to retrieve number of days
    days = days_dict[month]

    # check if year is a leap year (first convert year to a num)
    if is_leap_year(int(year)) is True:
        days -= 1
    
    print(f"{date} has {days} days in it.")