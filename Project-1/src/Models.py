from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Literal

class AnalyzeFeedback(BaseModel):
    feeling: Literal["positive", "negative", "neutral"]
    customer_service_rating: int = Field(
        ge=1,
        le=5,
        description="An integer from 1 to 5 representing customer satisfaction."
    )
    short_summary: str = Field(
        description="A brief summary of the feedback in no more than 10 words."
    )
    name: str

    @field_validator('name')
    @classmethod
    def validate_real_name(cls, value: str) -> str:
        clean_value = value.strip()

        if clean_value.lower() == "unknown":
            return "Unknown"
        
        prohibited_terms = ["no", "not", "waited", "buy", "repetitive"]
        if any(term in clean_value.lower() for term in prohibited_terms):
            raise ValueError(f"Invalid/AI-generated name: '{value}'")
        
        if not all(part.isalpha() for part in clean_value.split()):
            raise ValueError(f"Name contains invalid characters: '{value}'")

        return clean_value.title()

    # EXTRA RULE: prevents an absurd inconsistency (Positive with a score of 1)
    @model_validator(mode='after')
    def validate_consistency(self):
        if self.feeling == "positive" and self.customer_service_rating <= 2:
            raise ValueError("Inconsistency: A positive sentiment cannot have a score of 2 or lower!")
        return self
    
    