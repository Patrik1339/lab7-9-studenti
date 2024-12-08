class Note:
    def __init__(self, student, disciplina, valoare):
        self.__student = student
        self.__disciplina = disciplina
        self.__valoare = valoare

    def __eq__(self, other):
        return self.__student == other.__student and self.__disciplina == other.__disciplina and isinstance(self, Note) and isinstance(other, Note)

    def get_student(self):
        return self.__student

    def get_disciplina(self):
        return self.__disciplina

    def get_valoare(self):
        return self.__valoare