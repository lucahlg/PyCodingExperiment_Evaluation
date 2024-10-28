from kindergarten_garden import Garden

# Test data
diagram = """
[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
"""
students = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
]

# Create an instance of Garden
garden = Garden(diagram, students)

# Test plants for each student
print("Calculated plants for each student:")
print(f"Alice's plants: {garden.plants_for('Alice')}")
print(f"Bob's plants: {garden.plants_for('Bob')}")
print(f"Charlie's plants: {garden.plants_for('Charlie')}")
print(f"David's plants: {garden.plants_for('David')}")

# Test plants for each student
assert garden.plants_for("Alice") == ['V', 'R', 'C', 'G'], "Alice's plants should be Violets, Radishes, Clover, Grass"
assert garden.plants_for("Bob") == ['C', 'G', 'C', 'G'], "Bob's plants should be Clover, Grass, Clover, Grass"
assert garden.plants_for("Charlie") == ['V', 'R', 'C', 'G'], "Charlie's plants should be Violets, Radishes, Clover, Grass"
assert garden.plants_for("David") == ['G', 'C', 'G', 'C'], "David's plants should be Grass, Clover, Grass, Clover"

print("All tests passed!")

