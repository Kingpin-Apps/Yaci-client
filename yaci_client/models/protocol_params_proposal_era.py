from enum import Enum


class ProtocolParamsProposalEra(str, Enum):
    ALLEGRA = "Allegra"
    ALONZO = "Alonzo"
    BABBAGE = "Babbage"
    BYRON = "Byron"
    CONWAY = "Conway"
    MARY = "Mary"
    SHELLEY = "Shelley"

    def __str__(self) -> str:
        return str(self.value)
