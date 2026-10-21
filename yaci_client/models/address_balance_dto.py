from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amt import Amt


T = TypeVar("T", bound="AddressBalanceDto")


@_attrs_define
class AddressBalanceDto:
    """
    Attributes:
        block_number (int | Unset):
        block_time (int | Unset):
        address (str | Unset):
        amounts (list[Amt] | Unset):
        slot (int | Unset):
        last_balance_calculation_block (int | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    address: str | Unset = UNSET
    amounts: list[Amt] | Unset = UNSET
    slot: int | Unset = UNSET
    last_balance_calculation_block: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        address = self.address

        amounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = []
            for amounts_item_data in self.amounts:
                amounts_item = amounts_item_data.to_dict()
                amounts.append(amounts_item)

        slot = self.slot

        last_balance_calculation_block = self.last_balance_calculation_block

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if address is not UNSET:
            field_dict["address"] = address
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if slot is not UNSET:
            field_dict["slot"] = slot
        if last_balance_calculation_block is not UNSET:
            field_dict["last_balance_calculation_block"] = last_balance_calculation_block

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amt import Amt

        d = dict(src_dict)
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        address = d.pop("address", UNSET)

        _amounts = d.pop("amounts", UNSET)
        amounts: list[Amt] | Unset = UNSET
        if _amounts is not UNSET:
            amounts = []
            for amounts_item_data in _amounts:
                amounts_item = Amt.from_dict(amounts_item_data)

                amounts.append(amounts_item)

        slot = d.pop("slot", UNSET)

        last_balance_calculation_block = d.pop("last_balance_calculation_block", UNSET)

        address_balance_dto = cls(
            block_number=block_number,
            block_time=block_time,
            address=address,
            amounts=amounts,
            slot=slot,
            last_balance_calculation_block=last_balance_calculation_block,
        )

        address_balance_dto.additional_properties = d
        return address_balance_dto

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
