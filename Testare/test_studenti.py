import unittest

from Business.Service_studenti import ServiceStudenti
from Domeniu.Studenti import Studenti
from Erori.RepositoryError import RepositoryError
from Erori.ValidationError import ValidationError
from Infrastructura.Repository_studenti import RepositoryStudenti
from Validator.Validator_studenti import ValidatorStudenti


class TesteStudenti(unittest.TestCase):
    def setUp(self):
        self.__validator_studenti = ValidatorStudenti()
        self.__repository_studenti = RepositoryStudenti('D:/pycharm_projects/Exercitiu_simulare/Testare/teste_studenti.txt')
        self.__service_studenti = ServiceStudenti(self.__repository_studenti, self.__validator_studenti)
        self.__student1 = Studenti(1, "Alex")
        self.__student2 = Studenti(2, "Bob")
        self.__student1_modificat = Studenti(1, "Bob")
        self.__repository_studenti.set_studenti({})
        with open("D:/pycharm_projects/Exercitiu_simulare/Testare/teste_studenti.txt", 'w') as f:
            f.truncate(0)

    def adauga_student_helper(self, id_student, nume):
        """Metodă ajutătoare pentru a adăuga un student."""
        self.__service_studenti.adauga_student(id_student, nume)

    def test_student(self):
        # Test crearea studentului
        self.assertEqual(self.__student1.get_id_student(), 1)
        self.assertEqual(self.__student1.get_nume(), "Alex")

        # Test adăugare student
        with self.assertRaises(ValidationError):
            self.adauga_student_helper(-1, '')
        self.adauga_student_helper(1, "Alex")
        self.assertEqual(self.__repository_studenti.get_studenti(), {1: self.__student1})
        with self.assertRaises(RepositoryError):
            self.adauga_student_helper(1, "Alex")

        # Test căutare student
        with self.assertRaises(RepositoryError):
            self.__service_studenti.cauta_student(99)
        self.assertEqual(self.__service_studenti.cauta_student(1), self.__student1)

        # Test modificare student
        with self.assertRaises(RepositoryError):
            self.__service_studenti.modifica_student(99, "Bob")
        with self.assertRaises(ValidationError):
            self.__service_studenti.modifica_student(1, '')
        self.__service_studenti.modifica_student(1, "Bob")
        self.assertEqual(self.__repository_studenti.get_studenti()[1].get_nume(), "Bob")

        # Test ștergere student
        with self.assertRaises(RepositoryError):
            self.__service_studenti.sterge_student(99)
        self.__service_studenti.sterge_student(1)
        self.assertEqual(self.__repository_studenti.get_studenti(), {})

        # Test obținere studenți
        dictionar_asteptat = {2: self.__student2}
        self.__repository_studenti.set_studenti(dictionar_asteptat)
        self.assertEqual(self.__repository_studenti.get_studenti(), dictionar_asteptat)

    def tearDown(self):
        self.__repository_studenti.set_studenti({})
        with open("D:/pycharm_projects/Exercitiu_simulare/Testare/teste_studenti.txt", 'w') as f:
            f.truncate(0)