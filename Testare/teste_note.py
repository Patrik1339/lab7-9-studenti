import unittest

from Domeniu.Discipline import Discipline
from Domeniu.Studenti import Studenti
from Domeniu.Note import Note
from Erori.RepositoryError import RepositoryError
from Infrastructura.Repository_discipline import RepositoryDiscipline
from Infrastructura.Repository_note import RepositoryNote
from Infrastructura.Repository_studenti import RepositoryStudenti
from Business.Service_note import ServiceNote


class TesteNote(unittest.TestCase):
    def setUp(self):
        self.__repository_studenti = RepositoryStudenti('D:/pycharm_projects/Exercitiu_simulare/Testare/teste_studenti.txt')
        self.__repository_discipline = RepositoryDiscipline('D:/pycharm_projects/Exercitiu_simulare/Testare/teste_discipline.txt')
        self.__repository_note = RepositoryNote('D:/pycharm_projects/Exercitiu_simulare/Testare/teste_note.txt',
                                                self.__repository_studenti,
                                                self.__repository_discipline)
        self.__service_note = ServiceNote(self.__repository_studenti, self.__repository_discipline, self.__repository_note)
        self.__student1 = Studenti(1, "Alex")
        self.__disciplina1 = Discipline(1, "Matematica", "Profesor1")
        self.__nota1 = Note(self.__student1, self.__disciplina1, 10)
        self.__repository_studenti.set_studenti({1: self.__student1})
        self.__repository_discipline.set_discipline({1: self.__disciplina1})
        self.__repository_note.set_note({})

    def tearDown(self):
        self.__repository_studenti.set_studenti({})
        self.__repository_discipline.set_discipline({})
        self.__repository_note.set_note({})
        with open("D:/pycharm_projects/Exercitiu_simulare/Testare/teste_note.txt", 'w') as f:
            f.truncate(0)

    def test_asignare_nota(self):
        """Test pentru asignarea unei note."""
        # Test pentru asignare eșuată (student sau disciplină inexistentă)
        self.__repository_studenti.set_studenti({})
        self.__repository_discipline.set_discipline({})
        with self.assertRaises(RepositoryError):
            self.__service_note.asigngare_nota(self.__student1.get_id_student(), self.__disciplina1.get_id_disciplina(), 10)

        # Test pentru asignare reușită
        self.__repository_studenti.set_studenti({1: self.__student1})
        self.__repository_discipline.set_discipline({1: self.__disciplina1})
        self.__service_note.asigngare_nota(self.__student1.get_id_student(), self.__disciplina1.get_id_disciplina(), 10)

        # Verificare că nota a fost adăugată corect
        nota_adaugata = self.__repository_note.get_note()[(self.__student1.get_id_student(), self.__disciplina1.get_id_disciplina())]
        self.assertEqual(nota_adaugata.get_student(), self.__student1)
        self.assertEqual(nota_adaugata.get_disciplina(), self.__disciplina1)
        self.assertEqual(nota_adaugata.get_valoare(), 10)

    def test_get_note(self):
        """Test pentru obținerea notelor."""
        self.__service_note.asigngare_nota(self.__student1.get_id_student(), self.__disciplina1.get_id_disciplina(), 10)
        note_asteptate = {(1, 1): self.__nota1}
        self.assertEqual(self.__repository_note.get_note(), note_asteptate)
