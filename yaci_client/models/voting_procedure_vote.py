from enum import Enum


class VotingProcedureVote(str, Enum):
    ABSTAIN = "ABSTAIN"
    NO = "NO"
    YES = "YES"

    def __str__(self) -> str:
        return str(self.value)
