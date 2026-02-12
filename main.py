from dao.pessoa_dao import PessoaDAO
from dao.funcionario_dao import FuncionarioDAO
from dao.professor_dao import ProfessorDAO
from dao.aluno_dao import AlunoDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO
from dao.matricula_dao import MatriculaDAO


def mostrar(lista):
    print()
    if not lista:
        print("Nenhum registro encontrado.")
    for item in lista:
        print(item)
    print()


def ler_int(msg):
    return int(input(msg))


def ler_float(msg):
    return float(input(msg).replace(",", "."))


def main():
    pessoa = PessoaDAO()
    funcionario = FuncionarioDAO()
    professor = ProfessorDAO()
    aluno = AlunoDAO()
    curso = CursoDAO()
    turma = TurmaDAO()
    matricula = MatriculaDAO()

    while True:
        print("""
1 - Cadastrar
2 - Matricular Aluno
3 - Editar
4 - Listar
5 - Excluir
6 - Lançar Notas
7 - Emitir Boletim
8 - Sair
""")

        op = input("Escolha: ")

        # ================= CADASTRAR =================
        if op == "1":
            print("""
1 - Pessoa
2 - Funcionário
3 - Professor
4 - Aluno
5 - Curso
6 - Turma
""")
            sub = input("Escolha: ")

            if sub == "1":
                pessoa.inserir(
                    input("Nome: "),
                    input("CPF: "),
                    input("Email: ")
                )

            elif sub == "2":
                funcionario.inserir(
                    ler_int("ID Pessoa: ")
                )

            elif sub == "3":
                professor.inserir(
                    ler_int("ID Pessoa: ")
                )

            elif sub == "4":
                aluno.inserir(
                    ler_int("ID Pessoa: ")
                )

            elif sub == "5":
                curso.inserir(
                    input("Nome Curso: ")
                )

            elif sub == "6":
                turma.inserir(
                    ler_int("Ano: "),
                    ler_int("ID Curso: ")
                )

        # ================= MATRICULAR =================
        elif op == "2":
            mostrar(aluno.listar())
            mostrar(turma.listar())

            matricula.matricular(
                ler_int("ID Aluno: "),
                ler_int("ID Turma: ")
            )

        # ================= EDITAR =================
        elif op == "3":
            print("""
1 - Pessoa
2 - Funcionário
3 - Professor
4 - Aluno
5 - Curso
6 - Turma
""")
            sub = input("Escolha: ")

            if sub == "1":
                mostrar(pessoa.listar())
                pessoa.atualizar(
                    ler_int("ID Pessoa: "),
                    input("Novo Nome: "),
                    input("Novo CPF: "),
                    input("Novo Email: ")
                )

            elif sub == "2":
                mostrar(funcionario.listar())
                funcionario.atualizar(
                    ler_int("ID Funcionário: "),
                    ler_int("Novo ID Pessoa: ")
                )

            elif sub == "3":
                mostrar(professor.listar())
                professor.atualizar(
                    ler_int("ID Professor: "),
                    ler_int("Novo ID Pessoa: ")
                )

            elif sub == "4":
                mostrar(aluno.listar())
                aluno.atualizar(
                    ler_int("ID Aluno: "),
                    ler_int("Novo ID Pessoa: ")
                )

            elif sub == "5":
                mostrar(curso.listar())
                curso.atualizar(
                    ler_int("ID Curso: "),
                    input("Novo Nome: ")
                )

            elif sub == "6":
                mostrar(turma.listar())
                turma.atualizar(
                    ler_int("ID Turma: "),
                    ler_int("Novo Ano: "),
                    ler_int("Novo ID Curso: ")
                )

        # ================= LISTAR =================
        elif op == "4":
            print("""
1 - Pessoa
2 - Funcionário
3 - Professor
4 - Aluno
5 - Curso
6 - Turma
""")
            sub = input("Escolha: ")

            if sub == "1":
                mostrar(pessoa.listar())
            elif sub == "2":
                mostrar(funcionario.listar())
            elif sub == "3":
                mostrar(professor.listar())
            elif sub == "4":
                mostrar(aluno.listar())
            elif sub == "5":
                mostrar(curso.listar())
            elif sub == "6":
                mostrar(turma.listar())

        # ================= EXCLUIR =================
        elif op == "5":
            print("""
1 - Pessoa
2 - Funcionário
3 - Professor
4 - Aluno
5 - Curso
6 - Turma
""")
            sub = input("Escolha: ")

            if sub == "1":
                mostrar(pessoa.listar())
                pessoa.excluir(ler_int("ID Pessoa: "))

            elif sub == "2":
                mostrar(funcionario.listar())
                funcionario.excluir(ler_int("ID Funcionário: "))

            elif sub == "3":
                mostrar(professor.listar())
                professor.excluir(ler_int("ID Professor: "))

            elif sub == "4":
                mostrar(aluno.listar())
                aluno.excluir(ler_int("ID Aluno: "))

            elif sub == "5":
                mostrar(curso.listar())
                curso.excluir(ler_int("ID Curso: "))

            elif sub == "6":
                mostrar(turma.listar())
                turma.excluir(ler_int("ID Turma: "))

        # ================= LANÇAR NOTAS =================
        elif op == "6":
            mostrar(aluno.listar())

            matricula.lancar_notas(
                ler_int("ID Aluno: "),
                ler_float("Nota 1: "),
                ler_float("Nota 2: ")
            )

        # ================= BOLETIM =================
        elif op == "7":
            mostrar(aluno.listar())

            dados = matricula.boletim(
                ler_int("ID Aluno: ")
            )

            for nome, curso_nome, n1, n2 in dados:
                media = (float(n1) + float(n2)) / 2 if n1 and n2 else 0
                print(
                    f"Aluno: {nome} | Curso: {curso_nome} "
                    f"| N1: {n1} | N2: {n2} | Média: {media}"
                )

        elif op == "8":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")
            

if __name__ == "__main__":
    main()
