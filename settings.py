from enum import Enum
from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field, field_validator


class Languages(Enum):
    English = "English"
    French = "French"
    German = "German"
    Italian = "Italian"
    Spanish = "Spanish"
    Russian = "Russian"
    Chinese = "Chinese"
    Japanese = "Japanese"
    Korean = "Korean"
    NoLanguage = "None"
    Human = "Human"


class MySettings(BaseModel):
    prompt_prefix: str = Field(
        title="Prompt prefix",
        default="""You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
You are curious, funny and talk like the Cheshire Cat from Alice's adventures in wonderland.
You answer Human with a focus on the following context.
""",
        extra={"type": "TextArea"},
    )
    k: int = 3
    threshold: float = 0.7
    latest_n_history: int = 5
    user_name: str | None = "Human"
    language: Languages = Languages.English

    @field_validator("threshold")
    @classmethod
    def threshold_validator(cls, v):
        if v <= 0:
            raise ValueError("Memory threshold must be greater than 0")

    @field_validator("latest_n_history")
    @classmethod
    def latest_n_history_validator(cls, v):
        if v < 1:
            raise ValueError("Latest `n` history threshold must be greater than 1")

@plugin
def settings_model():
    return MySettings
