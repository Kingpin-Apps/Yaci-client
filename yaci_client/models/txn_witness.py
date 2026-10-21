from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.txn_witness_type import TxnWitnessType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="TxnWitness")


@_attrs_define
class TxnWitness:
    """
    Attributes:
        tx_hash (str | Unset):
        index (int | Unset):
        pub_key (str | Unset):
        signature (str | Unset):
        pub_keyhash (str | Unset):
        type_ (TxnWitnessType | Unset):
        additional_data (JsonNode | Unset):
    """

    tx_hash: str | Unset = UNSET
    index: int | Unset = UNSET
    pub_key: str | Unset = UNSET
    signature: str | Unset = UNSET
    pub_keyhash: str | Unset = UNSET
    type_: TxnWitnessType | Unset = UNSET
    additional_data: JsonNode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_hash = self.tx_hash

        index = self.index

        pub_key = self.pub_key

        signature = self.signature

        pub_keyhash = self.pub_keyhash

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        additional_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if index is not UNSET:
            field_dict["index"] = index
        if pub_key is not UNSET:
            field_dict["pub_key"] = pub_key
        if signature is not UNSET:
            field_dict["signature"] = signature
        if pub_keyhash is not UNSET:
            field_dict["pub_keyhash"] = pub_keyhash
        if type_ is not UNSET:
            field_dict["type"] = type_
        if additional_data is not UNSET:
            field_dict["additional_data"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_node import JsonNode

        d = dict(src_dict)
        tx_hash = d.pop("tx_hash", UNSET)

        index = d.pop("index", UNSET)

        pub_key = d.pop("pub_key", UNSET)

        signature = d.pop("signature", UNSET)

        pub_keyhash = d.pop("pub_keyhash", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: TxnWitnessType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TxnWitnessType(_type_)

        _additional_data = d.pop("additional_data", UNSET)
        additional_data: JsonNode | Unset
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = JsonNode.from_dict(_additional_data)

        txn_witness = cls(
            tx_hash=tx_hash,
            index=index,
            pub_key=pub_key,
            signature=signature,
            pub_keyhash=pub_keyhash,
            type_=type_,
            additional_data=additional_data,
        )

        txn_witness.additional_properties = d
        return txn_witness

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
