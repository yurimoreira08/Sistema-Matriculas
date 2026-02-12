from dataclasses import dataclass


@dataclass
class Disciplina:
    idDisciplina: int | None
    nome: str
    cargaHoraria: int
    codigoDisciplina: str
    idCurso: int
