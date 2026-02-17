from database import get_connection

class TurmaDAO:

    def create(self, periodo, ano, horario, id_curso):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Turma (periodo, ano, horario, idCurso)
                    VALUES (%s, %s, %s, %s)
                """, (periodo, ano, horario, id_curso))

                conn.commit()
                print("Turma cadastrada com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar turma: {e}")

        finally:
            conn.close()

    def read(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        t.idTurma,
                        c.idCurso,
                        c.nome,
                        c.cargaHoraria,
                        t.periodo,
                        t.ano,
                        t.horario
                    FROM Turma t
                    JOIN Curso c ON t.idCurso = c.idCurso
                    ORDER BY t.idTurma
                """)
                return cursor.fetchall()

        finally:
            conn.close()

    def update(self, id_turma, periodo, ano, horario):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute("""
                    UPDATE Turma
                    SET periodo = %s,
                        ano = %s,
                        horario = %s
                    WHERE idTurma = %s
                """, (periodo, ano, horario, id_turma))

                if cursor.rowcount == 0:
                    print("Turma não encontrada!")
                else:
                    conn.commit()
                    print("Turma atualizada com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar turma: {e}")

        finally:
            conn.close()

    def delete(self, id_turma):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM Turma
                    WHERE idTurma = %s
                """, (id_turma,))

                if cursor.rowcount == 0:
                    print("Turma não encontrada!")
                else:
                    conn.commit()
                    print("Turma deletada com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar turma: {e}")

        finally:
            conn.close()

    def find_by_id(self, id_turma):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        t.idTurma,
                        c.idCurso,
                        c.nome,
                        c.cargaHoraria,
                        t.periodo,
                        t.ano,
                        t.horario
                    FROM Turma t
                    JOIN Curso c ON t.idCurso = c.idCurso
                    WHERE t.idTurma = %s
                """, (id_turma,))

                return cursor.fetchone()

        finally:
            conn.close()
