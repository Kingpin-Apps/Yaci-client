from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionSummary")


@_attrs_define
class TransactionSummary:
    """
    Attributes:
        tx_hash (Union[Unset, str]):
        block_number (Union[Unset, int]):
        slot (Union[Unset, int]):
        output_addresses (Union[Unset, List[str]]):
        total_output (Union[Unset, int]):
        fee (Union[Unset, int]):
    """

    tx_hash: Union[Unset, str] = UNSET
    block_number: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    output_addresses: Union[Unset, List[str]] = UNSET
    total_output: Union[Unset, int] = UNSET
    fee: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tx_hash = self.tx_hash

        block_number = self.block_number

        slot = self.slot

        output_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_addresses, Unset):
            output_addresses = self.output_addresses

        total_output = self.total_output

        fee = self.fee

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if slot is not UNSET:
            field_dict["slot"] = slot
        if output_addresses is not UNSET:
            field_dict["output_addresses"] = output_addresses
        if total_output is not UNSET:
            field_dict["total_output"] = total_output
        if fee is not UNSET:
            field_dict["fee"] = fee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tx_hash = d.pop("tx_hash", UNSET)

        block_number = d.pop("block_number", UNSET)

        slot = d.pop("slot", UNSET)

        output_addresses = cast(List[str], d.pop("output_addresses", UNSET))

        total_output = d.pop("total_output", UNSET)

        fee = d.pop("fee", UNSET)

        transaction_summary = cls(
            tx_hash=tx_hash,
            block_number=block_number,
            slot=slot,
            output_addresses=output_addresses,
            total_output=total_output,
            fee=fee,
        )

        transaction_summary.additional_properties = d
        return transaction_summary

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
