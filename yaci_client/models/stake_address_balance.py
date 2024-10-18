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

T = TypeVar("T", bound="StakeAddressBalance")


@_attrs_define
class StakeAddressBalance:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        address (Union[Unset, str]):
        slot (Union[Unset, int]):
        quantity (Union[Unset, int]):
        epoch (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    address: Union[Unset, str] = UNSET
    slot: Union[Unset, int] = UNSET
    quantity: Union[Unset, int] = UNSET
    epoch: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        address = self.address

        slot = self.slot

        quantity = self.quantity

        epoch = self.epoch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if address is not UNSET:
            field_dict["address"] = address
        if slot is not UNSET:
            field_dict["slot"] = slot
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if epoch is not UNSET:
            field_dict["epoch"] = epoch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        address = d.pop("address", UNSET)

        slot = d.pop("slot", UNSET)

        quantity = d.pop("quantity", UNSET)

        epoch = d.pop("epoch", UNSET)

        stake_address_balance = cls(
            block_number=block_number,
            block_time=block_time,
            address=address,
            slot=slot,
            quantity=quantity,
            epoch=epoch,
        )

        stake_address_balance.additional_properties = d
        return stake_address_balance

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
