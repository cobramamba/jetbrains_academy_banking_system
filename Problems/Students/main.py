class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = self.name[0] + self.last_name + str(self.birth_year)


i_name = input()
i_last_name = input()
i_birth_year = input()

stud = Student(i_name, i_last_name, i_birth_year)

print(stud.student_id)
