from enum import Enum


class VotingProcedureDtoVoterType(str, Enum):
    CONSTITUTIONAL_COMMITTEE_HOT_KEY_HASH = "CONSTITUTIONAL_COMMITTEE_HOT_KEY_HASH"
    CONSTITUTIONAL_COMMITTEE_HOT_SCRIPT_HASH = (
        "CONSTITUTIONAL_COMMITTEE_HOT_SCRIPT_HASH"
    )
    DREP_KEY_HASH = "DREP_KEY_HASH"
    DREP_SCRIPT_HASH = "DREP_SCRIPT_HASH"
    STAKING_POOL_KEY_HASH = "STAKING_POOL_KEY_HASH"

    def __str__(self) -> str:
        return str(self.value)
