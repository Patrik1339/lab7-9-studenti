from Domeniu.Discipline import Discipline


class RepositoryDiscipline:
    def __init__(self, fisier):
        self.__fisier = fisier
        self.__discipline = {}
        self.citeste_fisier()

    def citeste_fisier(self):
        with open(self.__fisier, 'r') as f:
            for linie in f:
                linie = linie.strip()
                id_disciplina, nume, profesor = linie.split(',')
                id_disciplina = int(id_disciplina)
                disciplina = Discipline(id_disciplina, nume, profesor)
                self.__discipline[id_disciplina] = disciplina
        return self.__discipline

    def scrie_fisier(self):
        with open(self.__fisier, 'w') as f:
            for id_disciplina in self.__discipline:
                disciplina = self.__discipline[id_disciplina]
                f.write(f"{disciplina.get_id_disciplina()},{disciplina.get_nume()},{disciplina.get_profesor()}\n")
        return self.__discipline

    def adauga_disciplina(self, disciplina):
        self.__discipline[disciplina.get_id_disciplina()] = disciplina
        self.scrie_fisier()
        return self.__discipline

    def sterge_disciplina(self, id_disciplina):
        del self.__discipline[id_disciplina]
        self.scrie_fisier()
        return self.__discipline

    def modifica_disciplina(self, disciplina_modificata):
        self.__discipline[disciplina_modificata.get_id_disciplina()] = disciplina_modificata
        self.scrie_fisier()
        return self.__discipline

    def get_discipline(self):
        return self.__discipline

    def cauta_disciplina(self, id_disciplina):
        return self.__discipline[id_disciplina]

    def set_discipline(self, dictionar):
        self.__discipline = dictionar