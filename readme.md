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