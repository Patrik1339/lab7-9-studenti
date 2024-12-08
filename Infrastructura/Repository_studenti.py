from Domeniu.Studenti import Studenti


class RepositoryStudenti:
    def __init__(self, fisier):
        self.__fisier = fisier
        self.__studenti = {}
        self.citeste_fisier()

    def citeste_fisier(self):
        with open(self.__fisier, 'r') as f:
            for linie in f:
                linie = linie.strip()
                id_student, nume = linie.split(',')
                id_student = int(id_student)
                student = Studenti(id_student, nume)
                self.__studenti[id_student] = student
        return self.__studenti

    def scrie_fisier(self):
        with open(self.__fisier, 'w') as f:
            for id_student in self.__studenti:
                student = self.__studenti[id_student]
                f.write(f"{id_student},{student.get_nume()}\n")
        return self.__studenti

    def adauga_student(self, student):
        self.__studenti[student.get_id_student()] = student
        self.scrie_fisier()
        return self.__studenti

    def sterge_student(self, id_student):
        del self.__studenti[id_student]
        self.scrie_fisier()
        return self.__studenti

    def modifica_student(self, student_modificat):
        self.__studenti[student_modificat.get_id_student()] = student_modificat
        self.scrie_fisier()
        return self.__studenti

    def get_studenti(self):
        return self.__studenti

    def cauta_student(self, id_student):
        return self.__studenti[id_student]

    def set_studenti(self, dictionar):
        self.__studenti = dictionar