from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voting_procedure_dto_vote import VotingProcedureDtoVote
from ..models.voting_procedure_dto_voter_type import VotingProcedureDtoVoterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VotingProcedureDto")


@_attrs_define
class VotingProcedureDto:
    """
    Attributes:
        block_number (int | Unset):
        block_time (int | Unset):
        id (UUID | Unset):
        tx_hash (str | Unset):
        index (int | Unset):
        slot (int | Unset):
        voter_type (VotingProcedureDtoVoterType | Unset):
        voter_hash (str | Unset):
        gov_action_tx_hash (str | Unset):
        gov_action_index (int | Unset):
        vote (VotingProcedureDtoVote | Unset):
        anchor_url (str | Unset):
        anchor_hash (str | Unset):
        epoch (int | Unset):
        drep_id (str | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    id: UUID | Unset = UNSET
    tx_hash: str | Unset = UNSET
    index: int | Unset = UNSET
    slot: int | Unset = UNSET
    voter_type: VotingProcedureDtoVoterType | Unset = UNSET
    voter_hash: str | Unset = UNSET
    gov_action_tx_hash: str | Unset = UNSET
    gov_action_index: int | Unset = UNSET
    vote: VotingProcedureDtoVote | Unset = UNSET
    anchor_url: str | Unset = UNSET
    anchor_hash: str | Unset = UNSET
    epoch: int | Unset = UNSET
    drep_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        tx_hash = self.tx_hash

        index = self.index

        slot = self.slot

        voter_type: str | Unset = UNSET
        if not isinstance(self.voter_type, Unset):
            voter_type = self.voter_type.value

        voter_hash = self.voter_hash

        gov_action_tx_hash = self.gov_action_tx_hash

        gov_action_index = self.gov_action_index

        vote: str | Unset = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote.value

        anchor_url = self.anchor_url

        anchor_hash = self.anchor_hash

        epoch = self.epoch

        drep_id = self.drep_id

        field_dict: dict[str, Any] = {}
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
        if drep_id is not UNSET:
            field_dict["drep_id"] = drep_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        tx_hash = d.pop("tx_hash", UNSET)

        index = d.pop("index", UNSET)

        slot = d.pop("slot", UNSET)

        _voter_type = d.pop("voter_type", UNSET)
        voter_type: VotingProcedureDtoVoterType | Unset
        if isinstance(_voter_type, Unset):
            voter_type = UNSET
        else:
            voter_type = VotingProcedureDtoVoterType(_voter_type)

        voter_hash = d.pop("voter_hash", UNSET)

        gov_action_tx_hash = d.pop("gov_action_tx_hash", UNSET)

        gov_action_index = d.pop("gov_action_index", UNSET)

        _vote = d.pop("vote", UNSET)
        vote: VotingProcedureDtoVote | Unset
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = VotingProcedureDtoVote(_vote)

        anchor_url = d.pop("anchor_url", UNSET)

        anchor_hash = d.pop("anchor_hash", UNSET)

        epoch = d.pop("epoch", UNSET)

        drep_id = d.pop("drep_id", UNSET)

        voting_procedure_dto = cls(
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
            drep_id=drep_id,
        )

        voting_procedure_dto.additional_properties = d
        return voting_procedure_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
