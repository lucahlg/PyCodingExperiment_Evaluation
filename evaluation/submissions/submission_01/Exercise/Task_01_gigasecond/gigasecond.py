from datetime import datetime, timedelta


def add(moment):
    # Define a gigasecond using underscore notation for readability
    gigasecond = 1_000_000_000

    # Add gigasecond to the input datetime
    return moment + timedelta(seconds=gigasecond)



geburtstag = datetime(2004, 9, 26, 23, 30, 0)

print(add(geburtstag))