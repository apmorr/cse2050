class Person():
    def __init__(self, name, netid):
        self._netid = netid
        self._name = name

    @property
    def name(self):
        return self._name

class Student(Person):
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_netid(self):
        return self._netid

    def add_course(self, course):
        pass

class Faculty(Person):
    pass