from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.move_instataneous_reward_summary_pot import MoveInstataneousRewardSummaryPot
from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveInstataneousRewardSummary")


@_attrs_define
class MoveInstataneousRewardSummary:
    """
    Attributes:
        tx_hash (str | Unset):
        slot (int | Unset):
        block_number (int | Unset):
        block_time (int | Unset):
        pot (MoveInstataneousRewardSummaryPot | Unset):
        cert_index (int | Unset):
        total_stake_keys (int | Unset):
        total_rewards (int | Unset):
    """

    tx_hash: str | Unset = UNSET
    slot: int | Unset = UNSET
    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    pot: MoveInstataneousRewardSummaryPot | Unset = UNSET
    cert_index: int | Unset = UNSET
    total_stake_keys: int | Unset = UNSET
    total_rewards: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_hash = self.tx_hash

        slot = self.slot

        block_number = self.block_number

        block_time = self.block_time

        pot: str | Unset = UNSET
        if not isinstance(self.pot, Unset):
            pot = self.pot.value

        cert_index = self.cert_index

        total_stake_keys = self.total_stake_keys

        total_rewards = self.total_rewards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if slot is not UNSET:
            field_dict["slot"] = slot
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if pot is not UNSET:
            field_dict["pot"] = pot
        if cert_index is not UNSET:
            field_dict["cert_index"] = cert_index
        if total_stake_keys is not UNSET:
            field_dict["total_stake_keys"] = total_stake_keys
        if total_rewards is not UNSET:
            field_dict["total_rewards"] = total_rewards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tx_hash = d.pop("tx_hash", UNSET)

        slot = d.pop("slot", UNSET)

        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        _pot = d.pop("pot", UNSET)
        pot: MoveInstataneousRewardSummaryPot | Unset
        if isinstance(_pot, Unset):
            pot = UNSET
        else:
            pot = MoveInstataneousRewardSummaryPot(_pot)

        cert_index = d.pop("cert_index", UNSET)

        total_stake_keys = d.pop("total_stake_keys", UNSET)

        total_rewards = d.pop("total_rewards", UNSET)

        move_instataneous_reward_summary = cls(
            tx_hash=tx_hash,
            slot=slot,
            block_number=block_number,
            block_time=block_time,
            pot=pot,
            cert_index=cert_index,
            total_stake_keys=total_stake_keys,
            total_rewards=total_rewards,
        )

        move_instataneous_reward_summary.additional_properties = d
        return move_instataneous_reward_summary

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
