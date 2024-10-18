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

T = TypeVar("T", bound="Epoch")


@_attrs_define
class Epoch:
    """
    Attributes:
        number (Union[Unset, int]):
        block_count (Union[Unset, int]):
        transaction_count (Union[Unset, int]):
        total_output (Union[Unset, int]):
        total_fees (Union[Unset, int]):
        start_time (Union[Unset, int]):
        end_time (Union[Unset, int]):
        max_slot (Union[Unset, int]):
    """

    number: Union[Unset, int] = UNSET
    block_count: Union[Unset, int] = UNSET
    transaction_count: Union[Unset, int] = UNSET
    total_output: Union[Unset, int] = UNSET
    total_fees: Union[Unset, int] = UNSET
    start_time: Union[Unset, int] = UNSET
    end_time: Union[Unset, int] = UNSET
    max_slot: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number

        block_count = self.block_count

        transaction_count = self.transaction_count

        total_output = self.total_output

        total_fees = self.total_fees

        start_time = self.start_time

        end_time = self.end_time

        max_slot = self.max_slot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if block_count is not UNSET:
            field_dict["block_count"] = block_count
        if transaction_count is not UNSET:
            field_dict["transaction_count"] = transaction_count
        if total_output is not UNSET:
            field_dict["total_output"] = total_output
        if total_fees is not UNSET:
            field_dict["total_fees"] = total_fees
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if max_slot is not UNSET:
            field_dict["max_slot"] = max_slot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        block_count = d.pop("block_count", UNSET)

        transaction_count = d.pop("transaction_count", UNSET)

        total_output = d.pop("total_output", UNSET)

        total_fees = d.pop("total_fees", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        max_slot = d.pop("max_slot", UNSET)

        epoch = cls(
            number=number,
            block_count=block_count,
            transaction_count=transaction_count,
            total_output=total_output,
            total_fees=total_fees,
            start_time=start_time,
            end_time=end_time,
            max_slot=max_slot,
        )

        epoch.additional_properties = d
        return epoch

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
