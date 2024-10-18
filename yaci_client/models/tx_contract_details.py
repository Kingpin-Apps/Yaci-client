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

from ..models.tx_contract_details_type import TxContractDetailsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redeemer import Redeemer


T = TypeVar("T", bound="TxContractDetails")


@_attrs_define
class TxContractDetails:
    """
    Attributes:
        tx_hash (Union[Unset, str]):
        script_hash (Union[Unset, str]):
        script_content (Union[Unset, str]):
        type (Union[Unset, TxContractDetailsType]):
        redeemer (Union[Unset, Redeemer]):
        datum (Union[Unset, str]):
        datum_hash (Union[Unset, str]):
    """

    tx_hash: Union[Unset, str] = UNSET
    script_hash: Union[Unset, str] = UNSET
    script_content: Union[Unset, str] = UNSET
    type: Union[Unset, TxContractDetailsType] = UNSET
    redeemer: Union[Unset, "Redeemer"] = UNSET
    datum: Union[Unset, str] = UNSET
    datum_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        tx_hash = self.tx_hash

        script_hash = self.script_hash

        script_content = self.script_content

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        redeemer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.redeemer, Unset):
            redeemer = self.redeemer.to_dict()

        datum = self.datum

        datum_hash = self.datum_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if script_hash is not UNSET:
            field_dict["script_hash"] = script_hash
        if script_content is not UNSET:
            field_dict["script_content"] = script_content
        if type is not UNSET:
            field_dict["type"] = type
        if redeemer is not UNSET:
            field_dict["redeemer"] = redeemer
        if datum is not UNSET:
            field_dict["datum"] = datum
        if datum_hash is not UNSET:
            field_dict["datum_hash"] = datum_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.redeemer import Redeemer

        d = src_dict.copy()
        tx_hash = d.pop("tx_hash", UNSET)

        script_hash = d.pop("script_hash", UNSET)

        script_content = d.pop("script_content", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TxContractDetailsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TxContractDetailsType(_type)

        _redeemer = d.pop("redeemer", UNSET)
        redeemer: Union[Unset, Redeemer]
        if isinstance(_redeemer, Unset):
            redeemer = UNSET
        else:
            redeemer = Redeemer.from_dict(_redeemer)

        datum = d.pop("datum", UNSET)

        datum_hash = d.pop("datum_hash", UNSET)

        tx_contract_details = cls(
            tx_hash=tx_hash,
            script_hash=script_hash,
            script_content=script_content,
            type=type,
            redeemer=redeemer,
            datum=datum,
            datum_hash=datum_hash,
        )

        tx_contract_details.additional_properties = d
        return tx_contract_details

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
