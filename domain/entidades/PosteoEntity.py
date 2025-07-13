from typing import List, Any
from dataclasses import dataclass
from uuid import UUID
from datetime import date

@dataclass
class PosteoEntity:
    id: UUID
    fecha: date
    cuerpo: List[Any]
    tipo: str
