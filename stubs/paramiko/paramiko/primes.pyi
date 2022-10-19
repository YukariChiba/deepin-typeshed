from typing import Tuple

class ModulusPack:
    pack: dict[int, list[Tuple[int, int]]]
    discarded: list[Tuple[int, str]]
    def __init__(self) -> None: ...
    def read_file(self, filename: str) -> None: ...
    def get_modulus(self, min: int, prefer: int, max: int) -> Tuple[int, int]: ...
