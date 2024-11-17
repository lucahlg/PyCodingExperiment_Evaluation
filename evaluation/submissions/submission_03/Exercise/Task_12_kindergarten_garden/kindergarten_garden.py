class Garden:
    def __init__(self, diagram, students):
        self.diagram = diagram
        self.students = students
        self.plants = self._parse_diagram(diagram)

    def _parse_diagram(self, diagram):
        plant_mapping = {'G': 'grass', 'C': 'clover', 'R': 'radish', 'V': 'violet'}
        rows = diagram.split('\n')
        plants = []
        for row in rows:
            for char in row:
                if char in plant_mapping:
                    plants.append(plant_mapping[char])
        return plants

    def plants_for(self, student):
        index = self.students.index(student) * 4
        return self.plants[index:index + 4]
