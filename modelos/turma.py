from dataclasses import dataclass


@dataclass
class Turma:
    idTurma: int | None
    periodo: int
    ano: int
    horario: str
    idCurso: int
