import os
from abc import ABC, abstractmethod
from typing import Callable

from dittoed.util.python_path import import_sibling_modules


registry = {}


def register(name: str) -> Callable:
    def wrap(cls):
        if name not in registry:
            registry[name] = cls

    return wrap


class Installable(ABC):
    @abstractmethod
    def sync(self) -> None:
        pass

    def enabled(self) -> bool:
        return True


# Trigger installable registration.
import_sibling_modules(exceptions=os.path.basename(__file__))
