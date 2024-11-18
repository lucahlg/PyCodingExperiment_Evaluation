def day_to_ordinal(day):
    """Convert day number to its ordinal representation."""
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    return ordinals[day - 1]


def cumulative_gifts(day, gifts):
    """Recursive function to build the gifts text."""
    if day == 1:
        return gifts[0]  # Base case: the first day's gift
    return f"{gifts[day - 1]}{cumulative_gifts(day - 1, gifts)}"


def verse(day):
    """Construct the verse for a given day."""
    ordinal = day_to_ordinal(day)
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]
    gifts_text = cumulative_gifts(day, gifts)
    return f"On the {ordinal} day of Christmas my true love gave to me: {gifts_text}"


def recite(start_verse, end_verse):
    """Return the verses from start_verse to end_verse."""
    return [verse(day) for day in range(start_verse, end_verse + 1)]


# Example usage
print("\n\n".join(recite(1, 12)))


