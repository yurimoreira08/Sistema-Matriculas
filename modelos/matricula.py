from dataclasses import dataclass


@dataclass
class Matricula:
    idMatricula: int | None
    dataMatricula: str
    situacao: str
    nota1: float | None
    nota2: float | None
    idAluno: int
    idTurma: int
