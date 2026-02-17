from database import get_connection

class MatriculaDAO:

    def create(self, id_aluno, id_turma):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Matricula (idAluno, idTurma)
                    VALUES (%s, %s)
                """, (id_aluno, id_turma))

                conn.commit()
                print("Matrícula realizada com sucesso!")

        except Exception as e:
            print(f"Erro na matrícula: {e}")

        finally:
            conn.close()

    def read(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        m.idMatricula,
                        p.nome,
                        c.nome,
                        t.idTurma,
                        m.nota1,
                        m.nota2
                    FROM Matricula m
                    JOIN Aluno a ON m.idAluno = a.idAluno
                    JOIN Pessoa p ON a.idPessoa = p.idPessoa
                    JOIN Turma t ON m.idTurma = t.idTurma
                    JOIN Curso c ON t.idCurso = c.idCurso
                    ORDER BY m.idMatricula
                """)
                return cursor.fetchall()

        finally:
            conn.close()

    def update(self, id_matricula, n1, n2):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute("""
                    UPDATE Matricula
                    SET nota1 = %s,
                        nota2 = %s
                    WHERE idMatricula = %s
                """, (n1, n2, id_matricula))

                if cursor.rowcount == 0:
                    print("Matrícula não encontrada!")
                else:
                    conn.commit()
                    print("Notas lançadas com sucesso!")

        except Exception as e:
            print(f"Erro ao lançar notas: {e}")

        finally:
            conn.close()

    def delete(self, id_matricula):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute("""
                    DELETE FROM Matricula
                    WHERE idMatricula = %s
                """, (id_matricula,))

                if cursor.rowcount == 0:
                    print("Matrícula não encontrada!")
                else:
                    conn.commit()
                    print("Matrícula cancelada com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar matrícula: {e}")

        finally:
            conn.close()

    def find_by_id(self, id_matricula):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        p.nome,
                        c.nome,
                        t.periodo,
                        t.ano,
                        m.nota1,
                        m.nota2,
                        CASE
                            WHEN m.nota1 IS NOT NULL AND m.nota2 IS NOT NULL
                            THEN ROUND((m.nota1 + m.nota2) / 2.0, 2)
                            ELSE NULL
                        END AS media
                    FROM Matricula m
                    JOIN Aluno a ON m.idAluno = a.idAluno
                    JOIN Pessoa p ON a.idPessoa = p.idPessoa
                    JOIN Turma t ON m.idTurma = t.idTurma
                    JOIN Curso c ON t.idCurso = c.idCurso
                    WHERE m.idMatricula = %s
                """, (id_matricula,))

                return cursor.fetchone()

        finally:
            conn.close()
