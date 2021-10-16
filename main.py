import sqlite3

con = sqlite3.connect('Aluno.db')
cur = con.cursor()

print("1. Buscar os nomes de todos os alunos que frequentam alguma turma do professor 'JOAO PEDRO':")
for data in cur.execute("select ALUNO.nome from ALUNO join ALUNO_TURMA on ALUNO.id = ALUNO_TURMA.aluno_id join TURMA on TURMA.id = ALUNO_TURMA.turma_id join PROFESSOR on PROFESSOR.id = TURMA.PROFESSOR_id where PROFESSOR.nome = 'JOAO PEDRO'"):
    print("\t"+str(data[0]))

print("2. Buscar os dias da semana que tenham aulas da disciplina 'MATEMATICA':")
for data in cur.execute("select TURMA.dia_da_semana from TURMA inner join DISCIPLINA on TURMA.DISCIPLINA_id = DISCIPLINA.id where DISCIPLINA.nome = 'MATEMATICA'"):
    print("\t"+str(data[0]))

print("3. Buscar todos os alunos que frequentem aulas de 'MATEMATICA' e também 'FISICA':")
for data in cur.execute("select ALUNO.nome from ALUNO join ALUNO_TURMA on ALUNO.id = ALUNO_TURMA.aluno_id join TURMA on TURMA.id = ALUNO_TURMA.turma_id join DISCIPLINA on DISCIPLINA.id = TURMA.DISCIPLINA_id where DISCIPLINA.nome = 'MATEMATICA' and ALUNO.nome in (select ALUNO.nome from ALUNO join ALUNO_TURMA on ALUNO.id = ALUNO_TURMA.aluno_id join TURMA on TURMA.id = ALUNO_TURMA.turma_id join DISCIPLINA on DISCIPLINA.id = TURMA.DISCIPLINA_id where DISCIPLINA.nome = 'FISICA')"):
    print("\t"+str(data[0]))

print("4. Buscar as disciplinas que não tenham nenhuma turma:")
for data in cur.execute("select nome from DISCIPLINA where id NOT IN (SELECT DISCIPLINA_id from TURMA)"):
    print("\t"+str(data[0]))

print("5. Buscar os alunos que frequentem aulas de 'MATEMATICA' exceto os que frequentem 'QUIMICA':")
for data in cur.execute("select ALUNO.nome from ALUNO join ALUNO_TURMA on ALUNO.id = ALUNO_TURMA.aluno_id join TURMA on TURMA.id = ALUNO_TURMA.turma_id join DISCIPLINA on DISCIPLINA.id = TURMA.DISCIPLINA_id where DISCIPLINA.nome = 'MATEMATICA' and ALUNO.nome not in (select ALUNO.nome from ALUNO join ALUNO_TURMA on ALUNO.id = ALUNO_TURMA.aluno_id join TURMA on TURMA.id = ALUNO_TURMA.turma_id join DISCIPLINA on DISCIPLINA.id = TURMA.DISCIPLINA_id where DISCIPLINA.nome = 'QUIMICA')"):
    print("\t"+str(data[0]))
