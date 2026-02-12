from dataclasses import dataclass


@dataclass
class Curso:
    idCurso: int | None
    nome: str
    cargaHoraria: int
