from Domeniu.Discipline import Discipline
from Erori.RepositoryError import RepositoryError
from Erori.ValidationError import ValidationError


class Consola:
    def __init__(self, service_studenti, repository_studenti, service_discipline, repository_discipline, service_note, repository_note):
        self.__service_studenti = service_studenti
        self.__repository_studenti = repository_studenti
        self.__service_discipline = service_discipline
        self.__repository_discipline = repository_discipline
        self.__service_note = service_note
        self.__repository_note = repository_note
        self.__comenzi = {
            1: self.ui_adauga_student,
            2: self.ui_sterge_student,
            3: self.ui_modifica_student,
            4: self.ui_cauta_student,
            5: self.ui_afisare_studenti,
            6: self.ui_adauga_disciplina,
            7: self.ui_sterge_disciplina,
            8: self.ui_modifica_disciplina,
            9: self.ui_cauta_disciplina,
            10: self.ui_afisare_discipline,
            11: self.ui_asignare_nota,
            12: self.ui_afisare_note,
        }

    def ui_adauga_student(self):
        id_student = input("Id student: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("Id invalid!")
            return
        nume = input("Nume: ")
        try:
            self.__service_studenti.adauga_student(id_student, nume)
            print("Student adăugat cu succes!")
        except RepositoryError as re:
            print(re)
        except ValidationError as ve:
            print(ve)

    def ui_sterge_student(self):
        id_student = input("Id student: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("Id invalid!")
            return
        try:
            self.__service_studenti.sterge_student(id_student)
        except RepositoryError as re:
            print(re)

    def ui_modifica_student(self):
        id_student = input("Id student: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("Id invalid!")
            return
        nume = input("Nume: ")
        try:
            self.__service_studenti.modifica_student(id_student, nume)
        except RepositoryError as re:
            print(re)
        except ValidationError as ve:
            print(ve)

    def ui_cauta_student(self):
        id_student = input("Id student: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("Id invalid!")
            return
        try:
            student = self.__service_studenti.cauta_student(id_student)
            print(f"Id student:{id_student}, Nume:{student.get_nume()}")
        except RepositoryError as re:
            print(re)

    def ui_afisare_studenti(self):
        studenti = self.__repository_studenti.get_studenti()
        if len(studenti) == 0:
            print('Nu exista studenti!')
            return
        for id_student in studenti:
            student = self.__repository_studenti.cauta_student(id_student)
            print(f"Id student:{student.get_id_student()}, Nume:{student.get_nume()}")

    def ui_adauga_disciplina(self):
        id_disciplina = input("Id disciplina:")
        try:
            id_disciplina = int(id_disciplina)
        except ValueError:
            print("Id invalid!")
            return
        nume = input("Nume:")
        profesor = input("Profesor:")
        try:
            self.__service_discipline.adauga_disciplina(id_disciplina, nume, profesor)
            print("Disciplina adaugata cu succes!")
        except RepositoryError as re:
            print(re)
        except ValidationError as ve:
            print(ve)

    def ui_sterge_disciplina(self):
        id_disciplina = input("Id disciplina:")
        try:
            id_disciplina = int(id_disciplina)
        except ValueError:
            print("Id invalid!")
            return
        try:
            self.__service_discipline.sterge_disciplina(id_disciplina)
            print("Disciplina stearsa cu succes!")
        except RepositoryError as re:
            print(re)

    def ui_modifica_disciplina(self):
        id_disciplina = input("Id disciplina:")
        try:
            id_disciplina = int(id_disciplina)
        except ValueError:
            print("Id invalid!")
            return
        nume = input("Nume:")
        profesor = input("Profesor:")
        try:
            self.__service_discipline.modifica_discipline(id_disciplina, nume, profesor)
            print("Disciplina modificata cu succes!")
        except RepositoryError as re:
            print(re)
        except ValidationError as ve:
            print(ve)

    def ui_cauta_disciplina(self):
        id_disciplina = input("Id disciplina:")
        try:
            id_disciplina = int(id_disciplina)
        except ValueError:
            print("Id invalid!")
            return
        try:
            disciplina = self.__repository_discipline.cauta_disciplina(id_disciplina)
            print(f"Id student:{id_disciplina}, Nume:{disciplina.get_nume()}")
        except RepositoryError as re:
            print(re)

    def ui_afisare_discipline(self):
        discipline = self.__repository_discipline.get_discipline()
        if len(discipline) == 0:
            print("Nu exista discipline!")
            return
        for id_disciplina in discipline:
            disciplina = discipline[id_disciplina]
            print(f"Id disciplina:{disciplina.get_id_disciplina()}, Nume:{disciplina.get_nume()}, Profesor:{disciplina.get_profesor()}\n")

    def ui_asignare_nota(self):
        id_student = input("Id student:")
        try:
            id_student = int(id_student)
        except ValueError:
            print("Id invalid!")
            return
        id_disciplina = input("Id disciplina:")
        try:
            id_disciplina = int(id_disciplina)
        except ValueError:
            print("Id invalid!")
            return
        nota = input("Nota:")
        try:
            self.__service_note.asignare_nota(id_student, id_disciplina, nota)
        except RepositoryError as re:
            print(re)
            return
        print("Nota asignata cu succes!")

    def ui_afisare_note(self):
        note = self.__repository_note.get_note()
        for (id_student, id_disciplina) in note:
            student = self.__repository_studenti.cauta_student(id_student)
            disciplina = self.__repository_discipline.cauta_disciplina(id_disciplina)
            print(f"Nume student:{student.get_nume()}, Disciplina:{disciplina.get_nume()}, Nota:{note[(id_student, id_disciplina)].get_valoare()}\n")

    def run(self):
        while True:
            print('Lista comenzi:\n-------------')
            print('1: Adauga student\n2: Sterge student\n3: Modifica student\n4: Cauta student\n5: Afisare studenti\n6: Adauga disciplina\n7: Sterge disciplina\n8: Modifica disciplina\n9: Cauta disciplina\n10: Afisare discipline\n11: Asignare nota\n12: Afisare note\n-------------')
            comanda = input('Alege o comanda:')
            try:
                comanda = int(comanda)
            except ValueError:
                print('Comanda invalida!')
            if comanda in self.__comenzi:
                self.__comenzi[comanda]()
            elif comanda == 'exit':
                break