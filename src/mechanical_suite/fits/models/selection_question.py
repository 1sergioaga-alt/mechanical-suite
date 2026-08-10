from dataclasses import dataclass


@dataclass(frozen=True)
class SelectionQuestion:
    id: str
    options: tuple[str, ...]