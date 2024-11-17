class Garden:
    def __init__(self, diagram, students):
        self.students = students
        self.plants = self.decode(diagram)
    def decode(self, diagram):
        diagram = diagram.split('\n')
        plant_map = {'G': 'grass', 'C': 'clover', 'R': 'radish', 'V': 'violet'}
        rows = diagram[1:]
        plants = ''.join(rows).replace('[','').replace(']','')
        return [plant_map[plant] for plant in plants if plant in plant_map]
    def plants_of(self, student):
        index = self.students.index(student) * 2
        return self.plants[index:index + 4]
