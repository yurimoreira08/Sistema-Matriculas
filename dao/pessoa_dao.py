from database import get_connection

class PessoaDAO:

    def create(self, nome, cpf, email, data_nasc):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Pessoa (nome, cpf, email, dataNascimento)
                    VALUES (%s, %s, %s, %s)
                """, (nome, cpf, email, data_nasc))

                conn.commit()
                print("Pessoa cadastrada com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar pessoa: {e}")

        finally:
            conn.close()

    def read(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        idPessoa,
                        nome,
                        cpf,
                        email,
                        dataNascimento
                    FROM Pessoa
                    ORDER BY idPessoa
                """)
                return cursor.fetchall()
        finally:
            conn.close()

    def update(self, id_pessoa, nome, cpf, email, data_nasc):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute("""
                    UPDATE Pessoa
                    SET nome = %s,
                        cpf = %s,
                        email = %s,
                        dataNascimento = %s
                    WHERE idPessoa = %s
                """, (nome, cpf, email, data_nasc, id_pessoa))

                if cursor.rowcount == 0:
                    print("Pessoa não encontrada!")
                else:
                    conn.commit()
                    print("Pessoa atualizada com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar pessoa: {e}")

        finally:
            conn.close()


    def delete(self, id_pessoa):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:

                cursor.execute("""
                    DELETE FROM Pessoa
                    WHERE idPessoa = %s
                """, (id_pessoa,))

                if cursor.rowcount == 0:
                    print("Pessoa não encontrada!")
                else:
                    conn.commit()
                    print("Pessoa deletada com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar pessoa: {e}")

        finally:
            conn.close()

    def find_by_id(self, id_pessoa):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        idPessoa,
                        nome,
                        cpf,
                        email,
                        dataNascimento
                    FROM Pessoa
                    WHERE idPessoa = %s
                """, (id_pessoa,))

                return cursor.fetchone()

        finally:
            conn.close()
