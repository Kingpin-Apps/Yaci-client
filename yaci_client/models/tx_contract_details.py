from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        tx_hash (str | Unset):
        script_hash (str | Unset):
        script_content (str | Unset):
        type_ (TxContractDetailsType | Unset):
        redeemer (Redeemer | Unset):
        datum (str | Unset):
        datum_hash (str | Unset):
    """

    tx_hash: str | Unset = UNSET
    script_hash: str | Unset = UNSET
    script_content: str | Unset = UNSET
    type_: TxContractDetailsType | Unset = UNSET
    redeemer: Redeemer | Unset = UNSET
    datum: str | Unset = UNSET
    datum_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_hash = self.tx_hash

        script_hash = self.script_hash

        script_content = self.script_content

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        redeemer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redeemer, Unset):
            redeemer = self.redeemer.to_dict()

        datum = self.datum

        datum_hash = self.datum_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if script_hash is not UNSET:
            field_dict["script_hash"] = script_hash
        if script_content is not UNSET:
            field_dict["script_content"] = script_content
        if type_ is not UNSET:
            field_dict["type"] = type_
        if redeemer is not UNSET:
            field_dict["redeemer"] = redeemer
        if datum is not UNSET:
            field_dict["datum"] = datum
        if datum_hash is not UNSET:
            field_dict["datum_hash"] = datum_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.redeemer import Redeemer

        d = dict(src_dict)
        tx_hash = d.pop("tx_hash", UNSET)

        script_hash = d.pop("script_hash", UNSET)

        script_content = d.pop("script_content", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: TxContractDetailsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TxContractDetailsType(_type_)

        _redeemer = d.pop("redeemer", UNSET)
        redeemer: Redeemer | Unset
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
            type_=type_,
            redeemer=redeemer,
            datum=datum,
            datum_hash=datum_hash,
        )

        tx_contract_details.additional_properties = d
        return tx_contract_details

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
