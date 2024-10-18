from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="ScriptJsonDto")


@_attrs_define
class ScriptJsonDto:
    """
    Attributes:
        json (Union[Unset, JsonNode]):
    """

    json: Union[Unset, "JsonNode"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json, Unset):
            json = self.json.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if json is not UNSET:
            field_dict["json"] = json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.json_node import JsonNode

        d = src_dict.copy()
        _json = d.pop("json", UNSET)
        json: Union[Unset, JsonNode]
        if isinstance(_json, Unset):
            json = UNSET
        else:
            json = JsonNode.from_dict(_json)

        script_json_dto = cls(
            json=json,
        )

        script_json_dto.additional_properties = d
        return script_json_dto

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
