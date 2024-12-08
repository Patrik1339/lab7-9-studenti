class ValidatorDiscipline:

    def valideaza_disciplina(self, disciplina):
        erori = ''
        if disciplina.get_id_disciplina() < 0:
            erori += 'Id invalid!'
        if disciplina.get_nume() == '':
            erori += 'Nume invalid!'
        if disciplina.get_profesor() == '':
            erori += 'Profesor invalid!'
        if len(erori) != 0:
            return erori