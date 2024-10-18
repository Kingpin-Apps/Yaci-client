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

from ..models.script_dto_type import ScriptDtoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScriptDto")


@_attrs_define
class ScriptDto:
    """
    Attributes:
        script_hash (Union[Unset, str]):
        type (Union[Unset, ScriptDtoType]):
        serialised_size (Union[Unset, int]):
    """

    script_hash: Union[Unset, str] = UNSET
    type: Union[Unset, ScriptDtoType] = UNSET
    serialised_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        script_hash = self.script_hash

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        serialised_size = self.serialised_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if script_hash is not UNSET:
            field_dict["script_hash"] = script_hash
        if type is not UNSET:
            field_dict["type"] = type
        if serialised_size is not UNSET:
            field_dict["serialised_size"] = serialised_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        script_hash = d.pop("script_hash", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ScriptDtoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ScriptDtoType(_type)

        serialised_size = d.pop("serialised_size", UNSET)

        script_dto = cls(
            script_hash=script_hash,
            type=type,
            serialised_size=serialised_size,
        )

        script_dto.additional_properties = d
        return script_dto

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
