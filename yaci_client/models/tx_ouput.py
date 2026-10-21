from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amt import Amt


T = TypeVar("T", bound="TxOuput")


@_attrs_define
class TxOuput:
    """
    Attributes:
        address (str | Unset):
        amounts (list[Amt] | Unset):
        data_hash (str | Unset):
        inline_datum (str | Unset):
        reference_script_hash (str | Unset):
    """

    address: str | Unset = UNSET
    amounts: list[Amt] | Unset = UNSET
    data_hash: str | Unset = UNSET
    inline_datum: str | Unset = UNSET
    reference_script_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        amounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = []
            for amounts_item_data in self.amounts:
                amounts_item = amounts_item_data.to_dict()
                amounts.append(amounts_item)

        data_hash = self.data_hash

        inline_datum = self.inline_datum

        reference_script_hash = self.reference_script_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if data_hash is not UNSET:
            field_dict["dataHash"] = data_hash
        if inline_datum is not UNSET:
            field_dict["inlineDatum"] = inline_datum
        if reference_script_hash is not UNSET:
            field_dict["referenceScriptHash"] = reference_script_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amt import Amt

        d = dict(src_dict)
        address = d.pop("address", UNSET)

        _amounts = d.pop("amounts", UNSET)
        amounts: list[Amt] | Unset = UNSET
        if _amounts is not UNSET:
            amounts = []
            for amounts_item_data in _amounts:
                amounts_item = Amt.from_dict(amounts_item_data)

                amounts.append(amounts_item)

        data_hash = d.pop("dataHash", UNSET)

        inline_datum = d.pop("inlineDatum", UNSET)

        reference_script_hash = d.pop("referenceScriptHash", UNSET)

        tx_ouput = cls(
            address=address,
            amounts=amounts,
            data_hash=data_hash,
            inline_datum=inline_datum,
            reference_script_hash=reference_script_hash,
        )

        tx_ouput.additional_properties = d
        return tx_ouput

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
