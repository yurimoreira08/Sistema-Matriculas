from conexao import conectar

class PessoaDAO:

    def inserir(self,nome,cpf,email):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "INSERT INTO Pessoa (nome,cpf,email) VALUES (%s,%s,%s)",
                (nome,cpf,email)
            )

    def listar(self):
        with conectar() as con, con.cursor() as cur:
            cur.execute("SELECT * FROM Pessoa")
            return cur.fetchall()

    def atualizar(self,id,nome,cpf,email):
        with conectar() as con, con.cursor() as cur:
            cur.execute(
                "UPDATE Pessoa SET nome=%s,cpf=%s,email=%s WHERE idPessoa=%s",
                (nome,cpf,email,id)
            )

    def excluir(self,id):
        with conectar() as con, con.cursor() as cur:
            cur.execute("DELETE FROM Pessoa WHERE idPessoa=%s",(id,))
