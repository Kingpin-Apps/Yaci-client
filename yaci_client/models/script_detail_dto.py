from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.script_detail_dto_script_type import ScriptDetailDtoScriptType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="ScriptDetailDto")


@_attrs_define
class ScriptDetailDto:
    """
    Attributes:
        script_hash (str | Unset):
        script_type (ScriptDetailDtoScriptType | Unset):
        content (JsonNode | Unset):
    """

    script_hash: str | Unset = UNSET
    script_type: ScriptDetailDtoScriptType | Unset = UNSET
    content: JsonNode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        script_hash = self.script_hash

        script_type: str | Unset = UNSET
        if not isinstance(self.script_type, Unset):
            script_type = self.script_type.value

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if script_hash is not UNSET:
            field_dict["script_hash"] = script_hash
        if script_type is not UNSET:
            field_dict["script_type"] = script_type
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_node import JsonNode

        d = dict(src_dict)
        script_hash = d.pop("script_hash", UNSET)

        _script_type = d.pop("script_type", UNSET)
        script_type: ScriptDetailDtoScriptType | Unset
        if isinstance(_script_type, Unset):
            script_type = UNSET
        else:
            script_type = ScriptDetailDtoScriptType(_script_type)

        _content = d.pop("content", UNSET)
        content: JsonNode | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = JsonNode.from_dict(_content)

        script_detail_dto = cls(
            script_hash=script_hash,
            script_type=script_type,
            content=content,
        )

        script_detail_dto.additional_properties = d
        return script_detail_dto

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
