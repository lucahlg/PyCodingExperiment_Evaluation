def hexa(hex_string):
    """
    Wandelt eine hexadezimale Zahl, dargestellt als String, in ihre Dezimalzahl um.

    :param hex_string: Die hexadezimale Zahl als String (kann Leerzeichen enthalten).
    :return: Die Dezimalzahl.
    :raises ValueError: Wenn der String ungültige hexadezimale Zeichen enthält.
    """
    # Entferne alle Leerzeichen und mache den String klein
    hex_string = hex_string.strip().lower()

    # Überprüfe, ob der String nur gültige hexadezimale Zeichen enthält (0-9, a-f)
    if not all(c in '0123456789abcdef' for c in hex_string):
        raise ValueError("Ungültiger hexadezimaler String")

    # Initialisiere den Dezimalwert
    decimal_value = 0
    length = len(hex_string)

    # Iteriere durch jede Stelle des hexadezimalen Strings
    for i, char in enumerate(hex_string):
        # Bestimme den Wert der aktuellen hexadezimalen Stelle
        if '0' <= char <= '9':
            value = ord(char) - ord('0')  # Umwandlung der Ziffer in ihren Dezimalwert
        else:
            value = ord(char) - ord('a') + 10  # Umwandlung der Buchstaben (a-f) in ihren Dezimalwert

        # Berechne den Beitrag dieser Stelle zur Gesamtzahl
        power = length - 1 - i
        decimal_value += value * (16 ** power)

    return decimal_value


# Beispielaufrufe
try:
    print(hexa("10af8c"))  # Ausgabe: 1107548
    print(hexa("1a3"))  # Ausgabe: 419
    print(hexa("7f"))  # Ausgabe: 127
except ValueError as e:
    print(e)
