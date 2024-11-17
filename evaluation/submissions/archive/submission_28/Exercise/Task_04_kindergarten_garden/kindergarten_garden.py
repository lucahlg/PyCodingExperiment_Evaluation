class Garden:
    def __init__(self, diagram, students):
        self.plant_names = {'G': 'grass', 'C': 'clover', 'R': 'radish', 'V': 'violet'}
        self.students = students
        self.plants = {}
        rows = diagram.split('\n')[1:]
        for i, student in enumerate(students):
            self.plants[student] = []
            for row in rows:
                self.plants[student].extend(row[i*2:i*2+2])
        self.plants = {student: [self.plant_names[plant] for plant in plants] for student, plants in self.plants.items()}

        self.plant_names = {'G': 'grass', 'C': 'clover', 'R': 'radish', 'V': 'violet'}
    def plants(self, student):
        return self.plants[student]
        return self.plants[student]
        return self.plants[student]
        return self.plants[student]
        return self.plants[student]
        return self.plants[student]
