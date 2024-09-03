import importlib.metadata

from djchoices.choices import C, ChoiceItem, DjangoChoices


__version__ = importlib.metadata.version("django-choices")

__all__ = ["ChoiceItem", "DjangoChoices", "C"]
