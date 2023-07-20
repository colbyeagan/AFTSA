from AFTSA import funcs

#, 2021, 10, 2, 5, 45

#dateList = funcs.list_of_one_day_ranges_for_rfc_3339_since_specific_date(365, 2021, 10, 2, 5, 45)
dateList = funcs.n_day_intervals(10, 365, 2021, 10, 2, 5, 45)

for i in range(len(dateList[0])):
    print(f"{dateList[0][i]} --- {dateList[1][i]}")