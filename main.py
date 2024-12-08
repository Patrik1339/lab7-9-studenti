from Business.Service_discipline import ServiceDiscipline
from Business.Service_note import ServiceNote
from Business.Service_studenti import ServiceStudenti
from Infrastructura.Repository_discipline import RepositoryDiscipline
from Infrastructura.Repository_note import RepositoryNote
from Infrastructura.Repository_studenti import RepositoryStudenti
from Ui.Ui import Consola
from Validator.Validator_discipline import ValidatorDiscipline
from Validator.Validator_studenti import ValidatorStudenti


repository_studenti = RepositoryStudenti('Infrastructura/studenti.txt')
validator_studenti = ValidatorStudenti()
service_studenti = ServiceStudenti(repository_studenti, validator_studenti)
repository_discipline = RepositoryDiscipline('Infrastructura/discipline.txt')
validator_discipline = ValidatorDiscipline()
service_discipline = ServiceDiscipline(repository_discipline, validator_discipline)
repository_note = RepositoryNote('Infrastructura/note.txt', repository_studenti, repository_discipline)
service_note = ServiceNote(repository_studenti, repository_discipline, repository_note)
consola = Consola(service_studenti, repository_studenti, service_discipline, repository_discipline, service_note, repository_note)


def main():
    consola.run()

main()