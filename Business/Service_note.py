from Erori.RepositoryError import RepositoryError


class ServiceNote:
    def __init__(self, repository_studenti, repository_discipline, repository_note):
        self.__repository_studenti = repository_studenti
        self.__repository_discipline = repository_discipline
        self.__repository_note = repository_note

    def asignare_nota(self, id_student, id_disciplina, valoare):
        if not id_student in self.__repository_studenti.get_studenti() or not id_disciplina in self.__repository_discipline.get_discipline():
            raise RepositoryError("Student sau disciplina inexistenta!")
        student = self.__repository_studenti.cauta_student(id_student)
        disciplina = self.__repository_discipline.cauta_disciplina(id_disciplina)
        self.__repository_note.asignare_nota(student, disciplina, valoare)