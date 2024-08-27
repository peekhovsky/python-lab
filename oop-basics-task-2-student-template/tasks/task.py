# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.

class SchoolMember:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show(self):
        return f'Name: {self.name}, Age: {self.age}'


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return f'{super().show()}, Salary: {self.salary}'


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: int):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        return f'{super().show()}, Grades: {self.grades}'


if __name__ == '__main__':
    persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

    for person in persons:
        print(person.show())

    assert [person.show() for person in persons] == ["Name: Mr.Snape, Age: 40, Salary: 3000",
                                                     "Name: Harry, Age: 16, Grades: 75"]
