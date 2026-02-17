from database import get_connection

class FuncionarioDAO:

    def create(self, cargo, email_inst, id_pessoa):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Funcionario (cargo, emailInstitucional, idPessoa)
                    VALUES (%s, %s, %s)
                """, (cargo, email_inst, id_pessoa))

                conn.commit()
                print("Funcionário cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar funcionário: {e}")

        finally:
            conn.close()

    def read(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        f.idFuncionario,
                        p.nome,
                        f.cargo,
                        f.emailInstitucional
                    FROM Funcionario f
                    JOIN Pessoa p ON f.idPessoa = p.idPessoa
                    ORDER BY f.idFuncionario
                """)
                return cursor.fetchall()

        finally:
            conn.close()

    def update(self, id_func, cargo, email_inst):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute(
                    "SELECT idPessoa FROM Funcionario WHERE idFuncionario = %s",
                    (id_func,)
                )

                resultado = cursor.fetchone()

                if not resultado:
                    print("Funcionário não encontrado!")
                    return

                cursor.execute("""
                    UPDATE Funcionario
                    SET cargo = %s,
                        emailInstitucional = %s
                    WHERE idFuncionario = %s
                """, (cargo, email_inst, id_func))

                conn.commit()
                print("Funcionário atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar funcionário: {e}")

        finally:
            conn.close()

    def delete(self, id_func):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Funcionario WHERE idFuncionario = %s",
                    (id_func,)
                )

                if cursor.rowcount == 0:
                    print("Funcionário não encontrado!")
                else:
                    conn.commit()
                    print("Funcionário deletado com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar funcionário: {e}")

        finally:
            conn.close()

    def find_by_id(self, id_func):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        f.idFuncionario,
                        p.idPessoa,
                        p.nome,
                        p.cpf,
                        p.email,
                        f.cargo,
                        f.emailInstitucional
                    FROM Funcionario f
                    JOIN Pessoa p ON f.idPessoa = p.idPessoa
                    WHERE f.idFuncionario = %s
                """, (id_func,))

                return cursor.fetchone()

        finally:
            conn.close()
