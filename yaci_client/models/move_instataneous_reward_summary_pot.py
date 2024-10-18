from enum import Enum


class MoveInstataneousRewardSummaryPot(str, Enum):
    RESERVES = "RESERVES"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
