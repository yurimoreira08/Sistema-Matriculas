from conexao import conectar

class MatriculaDAO:

    def matricular(self,idAluno,idTurma):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO Matricula (idAluno,idTurma) VALUES (%s,%s)",
                (idAluno,idTurma)
            )

    def lancar_notas(self,idAluno,nota1,nota2):
        with conectar() as con, con.cursor() as cur:
            cur.execute("""
                UPDATE Matricula
                SET nota1=%s,nota2=%s
                WHERE idAluno=%s
            """,(nota1,nota2,idAluno))

    def boletim(self,idAluno):
        with conectar() as con, con.cursor() as cur:
            cur.execute("""
                SELECT p.nome,c.nome,m.nota1,m.nota2
                FROM Matricula m
                JOIN Aluno a ON a.idAluno=m.idAluno
                JOIN Pessoa p ON p.idPessoa=a.idPessoa
                JOIN Turma t ON t.idTurma=m.idTurma
                JOIN Curso c ON c.idCurso=t.idCurso
                WHERE a.idAluno=%s
            """,(idAluno,))
            return cur.fetchall()
