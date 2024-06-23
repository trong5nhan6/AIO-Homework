class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student: Name={self.name}, YOB={self.yob}, Grade={self.grade}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher: Name={self.name}, YOB={self.yob}, Subject={self.subject}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor: Name={self.name}, YOB={self.yob}, Specialist={self.specialist}"


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            print(person.describe())

    def count_doctor(self):
        count = sum(1 for person in self.people if isinstance(person, Doctor))
        return count

    def sort_age(self):
        return self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        teacher_yob = [teacher.yob for teacher in teachers]
        if not teacher_yob:
            return 0
        else:
            return sum(teacher_yob) / len(teacher_yob)


student1 = Student(name=" studentA ", yob=2010, grade="7")

teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")

doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")

ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"Number of doctors: {ward1.count_doctor()}")

print("\ nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

print(f"Average year of birth (teachers): {ward1.compute_average()}")
