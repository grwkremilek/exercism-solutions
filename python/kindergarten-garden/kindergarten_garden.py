class Garden:
    STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph",
                    "Kincaid", "Larry"]

    def __init__(self, diagram, students = STUDENTS):
        self.students = sorted(students)
        self.diagram = diagram
        self.all_plants = {
        'C' : 'Clover',
        'G' : 'Grass',
        'R' : 'Radishes',
        'V' : 'Violets' }

    def plants(self, name):
        row1, row2 = self.diagram.split("\n")
        student_idx = self.students.index(name)
        list_plants = [row1[student_idx*2], row1[student_idx*2 + 1],
                       row2[student_idx* 2], row2[student_idx * 2 + 1]]
        for index, i in enumerate(list_plants):
            list_plants[index] = self.all_plants.get(i)
        return list_plants
