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

For N random non-overlapping time stamps within a certain time range
```python
from AFTSA import randoms
```
For specified intervals between time stamps up to N time stamps or for a specified range
```python
from AFTSA import randoms
```

This package currently supports rfc3339 timestamp generation in the %Y-%m-%dT%H:%M:%SZ format. More timestamp formats can easily be added by cloning from github and changing the "return dt.strftime("%Y-%m-%dT%H:%M:%SZ")" statements across the functions you need. 

Main functions in intervals  


```python
from AFTSA import randoms

dateLists = intervals.list_of_one_day_ranges_for_rfc_3339_past_year()
```