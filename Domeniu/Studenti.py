class Studenti:
    def __init__(self, id_student, nume):
        self.__id_student = id_student
        self.__nume = nume

    def __eq__(self, other):
        return isinstance(self, Studenti) and isinstance(other, Studenti) and self.__nume == other.__nume and self.__id_student == other.__id_student

    def get_id_student(self):
        return self.__id_student

    def get_nume(self):
        return self.__nume