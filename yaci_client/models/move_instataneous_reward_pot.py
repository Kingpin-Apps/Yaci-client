from enum import Enum


class MoveInstataneousRewardPot(str, Enum):
    RESERVES = "RESERVES"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
