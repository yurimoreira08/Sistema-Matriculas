import sys
from dao.pessoa_dao import PessoaDAO
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.funcionario_dao import FuncionarioDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO
from dao.matricula_dao import MatriculaDAO

# VISUAL
def titulo(txt):
    print("\n" + "=" * 60)
    print(txt.center(60))
    print("=" * 60)

def subtitulo(txt):
    print("\n" + "-" * 60)
    print(txt.center(60))
    print("-" * 60)

def linha():
    print("-" * 60)

def pausa():
    input("\nPressione ENTER para continuar...")

def print_formatado(campos, valores):
    linha()
    for campo, valor in zip(campos, valores):
        print(f"{campo.ljust(20)}: {valor}")
    linha()

# VALIDAÇÕES
def safe_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número inteiro válido.")


def safe_float(msg):
    while True:
        try:
            val = float(input(msg))
            if 0 <= val <= 10:
                return val
            print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")


def lista_vazia(lista, nome):
    if not lista:
        print(f"\nNenhum {nome} cadastrado.")
        pausa()
        return True
    return False

def main():
    p = PessoaDAO()
    a = AlunoDAO()
    pr = ProfessorDAO()
    f = FuncionarioDAO()
    c = CursoDAO()
    t = TurmaDAO()
    m = MatriculaDAO()

    while True:
        titulo("SISTEMA DE MATRÍCULAS E NOTAS")

        print("1 - Cadastrar")
        print("2 - Matricular Aluno")
        print("3 - Editar")
        print("4 - Listar")
        print("5 - Excluir")
        print("6 - Lançar Notas")
        print("7 - Emitir Boletim")
        print("8 - Sair")

        op = input("\nEscolha: ")

        # CADASTRAR
        if op == "1":
            subtitulo("CADASTRAR")

            print("1 - Pessoa")
            print("2 - Funcionário")
            print("3 - Professor")
            print("4 - Aluno")
            print("5 - Curso")
            print("6 - Turma")

            sub = input("\nEscolha: ")

            if sub == "1":
                p.create(
                    input("Nome: "),
                    input("CPF: "),
                    input("Email: "),
                    input("Data Nascimento (YYYY-MM-DD): "),
                )

            elif sub == "2":
                dados = p.read()
                if lista_vazia(dados, "Pessoas"):
                    continue

                for x in dados:
                    print_formatado(["ID", "Nome"], [x[0], x[1]])

                f.create(
                    input("Cargo: "),
                    input("Email Institucional: "),
                    safe_int("ID Pessoa: "),
                )

            elif sub == "3":
                dados = p.read()
                if lista_vazia(dados, "Pessoas"):
                    continue

                for x in dados:
                    print_formatado(["ID", "Nome"], [x[0], x[1]])

                pr.create(
                    input("Área Especialização: "),
                    input("Email Institucional: "),
                    safe_int("ID Pessoa: "),
                )

            elif sub == "4":
                dados = p.read()
                if lista_vazia(dados, "Pessoas"):
                    continue

                for x in dados:
                    print_formatado(["ID", "Nome"], [x[0], x[1]])

                a.create(
                    input("Email Institucional: "),
                    safe_int("ID Pessoa: "),
                )

            elif sub == "5":
                c.create(
                    input("Nome do Curso: "),
                    safe_int("Carga Horária: "),
                )

            elif sub == "6":
                dados = c.read()
                if lista_vazia(dados, "Cursos"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Curso", "Carga Horária", "Qtd Alunos"],
                        [x[0], x[1], x[2], x[3]],
                    )

                t.create(
                    input("Período: "),
                    safe_int("Ano: "),
                    input("Horário: "),
                    safe_int("ID Curso: "),
                )

            else:
                print("Opção inválida.")

            pausa()

        # MATRICULAR
        elif op == "2":
            subtitulo("MATRICULAR ALUNO")

            alunos = a.read()
            turmas = t.read()

            if lista_vazia(alunos, "Alunos") or lista_vazia(turmas, "Turmas"):
                continue

            print("\nALUNOS DISPONÍVEIS")
            for x in alunos:
                print_formatado(
                    ["ID", "Nome", "Email Institucional"],
                    [x[0], x[1], x[2]],
                )

            id_aluno = safe_int("ID do Aluno: ")

            if not any(x[0] == id_aluno for x in alunos):
                print("\nAluno não existe.")
                pausa()
                continue

            print("\nTURMAS DISPONÍVEIS")
            for x in turmas:
                print_formatado(
                    ["ID Turma", "Curso", "Período", "Ano", "Horário"],
                    [x[0], x[2], x[4], x[5], x[6]],
                )

            id_turma = safe_int("ID da Turma: ")

            if not any(x[0] == id_turma for x in turmas):
                print("\nTurma não existe.")
                pausa()
                continue

            m.create(id_aluno, id_turma)
            pausa()

        # EDITAR
        elif op == "3":
            subtitulo("EDITAR")

            print("1 - Pessoa")
            print("2 - Funcionário")
            print("3 - Professor")
            print("4 - Aluno")
            print("5 - Curso")
            print("6 - Turma")

            sub = input("\nEscolha: ")

            if sub == "1":
                dados = p.read()
                if lista_vazia(dados, "Pessoas"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "CPF", "Email", "Nascimento"],
                        [x[0], x[1], x[2], x[3], x[4]],
                    )

                id_val = safe_int("ID: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nPessoa não existe.")
                    pausa()
                    continue

                p.update(
                    id_val,
                    input("Novo Nome: "),
                    input("Novo CPF: "),
                    input("Novo Email: "),
                    input("Nova Data (YYYY-MM-DD): "),
                )

            elif sub == "2":
                dados = f.read()
                if lista_vazia(dados, "Funcionários"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "Cargo", "Email Institucional"],
                        [x[0], x[1], x[2], x[3]],
                    )

                id_val = safe_int("ID Funcionário: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nFuncionário não existe.")
                    pausa()
                    continue

                f.update(
                    id_val,
                    input("Novo Cargo: "),
                    input("Novo Email Institucional: "),
                )

            elif sub == "3":
                dados = pr.read()
                if lista_vazia(dados, "Professores"):
                    continue

                for x in dados:
                    print_formatado(["ID", "Nome", "Área"], [x[0], x[1], x[2]])

                id_val = safe_int("ID Professor: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nProfessor não existe.")
                    pausa()
                    continue

                nova_area = input("Nova Área: ")
                novo_email = input("Novo Email Institucional: ")

                pr.update(id_val, nova_area, novo_email)


            elif sub == "4":
                dados = a.read()
                if lista_vazia(dados, "Alunos"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "Email Institucional"],
                        [x[0], x[1], x[2]],
                    )

                id_val = safe_int("ID Aluno: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nAluno não existe.")
                    pausa()
                    continue

                a.update(id_val, input("Novo Email Institucional: "))

            elif sub == "5":
                dados = c.read()
                if lista_vazia(dados, "Cursos"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Curso", "Carga Horária", "Qtd Alunos"],
                        [x[0], x[1], x[2], x[3]],
                    )

                id_val = safe_int("ID Curso: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nCurso não existe.")
                    pausa()
                    continue

                c.update(
                    id_val,
                    input("Novo Nome: "),
                    safe_int("Nova Carga Horária: "),
                )

            elif sub == "6":
                dados = t.read()
                if lista_vazia(dados, "Turmas"): continue

                for x in dados:
                    print_formatado(
                        ["ID", "Curso", "Carga Horária", "Período", "Ano", "Horário"],
                        [x[0], x[2], x[3], x[4], x[5], x[6]]
                    )

                id_val = safe_int("ID Turma: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nTurma não existe.")
                    pausa()
                    continue

                novo_periodo = input("Novo Período: ")
                novo_ano = safe_int("Novo Ano: ")
                novo_horario = input("Novo Horário: ")

                t.update(
                    id_val,
                    novo_periodo,
                    novo_ano,
                    novo_horario
                )

            pausa()

        # LISTAR
        elif op == "4":
            subtitulo("LISTAR")

            print("1 - Pessoa")
            print("2 - Funcionário")
            print("3 - Professor")
            print("4 - Aluno")
            print("5 - Curso")
            print("6 - Turma")

            sub = input("\nEscolha: ")

            if sub == "1":
                dados = p.read()
                if lista_vazia(dados, "Pessoas"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "CPF", "Email", "Nascimento"],
                        [x[0], x[1], x[2], x[3], x[4]],
                    )

            elif sub == "2":
                dados = f.read()
                if lista_vazia(dados, "Funcionários"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "Cargo", "Email Institucional"],
                        [x[0], x[1], x[2], x[3]],
                    )

            elif sub == "3":
                dados = pr.read()
                if lista_vazia(dados, "Professores"):
                    continue

                for x in dados:
                    print_formatado(["ID", "Nome", "Área"], [x[0], x[1], x[2]])

            elif sub == "4":
                dados = a.read()
                if lista_vazia(dados, "Alunos"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "Email Institucional"],
                        [x[0], x[1], x[2]],
                    )

            elif sub == "5":
                dados = c.read()
                if lista_vazia(dados, "Cursos"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Curso", "Carga Horária", "Qtd Alunos"],
                        [x[0], x[1], x[2], x[3]],
                    )

            elif sub == "6":
                dados = t.read()
                if lista_vazia(dados, "Turmas"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Curso", "Período", "Ano", "Horário"],
                        [x[0], x[2], x[4], x[5], x[6]]
                    )

            pausa()

        # EXCLUIR
        elif op == "5":
            subtitulo("EXCLUIR")

            print("1 - Pessoa")
            print("2 - Funcionário")
            print("3 - Professor")
            print("4 - Aluno")
            print("5 - Curso")
            print("6 - Turma")

            sub = input("\nEscolha: ")

            if sub == "1":
                dados = p.read()
                if lista_vazia(dados, "Pessoas"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "CPF", "Email", "Nascimento"],
                        [x[0], x[1], x[2], x[3], x[4]]
                    )

                id_val = safe_int("ID Pessoa: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nPessoa não existe.")
                    pausa()
                    continue

                if input("Confirmar exclusão? (s/n): ").lower() == "s":
                    p.delete(id_val)

            elif sub == "2":
                dados = f.read()
                if lista_vazia(dados, "Funcionários"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "Cargo", "Email Institucional"],
                        [x[0], x[1], x[2], x[3]]
                    )

                id_val = safe_int("ID Funcionário: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nFuncionário não existe.")
                    pausa()
                    continue

                if input("Confirmar exclusão? (s/n): ").lower() == "s":
                    f.delete(id_val)

            elif sub == "3":
                dados = pr.read()
                if lista_vazia(dados, "Professores"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "Área"],
                        [x[0], x[1], x[2]]
                    )

                id_val = safe_int("ID Professor: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nProfessor não existe.")
                    pausa()
                    continue

                if input("Confirmar exclusão? (s/n): ").lower() == "s":
                    pr.delete(id_val)

            elif sub == "4":
                dados = a.read()
                if lista_vazia(dados, "Alunos"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID", "Nome", "Email Institucional"],
                        [x[0], x[1], x[2]]
                    )

                id_val = safe_int("ID Aluno: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nAluno não existe.")
                    pausa()
                    continue

                if input("Confirmar exclusão? (s/n): ").lower() == "s":
                    a.delete(id_val)

            elif sub == "5":
                dados = c.read()
                if lista_vazia(dados, "Cursos"):
                    continue

                for x in dados:
                     print_formatado(
                        ["ID", "Curso", "Carga Horária", "Qtd Alunos"],
                        [x[0], x[1], x[2], x[3]]
                    )

                id_val = safe_int("ID Curso: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nCurso não existe.")
                    pausa()
                    continue

                if input("Confirmar exclusão? (s/n): ").lower() == "s":
                    c.delete(id_val)

            elif sub == "6":
                dados = t.read()
                if lista_vazia(dados, "Turmas"):
                    continue

                for x in dados:
                    print_formatado(
                        ["ID Turma", "Curso", "Carga Horária", "Período", "Ano", "Horário"],
                        [x[0], x[2], x[3], x[4], x[5], x[6]]
                    )

                id_val = safe_int("ID Turma: ")

                if not any(x[0] == id_val for x in dados):
                    print("\nTurma não existe.")
                    pausa()
                    continue

                if input("Confirmar exclusão? (s/n): ").lower() == "s":
                    t.delete(id_val)

            else:
                print("Opção inválida.")

            pausa()

        # LANÇAR NOTAS
        elif op == "6":
            subtitulo("LANÇAR NOTAS")

            dados = m.read()
            if lista_vazia(dados, "Matrículas"):
                continue

            print("\nMATRÍCULAS DISPONÍVEIS")
            for x in dados:
                print_formatado(
                    ["ID Matrícula", "Aluno", "Curso", "Turma", "Nota1", "Nota2"],
                    x,
                )

            id_matricula = safe_int("ID Matrícula: ")

            if not any(x[0] == id_matricula for x in dados):
                print("\nMatrícula não existe.")
                pausa()
                continue

            m.update(
                id_matricula,
                safe_float("Nota 1: "),
                safe_float("Nota 2: "),
            )
            
            pausa()
            
        # EMITIR BOLETIM
        elif op == "7":
            subtitulo("EMITIR BOLETIM")

            dados = m.read()
            if lista_vazia(dados, "Matrículas"):
                continue

            print("\nMATRÍCULAS DISPONÍVEIS")
            for x in dados:
                print_formatado(["ID", "Aluno", "Curso"], [x[0], x[1], x[2]])

            id_matricula = safe_int("ID Matrícula: ")

            if not any(x[0] == id_matricula for x in dados):
                print("\nMatrícula não existe.")
                pausa()
                continue

            bol = m.find_by_id(id_matricula)
            if bol:
                titulo("BOLETIM OFICIAL")
                print_formatado(
                    ["Aluno", "Curso", "Período", "Ano", "Nota1", "Nota2", "Média"],
                    bol,
                )

            pausa()

        # SAIR
        elif op == "8":
            titulo("SISTEMA FINALIZADO")
            sys.exit(0)
        else:
            print("Opção inválida.")
            pausa()

if __name__ == "__main__":
    main()