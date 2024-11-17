class Garden:
    def __init__(self, diagram, students):
        self.diagram = diagram
        self.students = students
        self.plants = self._assign_plants()

    def _assign_plants(self):
        plant_map = {'G': 'grass', 'C': 'clover', 'R': 'radish', 'V': 'violet'}
        plants = {}
        for i, student in enumerate(self.students):
            start = i * 4
            end = start + 4
            plants[student] = [plant_map[plant] for plant in self.diagram[start:end]]
        return plants

    def plants_for(self, student):
        return self.plants[student]
