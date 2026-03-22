from datetime import datetime


def get_days_from_today(date_str: str) -> int:
    """
    Function that returns the number of days between the current and given date.
    If given date already passed returns negative number of days.
    In case of invalid date input prints corresponding message and returns None.
    """

    try:
        converted_date = datetime.strptime(date_str, "%Y-%m-%d").date()  # Converting date to datetime object
    except ValueError:
        print("Invalid given date or format, date for get_days_from_today function should be valid and in YYYY-MM-DD format")
        return None

    current_date = datetime.today().date()  # Getting current date
    return (converted_date - current_date).days
