class Garden:
    def __init__(self, diagram, students):
        self.students = students
        self.diagram = diagram.split('\n')[2:]
        self.plants = {'G': 'grass', 'C': 'clover', 'R': 'radish', 'V': 'violet'}

    def get_plants(self, student):
        index = self.students.index(student) * 2
        return [self.plants[plant] for row in self.diagram for plant in row[index:index + 2]]
