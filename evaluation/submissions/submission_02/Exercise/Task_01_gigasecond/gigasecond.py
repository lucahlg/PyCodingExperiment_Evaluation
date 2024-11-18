from datetime import datetime, timedelta

def add(moment):
    return moment + timedelta(seconds=1_000_000_000)

# Given birth date and time
birth_datetime = datetime(2015, 1, 24, 22, 0, 0)

# Calculating the gigasecond date
gigasecond_datetime = add(birth_datetime)

print(gigasecond_datetime)  # Output: 2046-10-02 23:46:40
