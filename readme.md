# AFTSA - APIs for Time Series Analysis

- Docs in progress

## Getting Started

- Python 3.11 package -- Must run in python 3.11

```
pip install AFTSA  
```
or  
```
pip3.11 install AFTSA
```

The usage of this package is simple.   

For functions to do randomized time series analysis
```python
from AFTSA import randoms
```
For functions to do specified intervals time series analysis
```python
from AFTSA import randoms
```

This package currently supports rfc3339 timestamp generation in the %Y-%m-%dT%H:%M:%SZ format. More timestamp formats can easily be added by cloning from github and changing the "return dt.strftime("%Y-%m-%dT%H:%M:%SZ")" statements across the functions you need. 

## Main functions in intervals  

### intervals.list_of_one_day_ranges_for_rfc_3339_past_year()

intervals.list_of_one_day_ranges_for_rfc_3339_past_year() is the most straight forward function, taking no arguments. It 
simply returns two arrays where returnValue[0] is the array of start times and returnValue[1] is the array of end times. This function reads your machine's local clock and returns one day ranges in rfc3339 time format for the prior calendar year from the time you call it.
```python
from AFTSA import randoms

dateLists = intervals.list_of_one_day_ranges_for_rfc_3339_past_year()
```

### intervals.one_day_intervals(...)

intervals.one_day_intervals(time_range: int, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0)  
returns time_range amount of days of time stamps after the specified date in the remaining arguments. Only up to the day is a required argument. If no hour or more specific range is specified then the timestamps will default to the beginning of the day at hour zero.  
```python
# returns two arrays both with 100 days of timestamps starting on october 5th 2020 at 15:45 (3:45pm). All of the days start at this time and the end times end at this time the next day
dateLists = intervals.one_day_intervals(100, 2020, 10, 5, 15, 45)

for i in range(len(dateLists[0])):
    print(f"{dateLists[0][i]} -- {dateLists[1][i]}")

# Prints
"""
2020-10-05T15:45:00Z -- 2020-10-06T15:45:00Z
2020-10-06T15:45:00Z -- 2020-10-07T15:45:00Z
2020-10-07T15:45:00Z -- 2020-10-08T15:45:00Z
2020-10-08T15:45:00Z -- 2020-10-09T15:45:00Z
2020-10-09T15:45:00Z -- 2020-10-10T15:45:00Z
2020-10-10T15:45:00Z -- 2020-10-11T15:45:00Z
...
2021-01-09T15:45:00Z -- 2021-01-10T15:45:00Z
2021-01-10T15:45:00Z -- 2021-01-11T15:45:00Z
2021-01-11T15:45:00Z -- 2021-01-12T15:45:00Z
2021-01-12T15:45:00Z -- 2021-01-13T15:45:00Z
"""
```

### intervals.n_day_intervals(...)

intervals.n_day_intervals(num_of_days: int, time_range: int, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0): works the same as intervals.one_day_intervals() except there is an extra argument on the beginning where the duration of each range can be changed in increments of one day. In the example below you can see how each range now increments by 5 days each time.

```python
dateLists = intervals.n_day_intervals(5, 100, 2020, 10, 5, 15, 45)
for i in range(len(dateLists[0])):
    print(f"{dateLists[0][i]} -- {dateLists[1][i]}")

# Prints
"""
2020-10-05T15:45:00Z -- 2020-10-10T15:45:00Z
2020-10-10T15:45:00Z -- 2020-10-15T15:45:00Z
2020-10-15T15:45:00Z -- 2020-10-20T15:45:00Z
2020-10-20T15:45:00Z -- 2020-10-25T15:45:00Z
2020-10-25T15:45:00Z -- 2020-10-30T15:45:00Z
...
2022-01-28T15:45:00Z -- 2022-02-02T15:45:00Z
2022-02-02T15:45:00Z -- 2022-02-07T15:45:00Z
2022-02-07T15:45:00Z -- 2022-02-12T15:45:00Z
"""
```

## Main functions in randoms

### randoms.random_date()

randoms.random_date() returns a tuple with a random one hour time range in the past year
```python
randomHourRange = randoms.random_date()
print(randomHourRange)

# Prints
"""
('2022-11-16T00:00:00Z', '2022-11-16T01:00:00Z')
"""
```

### randoms.random_date_n(n: int)

randoms.random_date_n(n: int) also returns a tuple with a random one hour time range in the past year, however the argument n adjusts the duration of the interval in hour increments. 
```python
randomHourRange = randoms.random_date_n(5)
print(randomHourRange)

# Prints
"""
('2023-06-10T22:00:00Z', '2023-06-11T03:00:00Z')
"""
# The interval is a 5 hour time range instead of just 1 hour like with randoms.random_date()
```

### randoms.n_random_hour_ranges_sorted(n: int)

randoms.n_random_hour_ranges_sorted(n: int) returns two lists of n random start times and end times (where each start time is one hour before the matching end time) within the past year (month rounding, ie if you are in September the time stamps start in October). A non month-rounding version is in the works.

```python
# Will make 100 random one hour timestamp ranges in the past year (non overlapping)
randomDates = randoms.n_random_hour_ranges_sorted(100)
for i in range(len(randomDates[0])):
    print(f"{randomDates[0][i]} -- {randomDates[1][i]}")

# Prints
"""
2022-10-03T05:00:00Z -- 2022-10-03T06:00:00Z
2022-10-03T23:00:00Z -- 2022-10-04T00:00:00Z
2022-10-08T15:00:00Z -- 2022-10-08T16:00:00Z
2022-10-16T06:00:00Z -- 2022-10-16T07:00:00Z
2022-10-18T05:00:00Z -- 2022-10-18T06:00:00Z
...
2023-09-03T11:00:00Z -- 2023-09-03T12:00:00Z
2023-09-03T18:00:00Z -- 2023-09-03T19:00:00Z
2023-09-03T21:00:00Z -- 2023-09-03T22:00:00Z
2023-09-05T21:00:00Z -- 2023-09-05T22:00:00Z
"""
```