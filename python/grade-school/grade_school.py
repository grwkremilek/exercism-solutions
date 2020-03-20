from collections import defaultdict

class School:
    def __init__(self):
        self.school = defaultdict(list)

    def add_student(self, name, grade):
        self.school[grade].append(name)

    def roster(self):
        out = []
        for key in sorted(self.school.keys()):
            out += self.grade(key)
        return out

    def grade(self, grade_number):
        return sorted(self.school[grade_number])
