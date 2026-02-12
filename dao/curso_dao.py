from conexao import conectar

class CursoDAO:

    def inserir(self,nome):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO Curso (nome) VALUES (%s)",
                (nome,)
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute("SELECT * FROM Curso")
            return cur.fetchall()

    def atualizar(self,idCurso,nome):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "UPDATE Curso SET nome=%s WHERE idCurso=%s",
                (nome,idCurso)
            )

    def excluir(self,idCurso):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "DELETE FROM Curso WHERE idCurso=%s",
                (idCurso,)
            )
