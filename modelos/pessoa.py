from dataclasses import dataclass


@dataclass
class Pessoa:
    idPessoa: int | None
    nome: str
    cpf: str
    email: str
    dataNascimento: str
