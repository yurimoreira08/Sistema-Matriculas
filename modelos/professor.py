from dataclasses import dataclass


@dataclass
class Professor:
    idProfessor: int | None
    areaEspecializacao: str
    emailInstitucional: str
    idPessoa: int
