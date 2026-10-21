from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolBlock")


@_attrs_define
class PoolBlock:
    """
    Attributes:
        hash_ (str | Unset):
        number (int | Unset):
        epoch (int | Unset):
        pool_id (str | Unset):
    """

    hash_: str | Unset = UNSET
    number: int | Unset = UNSET
    epoch: int | Unset = UNSET
    pool_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        number = self.number

        epoch = self.epoch

        pool_id = self.pool_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if number is not UNSET:
            field_dict["number"] = number
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if pool_id is not UNSET:
            field_dict["pool_id"] = pool_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash", UNSET)

        number = d.pop("number", UNSET)

        epoch = d.pop("epoch", UNSET)

        pool_id = d.pop("pool_id", UNSET)

        pool_block = cls(
            hash_=hash_,
            number=number,
            epoch=epoch,
            pool_id=pool_id,
        )

        pool_block.additional_properties = d
        return pool_block

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
