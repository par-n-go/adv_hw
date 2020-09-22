from abc import ABC, abstractmethod
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Persona(ABC):

    @abstractmethod
    def show_info(self):
        pass

    def get_age(self):
        return relativedelta(datetime.now(),self.birthday).years

class Student(Persona):

    def __init__(self, surname, birthday, fakultet, kurs):
        self.surname = surname
        self.birthday = datetime.strptime(birthday,'%d/%m/%Y')
        self.fakultet = fakultet
        self.kurs = kurs

    def __str__(self):
        return f"{self.surname}"

    def show_info(self):
        return f"{self.surname} was born on {self.birthday} and is studying in {self.fakultet} ({self.kurs})"

    #def get_age(self):
    #    return relativedelta(datetime.now(),self.birthday).years

class Abiturient(Persona):

    def __init__(self, surname, birthday, fakultet):
        self.surname = surname
        self.birthday = datetime.strptime(birthday,'%d/%m/%Y')
        self.fakultet = fakultet

    def __str__(self):
        return f"{self.surname}"

    def show_info(self):
        return f"{self.surname} was born on {self.birthday} and is studying in {self.fakultet}"

    #def get_age(self):
    #    return relativedelta(datetime.now(),self.birthday).years


class Teacher(Persona):

    def __init__(self, surname, birthday, fakultet, dolzhnost, staz):
        self.surname = surname
        self.birthday = datetime.strptime(birthday,'%d/%m/%Y')
        self.fakultet = fakultet
        self.dolzhnost = dolzhnost
        self.staz = staz

    def __str__(self):
        return f"{self.surname}"

    def show_info(self):
        return f"{self.surname} was born on {self.birthday} and teaches {self.fakultet} as {self.dolzhnost} for {self.staz} years"

    #def get_age(self):
    #    return relativedelta(datetime.now(),self.birthday).years


stu1 = Student('Goretskyi', '19/08/1991', 'test', 'testik')

abi1 = Abiturient('Komarovskiy', '20/08/1985', 'matematika',)

tea1 = Teacher('Komarov', '20/08/1960', 'fizika', 'professor', '3')


person_list = [stu1, abi1, tea1]

for person in person_list:
    print (person.show_info())

min_age = 20
max_age = 36



filtered_list = list(filter(lambda x : x.get_age() >= min_age and x.get_age() <= max_age, person_list))

print(filtered_list)