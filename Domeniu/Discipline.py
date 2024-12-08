class Discipline:
    def __init__(self, id_disciplina, nume, profesor):
        self.__id_disciplina = id_disciplina
        self.__nume = nume
        self.__profesor = profesor

    def __eq__(self, other):
        return self.__id_disciplina == other.__id_disciplina and self.__nume == other.__nume and self.__profesor == other.__profesor

    def get_id_disciplina(self):
        return self.__id_disciplina

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return self.__profesor