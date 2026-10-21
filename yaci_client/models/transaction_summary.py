from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionSummary")


@_attrs_define
class TransactionSummary:
    """
    Attributes:
        tx_hash (str | Unset):
        block_number (int | Unset):
        slot (int | Unset):
        output_addresses (list[str] | Unset):
        total_output (int | Unset):
        fee (int | Unset):
    """

    tx_hash: str | Unset = UNSET
    block_number: int | Unset = UNSET
    slot: int | Unset = UNSET
    output_addresses: list[str] | Unset = UNSET
    total_output: int | Unset = UNSET
    fee: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_hash = self.tx_hash

        block_number = self.block_number

        slot = self.slot

        output_addresses: list[str] | Unset = UNSET
        if not isinstance(self.output_addresses, Unset):
            output_addresses = self.output_addresses

        total_output = self.total_output

        fee = self.fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if slot is not UNSET:
            field_dict["slot"] = slot
        if output_addresses is not UNSET:
            field_dict["output_addresses"] = output_addresses
        if total_output is not UNSET:
            field_dict["total_output"] = total_output
        if fee is not UNSET:
            field_dict["fee"] = fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tx_hash = d.pop("tx_hash", UNSET)

        block_number = d.pop("block_number", UNSET)

        slot = d.pop("slot", UNSET)

        output_addresses = cast(list[str], d.pop("output_addresses", UNSET))

        total_output = d.pop("total_output", UNSET)

        fee = d.pop("fee", UNSET)

        transaction_summary = cls(
            tx_hash=tx_hash,
            block_number=block_number,
            slot=slot,
            output_addresses=output_addresses,
            total_output=total_output,
            fee=fee,
        )

        transaction_summary.additional_properties = d
        return transaction_summary

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
