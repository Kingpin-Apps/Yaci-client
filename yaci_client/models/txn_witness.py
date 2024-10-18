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

from ..models.txn_witness_type import TxnWitnessType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="TxnWitness")


@_attrs_define
class TxnWitness:
    """
    Attributes:
        tx_hash (Union[Unset, str]):
        index (Union[Unset, int]):
        pub_key (Union[Unset, str]):
        signature (Union[Unset, str]):
        pub_keyhash (Union[Unset, str]):
        type (Union[Unset, TxnWitnessType]):
        additional_data (Union[Unset, JsonNode]):
    """

    tx_hash: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    pub_key: Union[Unset, str] = UNSET
    signature: Union[Unset, str] = UNSET
    pub_keyhash: Union[Unset, str] = UNSET
    type: Union[Unset, TxnWitnessType] = UNSET
    additional_data: Union[Unset, "JsonNode"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        tx_hash = self.tx_hash

        index = self.index

        pub_key = self.pub_key

        signature = self.signature

        pub_keyhash = self.pub_keyhash

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        additional_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        field_dict: Dict[str, Any] = {}
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
        if type is not UNSET:
            field_dict["type"] = type
        if additional_data is not UNSET:
            field_dict["additional_data"] = additional_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.json_node import JsonNode

        d = src_dict.copy()
        tx_hash = d.pop("tx_hash", UNSET)

        index = d.pop("index", UNSET)

        pub_key = d.pop("pub_key", UNSET)

        signature = d.pop("signature", UNSET)

        pub_keyhash = d.pop("pub_keyhash", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TxnWitnessType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TxnWitnessType(_type)

        _additional_data = d.pop("additional_data", UNSET)
        additional_data: Union[Unset, JsonNode]
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
            type=type,
            additional_data=additional_data,
        )

        txn_witness.additional_properties = d
        return txn_witness

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
