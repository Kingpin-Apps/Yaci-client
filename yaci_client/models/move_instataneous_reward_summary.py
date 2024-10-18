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

from ..models.move_instataneous_reward_summary_pot import (
    MoveInstataneousRewardSummaryPot,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveInstataneousRewardSummary")


@_attrs_define
class MoveInstataneousRewardSummary:
    """
    Attributes:
        tx_hash (Union[Unset, str]):
        slot (Union[Unset, int]):
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        pot (Union[Unset, MoveInstataneousRewardSummaryPot]):
        cert_index (Union[Unset, int]):
        total_stake_keys (Union[Unset, int]):
        total_rewards (Union[Unset, int]):
    """

    tx_hash: Union[Unset, str] = UNSET
    slot: Union[Unset, int] = UNSET
    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    pot: Union[Unset, MoveInstataneousRewardSummaryPot] = UNSET
    cert_index: Union[Unset, int] = UNSET
    total_stake_keys: Union[Unset, int] = UNSET
    total_rewards: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tx_hash = self.tx_hash

        slot = self.slot

        block_number = self.block_number

        block_time = self.block_time

        pot: Union[Unset, str] = UNSET
        if not isinstance(self.pot, Unset):
            pot = self.pot.value

        cert_index = self.cert_index

        total_stake_keys = self.total_stake_keys

        total_rewards = self.total_rewards

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tx_hash = d.pop("tx_hash", UNSET)

        slot = d.pop("slot", UNSET)

        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        _pot = d.pop("pot", UNSET)
        pot: Union[Unset, MoveInstataneousRewardSummaryPot]
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
