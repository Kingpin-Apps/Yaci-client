from enum import Enum


class TxAssetMintType(str, Enum):
    BURN = "BURN"
    MINT = "MINT"

    def __str__(self) -> str:
        return str(self.value)
