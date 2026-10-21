from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StakeAccountInfo")


@_attrs_define
class StakeAccountInfo:
    """
    Attributes:
        stake_address (str | Unset):
        controlled_amount (int | Unset):
        withdrawable_amount (int | Unset):
        pool_id (str | Unset):
    """

    stake_address: str | Unset = UNSET
    controlled_amount: int | Unset = UNSET
    withdrawable_amount: int | Unset = UNSET
    pool_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stake_address = self.stake_address

        controlled_amount = self.controlled_amount

        withdrawable_amount = self.withdrawable_amount

        pool_id = self.pool_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stake_address is not UNSET:
            field_dict["stake_address"] = stake_address
        if controlled_amount is not UNSET:
            field_dict["controlled_amount"] = controlled_amount
        if withdrawable_amount is not UNSET:
            field_dict["withdrawable_amount"] = withdrawable_amount
        if pool_id is not UNSET:
            field_dict["pool_id"] = pool_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stake_address = d.pop("stake_address", UNSET)

        controlled_amount = d.pop("controlled_amount", UNSET)

        withdrawable_amount = d.pop("withdrawable_amount", UNSET)

        pool_id = d.pop("pool_id", UNSET)

        stake_account_info = cls(
            stake_address=stake_address,
            controlled_amount=controlled_amount,
            withdrawable_amount=withdrawable_amount,
            pool_id=pool_id,
        )

        stake_account_info.additional_properties = d
        return stake_account_info

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
