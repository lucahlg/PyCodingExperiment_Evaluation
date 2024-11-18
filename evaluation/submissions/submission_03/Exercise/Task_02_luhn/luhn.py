class Luhn:
    def __init__(self, card_num):
        """
        Initialisiert die Klasse mit der Kartennummer.

        :param card_num: Die Kartennummer als String (kann Leerzeichen enthalten).
        """
        self.card_num = card_num

    def valid(self):
        """
        Überprüft, ob die Kartennummer nach dem Luhn-Algorithmus gültig ist.

        :return: True, wenn die Nummer gültig ist, andernfalls False.
        """
        # Entferne Leerzeichen aus der Kartennummer
        cleaned_number = self.card_num.replace(" ", "")

        # Prüfe, ob die Eingabe nur Ziffern enthält und länger als 1 Zeichen ist
        if not cleaned_number.isdigit() or len(cleaned_number) <= 1:
            return False

        # Wandle die Zeichenkette in eine Liste von Ganzzahlen um
        digits = list(map(int, cleaned_number))

        # Luhn-Algorithmus anwenden
        checksum = 0
        is_second = False  # Markiert jede zweite Ziffer von rechts

        for digit in reversed(digits):
            if is_second:
                doubled = digit * 2
                if doubled > 9:
                    doubled -= 9
                checksum += doubled
            else:
                checksum += digit

            is_second = not is_second  # Flag umkehren

        # Gültig, wenn die Prüfsumme durch 10 teilbar ist
        return checksum % 10 == 0


# Beispiele
print(Luhn("4539 3195 0343 6467").valid())  # Ausgabe: True (gültig)
print(Luhn("8273 1232 7352 0569").valid())  # Ausgabe: False (ungültig)
print(Luhn("1").valid())  # Ausgabe: False (zu kurz)
print(Luhn("abc123").valid())  # Ausgabe: False (ungültige Zeichen)
