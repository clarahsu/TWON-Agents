import typing

import pydantic

from src.integration import Integration
from src.persona import Persona
from src.schemas import model


class BaseRequest(pydantic.BaseModel):
    persona: typing.Union[typing.List[str], Persona]
    integration: Integration = Integration.model_config["json_schema_extra"]["examples"][0]

    language: typing.Literal['English', 'German', 'Dutch'] = "English"
    platform: typing.Literal['Twitter', 'Reddit', 'Facebook', 'Telegram'] = "Twitter"

    history: model.History = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "persona": [
                        Persona.model_config["json_schema_extra"]["examples"][0]['id'],
                        Persona.model_config["json_schema_extra"]["examples"][1]['id'],
                    ],
                    "integration": Integration.model_config["json_schema_extra"]["examples"][0],
                    "language": "English",
                    "platform": "Twitter",
                    "history": model.History.model_config["json_schema_extra"]["examples"][0],
                }
            ]
        }
    }
