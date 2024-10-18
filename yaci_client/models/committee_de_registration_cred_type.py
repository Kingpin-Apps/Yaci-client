from enum import Enum


class CommitteeDeRegistrationCredType(str, Enum):
    ADDR_KEYHASH = "ADDR_KEYHASH"
    SCRIPTHASH = "SCRIPTHASH"

    def __str__(self) -> str:
        return str(self.value)
