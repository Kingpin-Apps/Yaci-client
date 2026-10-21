from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TxMetadataLabelCBORDto")


@_attrs_define
class TxMetadataLabelCBORDto:
    """
    Attributes:
        block_number (int | Unset):
        block_time (int | Unset):
        label (str | Unset):
        metadata (str | Unset):
        slot (int | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    label: str | Unset = UNSET
    metadata: str | Unset = UNSET
    slot: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        label = self.label

        metadata = self.metadata

        slot = self.slot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if label is not UNSET:
            field_dict["label"] = label
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if slot is not UNSET:
            field_dict["slot"] = slot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        label = d.pop("label", UNSET)

        metadata = d.pop("metadata", UNSET)

        slot = d.pop("slot", UNSET)

        tx_metadata_label_cbor_dto = cls(
            block_number=block_number,
            block_time=block_time,
            label=label,
            metadata=metadata,
            slot=slot,
        )

        tx_metadata_label_cbor_dto.additional_properties = d
        return tx_metadata_label_cbor_dto

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
