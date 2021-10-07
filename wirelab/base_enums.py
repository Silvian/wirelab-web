from enum import Enum


class ChoiceEnum(Enum):
    """Choice fields abstract base enum."""

    @classmethod
    def choices(cls):
        return tuple((key.name, key.value) for key in cls)
