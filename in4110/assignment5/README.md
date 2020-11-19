# Assignment 5

## Dependencies

- re
- bs4
- matplotlib
- requests

## To Get the Reports

All the files that are supposed to create the reports are runnable as 'main':

- python3 requesting_urls.py
- python3 filter_urls.py
- python3 collect_dates.py
- python3 time_planner.py
- python3 fetch_player_statistics.py

## Task 5.3

The date formats being parsed:

- DD MONTH YYY
- MONTH DD, YYYY
- M/D/YYYY
- MM/DD/YYYY
- M/D YYYY
- MM/DD YYYY

> Any 4-digit integer less than 2030 is considered to be a 'year'. Dublicate dates are
>dropped.

## Task 5.5

In fetch player statistics there is a function that collects all the data required
to plot the charts extract_data(). In order to save time the output from this function
is stored in player_data.py as an object. You can rerun this function if necessary (
see the comments in fetch_player_statistics.py).

Pages for some players have a different layout, they were just discarded and their
respective statistics set to zeroes.

players_data.py