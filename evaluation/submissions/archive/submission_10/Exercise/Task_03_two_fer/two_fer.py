def two_fer(name):
    pass
    if not name:  # Wenn der Name leer ist
        name = "you"
    return f"One for {name}, one for me."

# Hauptprogramm
name = input("Wie heißt dein Gegenüber? ").strip()
print(two_fer(name))

