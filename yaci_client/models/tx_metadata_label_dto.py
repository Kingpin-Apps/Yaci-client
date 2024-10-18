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


T = TypeVar("T", bound="TxMetadataLabelDto")


@_attrs_define
class TxMetadataLabelDto:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        label (Union[Unset, str]):
        body (Union[Unset, JsonNode]):
        json_metadata (Union[Unset, JsonNode]):
        slot (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    body: Union[Unset, "JsonNode"] = UNSET
    json_metadata: Union[Unset, "JsonNode"] = UNSET
    slot: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        block_number = self.block_number

        block_time = self.block_time

        label = self.label

        body: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        json_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json_metadata, Unset):
            json_metadata = self.json_metadata.to_dict()

        slot = self.slot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if label is not UNSET:
            field_dict["label"] = label
        if body is not UNSET:
            field_dict["body"] = body
        if json_metadata is not UNSET:
            field_dict["json_metadata"] = json_metadata
        if slot is not UNSET:
            field_dict["slot"] = slot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.json_node import JsonNode

        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        label = d.pop("label", UNSET)

        _body = d.pop("body", UNSET)
        body: Union[Unset, JsonNode]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = JsonNode.from_dict(_body)

        _json_metadata = d.pop("json_metadata", UNSET)
        json_metadata: Union[Unset, JsonNode]
        if isinstance(_json_metadata, Unset):
            json_metadata = UNSET
        else:
            json_metadata = JsonNode.from_dict(_json_metadata)

        slot = d.pop("slot", UNSET)

        tx_metadata_label_dto = cls(
            block_number=block_number,
            block_time=block_time,
            label=label,
            body=body,
            json_metadata=json_metadata,
            slot=slot,
        )

        tx_metadata_label_dto.additional_properties = d
        return tx_metadata_label_dto

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
