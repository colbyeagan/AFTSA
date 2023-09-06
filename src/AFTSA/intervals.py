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


