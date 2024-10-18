from enum import Enum


class TxContractDetailsType(str, Enum):
    NATIVE_SCRIPT = "NATIVE_SCRIPT"
    PLUTUS_V1 = "PLUTUS_V1"
    PLUTUS_V2 = "PLUTUS_V2"
    PLUTUS_V3 = "PLUTUS_V3"

    def __str__(self) -> str:
        return str(self.value)
