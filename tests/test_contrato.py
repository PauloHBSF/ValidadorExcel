import pytest
from datetime import datetime
from pydantic import ValidationError

from src.contrato import Veiculos

def testa_caso_correto():
    
    dados_validos = {
        "id_veiculo": 0,
        "placa_veiculo": "BXD-4E26",
        "tipo_veiculo": "Vanderleia"
    }
    
    veich = Veiculos(**dados_validos)

    assert veich.id_veiculo == dados_validos["id_veiculo"]
    assert veich.placa_veiculo == dados_validos["placa_veiculo"]
    assert veich.tipo_veiculo == dados_validos["tipo_veiculo"]