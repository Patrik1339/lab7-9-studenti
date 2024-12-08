import unittest

from Business.Service_discipline import ServiceDiscipline
from Domeniu.Discipline import Discipline
from Erori.RepositoryError import RepositoryError
from Erori.ValidationError import ValidationError
from Infrastructura.Repository_discipline import RepositoryDiscipline
from Validator.Validator_discipline import ValidatorDiscipline


class TestDiscipline(unittest.TestCase):
    def setUp(self):
        self.__validator_discipline = ValidatorDiscipline()
        self.__repository_discipline = RepositoryDiscipline('D:/pycharm_projects/Exercitiu_simulare/Testare/teste_discipline.txt')
        self.__service_discipline = ServiceDiscipline(self.__repository_discipline, self.__validator_discipline)
        self.__disciplina1 = Discipline(1, "Matematica", "Profesor1")
        self.__disciplina2 = Discipline(2, "Romana", "Profesor2")
        self.__disciplina1_modificata = Discipline(1, "Romana", "Profesor2")
        self.__repository_discipline.set_discipline({})
        with open("D:/pycharm_projects/Exercitiu_simulare/Testare/teste_discipline.txt", 'w') as f:
            f.truncate(0)

    def adauga_disciplina_helper(self, id_disciplina, nume, profesor):
        self.__service_discipline.adauga_disciplina(id_disciplina, nume, profesor)

    def test_disciplina(self):
        # Test crearea disciplinei
        self.assertEqual(self.__disciplina1.get_id_disciplina(), 1)
        self.assertEqual(self.__disciplina1.get_nume(), "Matematica")
        self.assertEqual(self.__disciplina1.get_profesor(), "Profesor1")

        # Test adăugare disciplină
        with self.assertRaises(ValidationError):
            self.adauga_disciplina_helper(-1, '', '')
        self.adauga_disciplina_helper(1, "Matematica", "Profesor1")
        with self.assertRaises(RepositoryError):
            self.adauga_disciplina_helper(1, "Matematica", "Profesor1")

        # Test ștergere disciplină
        with self.assertRaises(RepositoryError):
            self.__service_discipline.sterge_disciplina(99)
        self.__service_discipline.sterge_disciplina(1)
        self.assertEqual(self.__repository_discipline.get_discipline(), {})

        # Test modificare disciplină
        self.adauga_disciplina_helper(1, "Matematica", "Profesor1")
        self.__service_discipline.modifica_discipline(1, "Romana", "Profesor2")
        disciplina_modificata = self.__repository_discipline.get_discipline()[1]
        self.assertEqual(disciplina_modificata.get_nume(), "Romana")
        self.assertEqual(disciplina_modificata.get_profesor(), "Profesor2")

        # Test get discipline
        dictionar_asteptat = {1: self.__disciplina1, 2: self.__disciplina2}
        self.__repository_discipline.set_discipline(dictionar_asteptat)
        self.assertEqual(self.__repository_discipline.get_discipline(), dictionar_asteptat)
