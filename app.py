import csv


class Aluno:
    def __init__(self, matricula, cod_curso):
        self.id = matricula
        self.cod_curso = cod_curso
        self.notas = []

    def calcular_cr(self):
        soma_ponderada = 0
        total_carga_horaria = 0

        for disciplina, nota in self.notas:
            soma_ponderada += nota * disciplina.carga_horaria
            total_carga_horaria += disciplina.carga_horaria

        if total_carga_horaria == 0:
            return 0

        return soma_ponderada / total_carga_horaria


class Disciplina:
    def __init__(self, codigo, carga_horaria):
        self.codigo = codigo
        self.carga_horaria = carga_horaria


def processar_dados(nome_arquivo='notas.csv'):
    alunos = {}
    disciplinas = {}

    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as notas_csv:
            leitor_csv = csv.DictReader(notas_csv)
            for linha in leitor_csv:
                matricula = linha['MATRICULA']
                cod_curso = linha['COD_CURSO']
                cod_disciplina = linha['COD_DISCIPLINA']
                nota = int(linha['NOTA'])
                carga_horaria = int(linha['CARGA_HORARIA'])

                if matricula not in alunos:
                    alunos[matricula] = Aluno(matricula, cod_curso)

                if cod_disciplina not in disciplinas:
                    disciplinas[cod_disciplina] = Disciplina(
                        cod_disciplina, carga_horaria)

                aluno_atual = alunos[matricula]
                disciplina_atual = disciplinas[cod_disciplina]
                aluno_atual.notas.append((disciplina_atual, nota))
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{nome_arquivo}' não foi encontrado.")
        return {}

    return alunos


def main():
    alunos = processar_dados()
    if not alunos:
        return

    print("--- CR dos Alunos ---")
    for aluno in alunos.values():
        cr_do_aluno = aluno.calcular_cr()
        print(f"{aluno.id} - {cr_do_aluno:.2f}")

    print("\n--- Média de CR dos Cursos ---")
    cr_por_curso = {}
    for aluno in alunos.values():
        cr_aluno = aluno.calcular_cr()
        curso_id = aluno.cod_curso
        if curso_id not in cr_por_curso:
            cr_por_curso[curso_id] = [cr_aluno, 1]
        else:
            cr_por_curso[curso_id][0] += cr_aluno
            cr_por_curso[curso_id][1] += 1

    for curso_id, dados in cr_por_curso.items():
        soma_cr, contagem_alunos = dados
        media_cr = soma_cr / contagem_alunos
        print(f"{curso_id} - {media_cr:.2f}")


if __name__ == "__main__":
    main()
