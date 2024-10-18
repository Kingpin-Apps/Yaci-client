from enum import Enum


class DelegationVoteDrepType(str, Enum):
    ABSTAIN = "ABSTAIN"
    ADDR_KEYHASH = "ADDR_KEYHASH"
    NO_CONFIDENCE = "NO_CONFIDENCE"
    SCRIPTHASH = "SCRIPTHASH"

    def __str__(self) -> str:
        return str(self.value)
