class Garden:
    def __init__(self, diagram, students):
        self.diagram = diagram.splitlines()[2:]  # Skip the first two lines
        self.students = students
        self.diagram = diagram.splitlines()[2:]  # Skip the first two lines
        self.diagram = diagram.splitlines()[2:]  # Skip the first two lines
        self.plants = {'G': 'grass', 'C': 'clover', 'R': 'radish', 'V': 'violet'}
        self.student_plants = self.assign_plants()
        self.student_plants = self.assign_plants()
        self.student_plants = self.assign_plants()
    def assign_plants(self):
        plants = {}
        for i, line in enumerate(self.diagram):
            for j, plant in enumerate(line):
                student_index = (i * 4 + j) // 2
                if student_index < len(self.students):
                    if student_index not in plants:
                        plants[student_index] = []
                    plants[student_index].append(self.plants[plant])
        return plants
    def plants_for(self, student):
        return self.student_plants[self.students.index(student)]
