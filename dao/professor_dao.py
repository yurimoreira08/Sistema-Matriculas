from conexao import conectar

class ProfessorDAO:

    def inserir(self,idPessoa):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO Professor (idPessoa) VALUES (%s)",
                (idPessoa,)
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute("""
                SELECT pr.idProfessor,p.nome
                FROM Professor pr
                JOIN Pessoa p ON p.idPessoa=pr.idPessoa
            """)
            return cur.fetchall()

    def atualizar(self,idProfessor,idPessoa):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "UPDATE Professor SET idPessoa=%s WHERE idProfessor=%s",
                (idPessoa,idProfessor)
            )

    def excluir(self,idProfessor):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "DELETE FROM Professor WHERE idProfessor=%s",
                (idProfessor,)
            )
