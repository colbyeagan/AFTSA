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
    
def add_day_to_timestamp(timestamp):
    # parse the input timestamp into a datetime object
    dt = datetime.datetime.fromisoformat(timestamp)

    # add one week to the datetime object
    dt = dt + datetime.timedelta(days=1)

    # return the resulting timestamp in the desired format
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def sort_timestamps(timestamps: list):
    """This function takes the list of start and end times in rfc 3339 format, returned from the return_n_random_hour_ranges_sorted function, and sorts the lists in chronological order."""
    # Convert timestamps to datetime objects
    datetimes = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
    # Sort datetime objects
    datetimes.sort()
    # Convert sorted datetime objects back to timestamps
    sorted_timestamps = [dt.strftime("%Y-%m-%dT%H:%M:%SZ") for dt in datetimes]
    return sorted_timestamps

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



def list_of_one_day_ranges_for_rfc_3339_past_year():
    """Generates 365 one day ranges in rfc3339 format starting at the specified date."""
    start_time_list: list = list()
    end_time_list: list = list()
    time1 = datetime.datetime.now()
    time1 = time1.replace(hour=0, minute=0, second=0, microsecond=0)
    time1 = time1 - datetime.timedelta(days=365)
    #time1 = datetime.datetime(2022, 3, 1, 0)
    time1 = time1.strftime("%Y-%m-%dT%H:%M:%SZ")
    for i in range(365):
        start_time_list.append(time1)
        time2 = add_day_to_timestamp(time1)
        end_time_list.append(time2)
        time1 = add_day_to_timestamp(time1)
        
    return start_time_list, end_time_list
        

def one_day_intervals(time_range: int, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0):
    """Generates range days one day ranges in rfc3339 format starting at the specified date."""
    start_time_list: list = list()
    end_time_list: list = list()
    """
    print(f"RANGE: {time_range}")
    print(f"YEAR: {year}")
    print(f"MONTH: {month}")
    print(f"DAY: {day}")
    print(f"HOUR: {hour}")
    print(f"MINUTE: {minute}")
    print(f"SECOND: {second}")
    """
    time1 = datetime.datetime(year, month, day, hour, minute, second)
    time1 = time1.strftime("%Y-%m-%dT%H:%M:%SZ")
    for i in range(time_range):
        start_time_list.append(time1)
        time2 = add_day_to_timestamp(time1)
        end_time_list.append(time2)
        time1 = add_day_to_timestamp(time1)

    return start_time_list, end_time_list

def n_day_intervals(num_of_days: int, time_range: int, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0):
    """Generates range days one day ranges in rfc3339 format starting at the specified date."""
    start_time_list: list = list()
    end_time_list: list = list()
    """
    print(f"RANGE: {time_range}")
    print(f"YEAR: {year}")
    print(f"MONTH: {month}")
    print(f"DAY: {day}")
    print(f"HOUR: {hour}")
    print(f"MINUTE: {minute}")
    print(f"SECOND: {second}")
    """
    print(f"NUM OF Days: {num_of_days}")
    time1 = datetime.datetime(year, month, day, hour, minute, second)
    time1 = time1.strftime("%Y-%m-%dT%H:%M:%SZ")
    tempT = time1
    for i in range(time_range):
        start_time_list.append(time1)
        for _ in range(num_of_days): 
            time2 = add_day_to_timestamp(tempT)
            tempT = time2
        end_time_list.append(time2)
        #for _ in range(num_of_days): 
        time1 = time2
        #time1 = add_day_to_timestamp(time1)

    return start_time_list, end_time_list


def return_n_random_hour_ranges_sorted(n: int) -> list:
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