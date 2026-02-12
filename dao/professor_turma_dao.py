from conexao import conectar


class ProfessorTurmaDAO:
    def vincular(self, id_professor: int, id_turma: int):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Professor_Turma (idProfessor, idTurma)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING
                """,
                (id_professor, id_turma),
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                """
                SELECT pt.idProfessor, p.nome, pt.idTurma
                FROM Professor_Turma pt
                JOIN Professor pr ON pr.idProfessor = pt.idProfessor
                JOIN Pessoa p ON p.idPessoa = pr.idPessoa
                ORDER BY pt.idProfessor, pt.idTurma
                """
            )
            return cur.fetchall()
