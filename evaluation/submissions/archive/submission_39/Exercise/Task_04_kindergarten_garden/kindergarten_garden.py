class Garden:
    
    def __init__(self, diagram, students):
        def __init__(self, diagram, students):
        self.diagram = diagram.splitlines()
        self.students = students
        self.plants = self._parse_plants()

    def _parse_plants(self):
        plant_map = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
        plants = {}
        for i, student in enumerate(self.students):
            plants[student] = []
            row = i // 2
            col = (i % 2) * 2
            plants[student].extend([plant_map[self.diagram[row][col]], plant_map[self.diagram[row][col + 1]]])
        return plants
