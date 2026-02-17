from database import get_connection

class CursoDAO:

    def create(self, nome, carga):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Curso (nome, cargaHoraria)
                    VALUES (%s, %s)
                """, (nome, carga))

                conn.commit()
                print("Curso cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar curso: {e}")

        finally:
            conn.close()

    def read(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        c.idCurso,
                        c.nome,
                        c.cargaHoraria,
                        COALESCE(COUNT(DISTINCT m.idAluno), 0) AS qtd_alunos
                    FROM Curso c
                    LEFT JOIN Turma t ON c.idCurso = t.idCurso
                    LEFT JOIN Matricula m ON t.idTurma = m.idTurma
                    GROUP BY c.idCurso, c.nome, c.cargaHoraria
                    ORDER BY c.idCurso
                """)
                return cursor.fetchall()
        finally:
            conn.close()

    def update(self, id_curso, nome, carga):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    UPDATE Curso
                    SET nome = %s,
                        cargaHoraria = %s
                    WHERE idCurso = %s
                """, (nome, carga, id_curso))

                if cursor.rowcount == 0:
                    print("Curso não encontrado!")
                else:
                    conn.commit()
                    print("Curso atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar curso: {e}")

        finally:
            conn.close()

    def delete(self, id_curso):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM Curso
                    WHERE idCurso = %s
                """, (id_curso,))

                if cursor.rowcount == 0:
                    print("Curso não encontrado!")
                else:
                    conn.commit()
                    print("Curso deletado com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar curso: {e}")

        finally:
            conn.close()

    def find_by_id(self, id_curso):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        idCurso,
                        nome,
                        cargaHoraria
                    FROM Curso
                    WHERE idCurso = %s
                """, (id_curso,))

                return cursor.fetchone()

        finally:
            conn.close()
