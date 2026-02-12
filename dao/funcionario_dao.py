from conexao import conectar

class FuncionarioDAO:

    def inserir(self,idPessoa):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO Funcionario (idPessoa) VALUES (%s)",
                (idPessoa,)
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute("""
                SELECT f.idFuncionario,p.nome
                FROM Funcionario f
                JOIN Pessoa p ON p.idPessoa=f.idPessoa
            """)
            return cur.fetchall()

    def atualizar(self,idFuncionario,idPessoa):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "UPDATE Funcionario SET idPessoa=%s WHERE idFuncionario=%s",
                (idPessoa,idFuncionario)
            )

    def excluir(self,idFuncionario):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "DELETE FROM Funcionario WHERE idFuncionario=%s",
                (idFuncionario,)
            )
