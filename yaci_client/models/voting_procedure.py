from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voting_procedure_vote import VotingProcedureVote
from ..models.voting_procedure_voter_type import VotingProcedureVoterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VotingProcedure")


@_attrs_define
class VotingProcedure:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        id (Union[Unset, str]):
        tx_hash (Union[Unset, str]):
        index (Union[Unset, int]):
        slot (Union[Unset, int]):
        voter_type (Union[Unset, VotingProcedureVoterType]):
        voter_hash (Union[Unset, str]):
        gov_action_tx_hash (Union[Unset, str]):
        gov_action_index (Union[Unset, int]):
        vote (Union[Unset, VotingProcedureVote]):
        anchor_url (Union[Unset, str]):
        anchor_hash (Union[Unset, str]):
        epoch (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    voter_type: Union[Unset, VotingProcedureVoterType] = UNSET
    voter_hash: Union[Unset, str] = UNSET
    gov_action_tx_hash: Union[Unset, str] = UNSET
    gov_action_index: Union[Unset, int] = UNSET
    vote: Union[Unset, VotingProcedureVote] = UNSET
    anchor_url: Union[Unset, str] = UNSET
    anchor_hash: Union[Unset, str] = UNSET
    epoch: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        id = self.id

        tx_hash = self.tx_hash

        index = self.index

        slot = self.slot

        voter_type: Union[Unset, str] = UNSET
        if not isinstance(self.voter_type, Unset):
            voter_type = self.voter_type.value

        voter_hash = self.voter_hash

        gov_action_tx_hash = self.gov_action_tx_hash

        gov_action_index = self.gov_action_index

        vote: Union[Unset, str] = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote.value

        anchor_url = self.anchor_url

        anchor_hash = self.anchor_hash

        epoch = self.epoch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if id is not UNSET:
            field_dict["id"] = id
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if index is not UNSET:
            field_dict["index"] = index
        if slot is not UNSET:
            field_dict["slot"] = slot
        if voter_type is not UNSET:
            field_dict["voter_type"] = voter_type
        if voter_hash is not UNSET:
            field_dict["voter_hash"] = voter_hash
        if gov_action_tx_hash is not UNSET:
            field_dict["gov_action_tx_hash"] = gov_action_tx_hash
        if gov_action_index is not UNSET:
            field_dict["gov_action_index"] = gov_action_index
        if vote is not UNSET:
            field_dict["vote"] = vote
        if anchor_url is not UNSET:
            field_dict["anchor_url"] = anchor_url
        if anchor_hash is not UNSET:
            field_dict["anchor_hash"] = anchor_hash
        if epoch is not UNSET:
            field_dict["epoch"] = epoch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        id = d.pop("id", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        index = d.pop("index", UNSET)

        slot = d.pop("slot", UNSET)

        _voter_type = d.pop("voter_type", UNSET)
        voter_type: Union[Unset, VotingProcedureVoterType]
        if isinstance(_voter_type, Unset):
            voter_type = UNSET
        else:
            voter_type = VotingProcedureVoterType(_voter_type)

        voter_hash = d.pop("voter_hash", UNSET)

        gov_action_tx_hash = d.pop("gov_action_tx_hash", UNSET)

        gov_action_index = d.pop("gov_action_index", UNSET)

        _vote = d.pop("vote", UNSET)
        vote: Union[Unset, VotingProcedureVote]
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = VotingProcedureVote(_vote)

        anchor_url = d.pop("anchor_url", UNSET)

        anchor_hash = d.pop("anchor_hash", UNSET)

        epoch = d.pop("epoch", UNSET)

        voting_procedure = cls(
            block_number=block_number,
            block_time=block_time,
            id=id,
            tx_hash=tx_hash,
            index=index,
            slot=slot,
            voter_type=voter_type,
            voter_hash=voter_hash,
            gov_action_tx_hash=gov_action_tx_hash,
            gov_action_index=gov_action_index,
            vote=vote,
            anchor_url=anchor_url,
            anchor_hash=anchor_hash,
            epoch=epoch,
        )

        voting_procedure.additional_properties = d
        return voting_procedure

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
