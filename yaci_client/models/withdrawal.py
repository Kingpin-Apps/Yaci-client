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

T = TypeVar("T", bound="Withdrawal")


@_attrs_define
class Withdrawal:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        address (Union[Unset, str]):
        tx_hash (Union[Unset, str]):
        amount (Union[Unset, int]):
        epoch (Union[Unset, int]):
        slot (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    address: Union[Unset, str] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    epoch: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        address = self.address

        tx_hash = self.tx_hash

        amount = self.amount

        epoch = self.epoch

        slot = self.slot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if address is not UNSET:
            field_dict["address"] = address
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if amount is not UNSET:
            field_dict["amount"] = amount
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if slot is not UNSET:
            field_dict["slot"] = slot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        address = d.pop("address", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        amount = d.pop("amount", UNSET)

        epoch = d.pop("epoch", UNSET)

        slot = d.pop("slot", UNSET)

        withdrawal = cls(
            block_number=block_number,
            block_time=block_time,
            address=address,
            tx_hash=tx_hash,
            amount=amount,
            epoch=epoch,
            slot=slot,
        )

        withdrawal.additional_properties = d
        return withdrawal

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
