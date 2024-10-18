from enum import Enum


class RedeemerTag(str, Enum):
    CERT = "cert"
    MINT = "mint"
    PROPOSING = "proposing"
    REWARD = "reward"
    SPEND = "spend"
    VOTING = "voting"

    def __str__(self) -> str:
        return str(self.value)
