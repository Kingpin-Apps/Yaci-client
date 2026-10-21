from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Epoch")


@_attrs_define
class Epoch:
    """
    Attributes:
        number (int | Unset):
        block_count (int | Unset):
        transaction_count (int | Unset):
        total_output (int | Unset):
        total_fees (int | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        max_slot (int | Unset):
    """

    number: int | Unset = UNSET
    block_count: int | Unset = UNSET
    transaction_count: int | Unset = UNSET
    total_output: int | Unset = UNSET
    total_fees: int | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    max_slot: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        block_count = self.block_count

        transaction_count = self.transaction_count

        total_output = self.total_output

        total_fees = self.total_fees

        start_time = self.start_time

        end_time = self.end_time

        max_slot = self.max_slot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if block_count is not UNSET:
            field_dict["block_count"] = block_count
        if transaction_count is not UNSET:
            field_dict["transaction_count"] = transaction_count
        if total_output is not UNSET:
            field_dict["total_output"] = total_output
        if total_fees is not UNSET:
            field_dict["total_fees"] = total_fees
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if max_slot is not UNSET:
            field_dict["max_slot"] = max_slot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number", UNSET)

        block_count = d.pop("block_count", UNSET)

        transaction_count = d.pop("transaction_count", UNSET)

        total_output = d.pop("total_output", UNSET)

        total_fees = d.pop("total_fees", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        max_slot = d.pop("max_slot", UNSET)

        epoch = cls(
            number=number,
            block_count=block_count,
            transaction_count=transaction_count,
            total_output=total_output,
            total_fees=total_fees,
            start_time=start_time,
            end_time=end_time,
            max_slot=max_slot,
        )

        epoch.additional_properties = d
        return epoch

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
