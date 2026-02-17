from database import get_connection

class AlunoDAO:

    def create(self, email_inst, id_pessoa):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Aluno (emailInstitucional, idPessoa)
                    VALUES (%s, %s)
                """, (email_inst, id_pessoa))

                conn.commit()
                print("Aluno cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar aluno: {e}")

        finally:
            conn.close()

    def read(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        a.idAluno,
                        p.nome,
                        a.emailInstitucional
                    FROM Aluno a
                    JOIN Pessoa p ON a.idPessoa = p.idPessoa
                    ORDER BY a.idAluno
                """)
                return cursor.fetchall()
        finally:
            conn.close()

    def update(self, id_aluno, email_inst):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute(
                    "SELECT idPessoa FROM Aluno WHERE idAluno = %s",
                    (id_aluno,)
                )

                resultado = cursor.fetchone()

                if not resultado:
                    print("Aluno não encontrado!")
                    return

                cursor.execute("""
                    UPDATE Aluno
                    SET emailInstitucional = %s
                    WHERE idAluno = %s
                """, (email_inst, id_aluno))

                conn.commit()
                print("Aluno atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar aluno: {e}")

        finally:
            conn.close()

    def delete(self, id_aluno):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Aluno WHERE idAluno = %s",
                    (id_aluno,)
                )

                if cursor.rowcount == 0:
                    print("Aluno não encontrado!")
                else:
                    conn.commit()
                    print("Aluno deletado com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar aluno: {e}")

        finally:
            conn.close()

    def find_by_id(self, id_aluno):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        a.idAluno,
                        p.idPessoa,
                        p.nome,
                        p.cpf,
                        p.email,
                        a.emailInstitucional
                    FROM Aluno a
                    JOIN Pessoa p ON a.idPessoa = p.idPessoa
                    WHERE a.idAluno = %s
                """, (id_aluno,))
                return cursor.fetchone()
        finally:
            conn.close()
