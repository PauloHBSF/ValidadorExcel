from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from pydantic import (
    EmailStr,
    PositiveInt,
    PositiveFloat
)


class CategoriaEnum(str, Enum):
    categoria1 = "Vanderleia"
    categoria2 = "Bitruck"
    categoria3 = "Rodotrem"
    

class Veiculos(BaseModel): 
    id_veiculo: int
    placa_veiculo: str
    tipo_veiculo: CategoriaEnum
    