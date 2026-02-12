from conexao import conectar

class AlunoDAO:

    def inserir(self,idPessoa):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO Aluno (idPessoa) VALUES (%s)",
                (idPessoa,)
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute("""
                SELECT a.idAluno,p.nome
                FROM Aluno a
                JOIN Pessoa p ON p.idPessoa=a.idPessoa
            """)
            return cur.fetchall()

    def atualizar(self,idAluno,idPessoa):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "UPDATE Aluno SET idPessoa=%s WHERE idAluno=%s",
                (idPessoa,idAluno)
            )

    def excluir(self,idAluno):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "DELETE FROM Aluno WHERE idAluno=%s",
                (idAluno,)
            )
