from dataclasses import dataclass


@dataclass
class Aluno:
    idAluno: int | None
    emailInstitucional: str
    idPessoa: int
