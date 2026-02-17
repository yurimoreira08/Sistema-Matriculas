from database import get_connection

class ProfessorDAO:

    def create(self, area, email_inst, id_pessoa):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Professor (areaEspecializacao, emailInstitucional, idPessoa)
                    VALUES (%s, %s, %s)
                """, (area, email_inst, id_pessoa))

                conn.commit()
                print("Professor cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar professor: {e}")

        finally:
            conn.close()

    def read(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        pr.idProfessor,
                        p.nome,
                        pr.areaEspecializacao,
                        pr.emailInstitucional
                    FROM Professor pr
                    JOIN Pessoa p ON pr.idPessoa = p.idPessoa
                    ORDER BY pr.idProfessor
                """)
                return cursor.fetchall()

        finally:
            conn.close()

    def update(self, id_prof, area, email_inst):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute(
                    "SELECT idPessoa FROM Professor WHERE idProfessor = %s",
                    (id_prof,)
                )

                resultado = cursor.fetchone()

                if not resultado:
                    print("Professor não encontrado!")
                    return

                cursor.execute("""
                    UPDATE Professor
                    SET areaEspecializacao = %s,
                        emailInstitucional = %s
                    WHERE idProfessor = %s
                """, (area, email_inst, id_prof))

                conn.commit()
                print("Professor atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar professor: {e}")

        finally:
            conn.close()

    def delete(self, id_prof):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Professor WHERE idProfessor = %s",
                    (id_prof,)
                )

                if cursor.rowcount == 0:
                    print("Professor não encontrado!")
                else:
                    conn.commit()
                    print("Professor deletado com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar professor: {e}")

        finally:
            conn.close()

    def find_by_id(self, id_prof):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        pr.idProfessor,
                        p.idPessoa,
                        p.nome,
                        p.cpf,
                        p.email,
                        pr.areaEspecializacao,
                        pr.emailInstitucional
                    FROM Professor pr
                    JOIN Pessoa p ON pr.idPessoa = p.idPessoa
                    WHERE pr.idProfessor = %s
                """, (id_prof,))

                return cursor.fetchone()

        finally:
            conn.close()
