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

T = TypeVar("T", bound="TxRedeemerDto")


@_attrs_define
class TxRedeemerDto:
    """
    Attributes:
        tx_index (Union[Unset, int]):
        purpose (Union[Unset, str]):
        script_hash (Union[Unset, str]):
        datum_hash (Union[Unset, str]):
        redeemer_data_hash (Union[Unset, str]):
        unit_mem (Union[Unset, str]):
        unit_steps (Union[Unset, str]):
    """

    tx_index: Union[Unset, int] = UNSET
    purpose: Union[Unset, str] = UNSET
    script_hash: Union[Unset, str] = UNSET
    datum_hash: Union[Unset, str] = UNSET
    redeemer_data_hash: Union[Unset, str] = UNSET
    unit_mem: Union[Unset, str] = UNSET
    unit_steps: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tx_index = self.tx_index

        purpose = self.purpose

        script_hash = self.script_hash

        datum_hash = self.datum_hash

        redeemer_data_hash = self.redeemer_data_hash

        unit_mem = self.unit_mem

        unit_steps = self.unit_steps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_index is not UNSET:
            field_dict["tx_index"] = tx_index
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if script_hash is not UNSET:
            field_dict["script_hash"] = script_hash
        if datum_hash is not UNSET:
            field_dict["datum_hash"] = datum_hash
        if redeemer_data_hash is not UNSET:
            field_dict["redeemer_data_hash"] = redeemer_data_hash
        if unit_mem is not UNSET:
            field_dict["unit_mem"] = unit_mem
        if unit_steps is not UNSET:
            field_dict["unit_steps"] = unit_steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tx_index = d.pop("tx_index", UNSET)

        purpose = d.pop("purpose", UNSET)

        script_hash = d.pop("script_hash", UNSET)

        datum_hash = d.pop("datum_hash", UNSET)

        redeemer_data_hash = d.pop("redeemer_data_hash", UNSET)

        unit_mem = d.pop("unit_mem", UNSET)

        unit_steps = d.pop("unit_steps", UNSET)

        tx_redeemer_dto = cls(
            tx_index=tx_index,
            purpose=purpose,
            script_hash=script_hash,
            datum_hash=datum_hash,
            redeemer_data_hash=redeemer_data_hash,
            unit_mem=unit_mem,
            unit_steps=unit_steps,
        )

        tx_redeemer_dto.additional_properties = d
        return tx_redeemer_dto

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
