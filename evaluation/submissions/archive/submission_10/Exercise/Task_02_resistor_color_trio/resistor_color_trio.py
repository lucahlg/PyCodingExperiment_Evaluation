def label(colors):
    # Farben zu Nummern
    color_to_digit = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    # Farben in Zahlen umwandeln
    first_color = color_to_digit[colors[0]]
    second_color = color_to_digit[colors[1]]
    third_color = color_to_digit[colors[2]]

    # Zahl berechnen: Erste Farbe + Zweite Farbe + Dritte Farbe als 0er Anhängsel
    resistance_value = (first_color * 10 + second_color) * (10 ** third_color)

    # Ausgabe je nach Größe der Zahl
    if resistance_value >= 1000000:
        value = resistance_value / 1000000
        unit = "megaohms"
    elif resistance_value >= 1000:
        value = resistance_value / 1000
        unit = "kiloohms"
    else:
        return f"{resistance_value} ohms"

    # Entfernen der Dezimalstellen, falls es eine ganze Zahl ist
    if value.is_integer():
        return f"{int(value)} {unit}"
    else:
        return f"{value} {unit}"

# Interaktive Abfrage der Farben
def get_colors():
    first_color = input("Gib die erste Farbe ein: ").lower()
    second_color = input("Gib die zweite Farbe ein: ").lower()
    third_color = input("Gib die dritte Farbe ein: ").lower()

    return [first_color, second_color, third_color]

# Farben abfragen und Ergebnis anzeigen
colors = get_colors()
result = label(colors)
print(result)
