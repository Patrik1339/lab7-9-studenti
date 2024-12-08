from Domeniu.Studenti import Studenti
from Erori.RepositoryError import RepositoryError
from Erori.ValidationError import ValidationError


class ServiceStudenti:
    def __init__(self, repository_studenti, validator_studenti):
        self.__repository_studenti = repository_studenti
        self.__validator_studenti = validator_studenti

    def adauga_student(self, id_student, nume):
        if id_student in self.__repository_studenti.get_studenti():
            raise RepositoryError('Student existent!')
        student = Studenti(id_student, nume)
        erori = self.__validator_studenti.valideaza_student(student)
        if erori is not None:
            raise ValidationError(erori)
        self.__repository_studenti.adauga_student(student)

    def sterge_student(self, id_student):
        if id_student not in self.__repository_studenti.get_studenti():
            raise RepositoryError('Student inexistent!')
        self.__repository_studenti.sterge_student(id_student)

    def modifica_student(self, id_student, nume):
        if id_student not in self.__repository_studenti.get_studenti():
            raise RepositoryError('Student inexistent!')
        student_modificat = Studenti(id_student, nume)
        erori = self.__validator_studenti.valideaza_student(student_modificat)
        if erori is not None:
            raise ValidationError(erori)
        self.__repository_studenti.modifica_student(student_modificat)

    def cauta_student(self, id_student):
        if id_student not in self.__repository_studenti.get_studenti():
            raise RepositoryError('Student inexistent!')
        student = self.__repository_studenti.cauta_student(id_student)
        return student