from dataclasses import dataclass


@dataclass
class Vaga:
    titulo: str
    empresa: str
    localizacao: str
    link: str
    tags: str