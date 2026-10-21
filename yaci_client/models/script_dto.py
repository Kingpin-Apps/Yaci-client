from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.script_dto_type import ScriptDtoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScriptDto")


@_attrs_define
class ScriptDto:
    """
    Attributes:
        script_hash (str | Unset):
        type_ (ScriptDtoType | Unset):
        serialised_size (int | Unset):
    """

    script_hash: str | Unset = UNSET
    type_: ScriptDtoType | Unset = UNSET
    serialised_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        script_hash = self.script_hash

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        serialised_size = self.serialised_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if script_hash is not UNSET:
            field_dict["script_hash"] = script_hash
        if type_ is not UNSET:
            field_dict["type"] = type_
        if serialised_size is not UNSET:
            field_dict["serialised_size"] = serialised_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        script_hash = d.pop("script_hash", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ScriptDtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ScriptDtoType(_type_)

        serialised_size = d.pop("serialised_size", UNSET)

        script_dto = cls(
            script_hash=script_hash,
            type_=type_,
            serialised_size=serialised_size,
        )

        script_dto.additional_properties = d
        return script_dto

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
