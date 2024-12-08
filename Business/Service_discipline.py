from Domeniu.Discipline import Discipline
from Erori.RepositoryError import RepositoryError
from Erori.ValidationError import ValidationError


class ServiceDiscipline:
    def __init__(self, repository_discipline, validator_discipline):
        self.__repository_discipline = repository_discipline
        self.__validator_discipline = validator_discipline

    def adauga_disciplina(self, id_disciplina, nume, profesor):
        if id_disciplina in self.__repository_discipline.get_discipline():
            raise RepositoryError('Disciplina existenta!')
        disciplina = Discipline(id_disciplina, nume, profesor)
        erori = self.__validator_discipline.valideaza_disciplina(disciplina)
        if erori is not None:
            raise ValidationError(erori)
        self.__repository_discipline.adauga_disciplina(disciplina)

    def sterge_disciplina(self, id_disciplina):
        if id_disciplina not in self.__repository_discipline.get_discipline():
            raise RepositoryError('Disciplina inexistenta!')
        self.__repository_discipline.sterge_disciplina(id_disciplina)
        return self.__repository_discipline.get_discipline()

    def modifica_discipline(self, id_disciplina, nume, profesor):
        if id_disciplina not in self.__repository_discipline.get_discipline():
            raise RepositoryError('Disciplina inexistenta!')
        disciplina = Discipline(id_disciplina, nume, profesor)
        erori = self.__validator_discipline.valideaza_disciplina(disciplina)
        if erori is not None:
            raise ValidationError(erori)
        self.__repository_discipline.modifica_disciplina(disciplina)