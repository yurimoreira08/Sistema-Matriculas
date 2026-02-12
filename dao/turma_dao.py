from conexao import conectar

class TurmaDAO:

    def inserir(self,ano,idCurso):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO Turma (ano,idCurso) VALUES (%s,%s)",
                (ano,idCurso)
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute("""
                SELECT t.idTurma,t.ano,c.nome
                FROM Turma t
                JOIN Curso c ON c.idCurso=t.idCurso
            """)
            return cur.fetchall()

    def atualizar(self,idTurma,ano,idCurso):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "UPDATE Turma SET ano=%s,idCurso=%s WHERE idTurma=%s",
                (ano,idCurso,idTurma)
            )

    def excluir(self,idTurma):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "DELETE FROM Turma WHERE idTurma=%s",
                (idTurma,)
            )
