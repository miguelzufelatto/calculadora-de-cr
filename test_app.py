from app import Aluno, Disciplina


def test_calcular_cr_simples():
    aluno_teste = Aluno("999", "T1")
    disciplina_A = Disciplina("D-A", 60)
    disciplina_B = Disciplina("D-B", 40)

    aluno_teste.notas.append((disciplina_A, 100))
    aluno_teste.notas.append((disciplina_B, 50))

    cr_calculado = aluno_teste.calcular_cr()

    cr_esperado = 80.0
    assert cr_calculado == cr_esperado


def test_calcular_cr_aluno_sem_notas():
    aluno_sem_notas = Aluno("000", "T2")
    cr_calculado = aluno_sem_notas.calcular_cr()
    assert cr_calculado == 0


def test_calcular_cr_com_nota_zero():
    aluno_teste = Aluno("111", "T3")
    disciplina_A = Disciplina("D-A", 60)
    disciplina_B = Disciplina("D-B", 40)

    aluno_teste.notas.append((disciplina_A, 80))
    aluno_teste.notas.append((disciplina_B, 0))

    cr_calculado = aluno_teste.calcular_cr()

    cr_esperado = 48.0
    assert cr_calculado == cr_esperado
