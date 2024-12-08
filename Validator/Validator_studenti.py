from Erori.RepositoryError import RepositoryError


class ValidatorStudenti:
    def __init__(self):
        pass

    def valideaza_student(self, student):
        erori = ''
        if student.get_id_student() < 0:
            erori += 'Id invalid!\n'
        if student.get_nume() == '':
            erori += 'Nume invalid!\n'
        erori = erori.strip('\n')
        if len(erori) != 0:
            return erori