class Garden:
    def __init__(self, diagram, students):
        self.students = students
        self.plants = self.parse_diagram(diagram)

    def parse_diagram(self, diagram):
        # Split the diagram into rows and remove the first two lines (windows)
        rows = diagram.strip().splitlines()[2:]
        # Join the rows to get a single string of plants
        plant_string = ''.join(rows)
        return plant_string

    def plants_for(self, student):
        index = self.students.index(student) * 4  # Each student has 4 plants
        return [self.plants[i] for i in range(index, index + 4)]

