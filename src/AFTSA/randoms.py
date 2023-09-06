import time
import datetime
import random

"""This code cell contains two functions (is_leap_year and random_date) which help generate a random one hour date range when random_date() is called"""
def is_leap_year(year: int):
    """Returns True if the given year in typical four digit year format (i.e. 2023) is a leap year, False otherwise."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def random_date():
    """Generate a random one hour date range within the last year in RFC 3339 format to be used with API."""
    month = random.randint(1, 12)
    year = random.randint(datetime.datetime.now().year - 1, datetime.datetime.now().year)
    if month <= datetime.datetime.now().month:
        year = datetime.datetime.now().year
    else:
        year = datetime.datetime.now().year - 1
    if month == datetime.datetime.now().month:
        if datetime.datetime.now().day <= 2:
            day = 1
        else:
            day = random.randint(1, datetime.datetime.now().day - 1)
    elif month == 2:
        if is_leap_year(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    hour = random.randint(0, 23)
    start_time = datetime.datetime(year, month, day, hour)
    end_time = start_time + datetime.timedelta(hours=1)
    start_timestamp = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_timestamp = end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    return start_timestamp, end_timestamp

def random_date_n(n: int):
    """Generate a random one hour date range within the last year in RFC 3339 format to be used with API."""
    month = random.randint(1, 12)
    year = random.randint(datetime.datetime.now().year - 1, datetime.datetime.now().year)
    if month <= datetime.datetime.now().month:
        year = datetime.datetime.now().year
    else:
        year = datetime.datetime.now().year - 1
    if month == datetime.datetime.now().month:
        if datetime.datetime.now().day <= 2:
            day = 1
        else:
            day = random.randint(1, datetime.datetime.now().day - 1)
    elif month == 2:
        if is_leap_year(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    hour = random.randint(0, 23)
    start_time = datetime.datetime(year, month, day, hour)
    end_time = start_time + datetime.timedelta(hours=n)
    start_timestamp = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_timestamp = end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    return start_timestamp, end_timestamp

def sort_timestamps(timestamps: list):
    """This function takes the list of start and end times in rfc 3339 format, returned from the return_n_random_hour_ranges_sorted function, and sorts the lists in chronological order."""
    # Convert timestamps to datetime objects
    datetimes = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
    # Sort datetime objects
    datetimes.sort()
    # Convert sorted datetime objects back to timestamps
    sorted_timestamps = [dt.strftime("%Y-%m-%dT%H:%M:%SZ") for dt in datetimes]
    return sorted_timestamps

def n_random_hour_ranges_sorted(n: int) -> list:
    """This returns two SORTED lists of start times and end times (where each index of the end time is one hour after the same index in start time)."""
    """This function returns n number of one hour ranges."""
    start_time1_list: list = list()
    end_time1_list: list = list()
    for i in range(0, n):
        s1, s2 = random_date()
        while s1 in start_time1_list:
            s1, s2 = random_date()
        start_time1_list.append(s1)
        end_time1_list.append(s2)

    sorted_start = sort_timestamps(start_time1_list)
    sorted_end = sort_timestamps(end_time1_list)
    return (sorted_start, sorted_end)

def n_random_m_ranges(n: int, range_len_m: int):
    """This returns two SORTED lists of start times and end times (where each index of the end time is range_len hours after the same index in start time."""
    """This function returns n number of one hour ranges in the last year."""
    start_time1_list: list = list()
    end_time1_list: list = list()
    for i in range(0, n):
        s1, s2 = random_date_n(range_len)
        while s1 in start_time1_list:
            s1, s2 = random_date_n(range_len)
        start_time1_list.append(s1)
        end_time1_list.append(s2)
    sorted_start = sort_timestamps(start_time1_list)
    sorted_end = sort_timestamps(end_time1_list)
    return (sorted_start, sorted_end)