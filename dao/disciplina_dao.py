from conexao import conectar


class DisciplinaDAO:
    def inserir(self, nome: str, carga_horaria: int, codigo: str, id_curso: int):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Disciplina (nome, cargaHoraria, codigoDisciplina, idCurso)
                VALUES (%s, %s, %s, %s)
                """,
                (nome, carga_horaria, codigo, id_curso),
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                """
                SELECT d.idDisciplina, d.nome, d.cargaHoraria, d.codigoDisciplina, c.nome AS curso
                FROM Disciplina d
                JOIN Curso c ON c.idCurso = d.idCurso
                ORDER BY d.idDisciplina
                """
            )
            return cur.fetchall()

    def atualizar(self, id_disc: int, nome: str, carga_horaria: int, codigo: str, id_curso: int):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                """
                UPDATE Disciplina
                SET nome=%s, cargaHoraria=%s, codigoDisciplina=%s, idCurso=%s
                WHERE idDisciplina=%s
                """,
                (nome, carga_horaria, codigo, id_curso, id_disc),
            )

    def excluir(self, id_disc: int):
        with conectar() as con, con.cursor() as cur:
            cur.execute("DELETE FROM Disciplina WHERE idDisciplina=%s", (id_disc,))
