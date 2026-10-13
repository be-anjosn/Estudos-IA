from pydantic import BaseModel, Field
from typing import Literal

class AnaliseFeedback(BaseModel):
    sentimento: Literal["positivo","negativo", "neutro"]
    nota_atendimento: int = Field(
        ge=1,
        le=5,
        description="Nota de que representa o nível de satisfação do cliente, sendo 1 - muito insatisfeito e 5 - muito satisfeito"
    )
    resumo_curto: str = Field( 
        description="Um resumo curto em 1 linha sobre o assunto"
    )
