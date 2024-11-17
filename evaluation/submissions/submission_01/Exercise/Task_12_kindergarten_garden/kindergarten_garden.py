class Garden:
    def __init__(self, diagram, students):
        self.diagram = diagram
        self.students = students
        self.plants = self._assign_plants()
    def _assign_plants(self):
        plant_map = {'G': 'Grass', 'C': 'Clover', 'R': 'Radish', 'V': 'Violet'}
        plants = {}
        for i, student in enumerate(self.students):
            start = i * 4
            end = start + 4
            plants[student] = [plant_map[plant] for plant in self.diagram[start:end]]
        return plants

    def plants(self, student):
        return self.plants.get(student, [])
# Example usage:
# garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV", ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"])
# print(garden.plants("Alice"))