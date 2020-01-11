from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class GenderEnum(ChoiceEnum):
    MALE = 'male'
    FEMALE = 'female'
    UNSPECIFIED = 'unspecified'

