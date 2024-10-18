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

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtxoKey")


@_attrs_define
class UtxoKey:
    """
    Attributes:
        tx_hash (Union[Unset, str]):
        output_index (Union[Unset, int]):
    """

    tx_hash: Union[Unset, str] = UNSET
    output_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tx_hash = self.tx_hash

        output_index = self.output_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if output_index is not UNSET:
            field_dict["output_index"] = output_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tx_hash = d.pop("tx_hash", UNSET)

        output_index = d.pop("output_index", UNSET)

        utxo_key = cls(
            tx_hash=tx_hash,
            output_index=output_index,
        )

        utxo_key.additional_properties = d
        return utxo_key

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
