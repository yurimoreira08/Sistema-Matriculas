from dataclasses import dataclass


@dataclass
class Funcionario:
    idFuncionario: int | None
    cargo: str
    emailInstitucional: str
    idPessoa: int
