from enum import Enum


class ScriptDtoType(str, Enum):
    PLUTUSV1 = "plutusV1"
    PLUTUSV2 = "plutusV2"
    PLUTUSV3 = "plutusV3"
    TIMELOCK = "timelock"

    def __str__(self) -> str:
        return str(self.value)
