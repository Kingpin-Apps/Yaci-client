from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FingerprintSupply")


@_attrs_define
class FingerprintSupply:
    """
    Attributes:
        fingerprint (str | Unset):
        supply (int | Unset):
    """

    fingerprint: str | Unset = UNSET
    supply: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fingerprint = self.fingerprint

        supply = self.supply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if supply is not UNSET:
            field_dict["supply"] = supply

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fingerprint = d.pop("fingerprint", UNSET)

        supply = d.pop("supply", UNSET)

        fingerprint_supply = cls(
            fingerprint=fingerprint,
            supply=supply,
        )

        fingerprint_supply.additional_properties = d
        return fingerprint_supply

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
