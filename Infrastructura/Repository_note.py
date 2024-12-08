from Domeniu.Note import Note


class RepositoryNote:
    def __init__(self, fisier, repository_studenti, repository_discipline):
        self.__repository_studenti = repository_studenti
        self.__repository_discipline = repository_discipline
        self.__note = {}
        self.__fisier = fisier
        self.citeste_fisier()

    def citeste_fisier(self):
        with open(self.__fisier, "r") as f:
            for linie in f:
                linie = linie.strip()
                id_student, id_disciplina, valoare = linie.split(',')
                id_student = int(id_student)
                id_disciplina = int(id_disciplina)
                valoare = float(valoare)
                student = self.__repository_studenti.cauta_student(id_student)
                disciplina = self.__repository_discipline.cauta_disciplina(id_disciplina)
                nota = Note(student, disciplina, valoare)
                if (id_student, id_disciplina) not in self.__note:
                    self.__note[(id_student, id_disciplina)] = []
                self.__note[(id_student, id_disciplina)].append(nota)

    def scrie_fisier(self):
        with open(self.__fisier, "w") as f:
            for (id_student, id_disciplina) in self.__note:
                for nota in self.__note[(id_student, id_disciplina)]:
                    f.write(f"{id_student},{id_disciplina},{nota.get_valoare()}\n")

    def asignare_nota(self, student, disciplina, valoare):
        nota = Note(student, disciplina, valoare)
        self.__note[(student.get_id_student(), disciplina.get_id_disciplina())] = nota
        self.scrie_fisier()

    def set_note(self, dictionar):
        self.__note = dictionar
        self.scrie_fisier()

    def get_note(self):
        return self.__note