from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EpochContent")


@_attrs_define
class EpochContent:
    """
    Attributes:
        epoch (Union[Unset, int]):
        first_block_time (Union[Unset, int]):
        last_block_time (Union[Unset, int]):
        block_count (Union[Unset, int]):
        tx_count (Union[Unset, int]):
        output (Union[Unset, str]):
        fees (Union[Unset, str]):
    """

    epoch: Unset | int = UNSET
    first_block_time: Unset | int = UNSET
    last_block_time: Unset | int = UNSET
    block_count: Unset | int = UNSET
    tx_count: Unset | int = UNSET
    output: Unset | str = UNSET
    fees: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        epoch = self.epoch

        first_block_time = self.first_block_time

        last_block_time = self.last_block_time

        block_count = self.block_count

        tx_count = self.tx_count

        output = self.output

        fees = self.fees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if first_block_time is not UNSET:
            field_dict["first_block_time"] = first_block_time
        if last_block_time is not UNSET:
            field_dict["last_block_time"] = last_block_time
        if block_count is not UNSET:
            field_dict["block_count"] = block_count
        if tx_count is not UNSET:
            field_dict["tx_count"] = tx_count
        if output is not UNSET:
            field_dict["output"] = output
        if fees is not UNSET:
            field_dict["fees"] = fees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        epoch = d.pop("epoch", UNSET)

        first_block_time = d.pop("first_block_time", UNSET)

        last_block_time = d.pop("last_block_time", UNSET)

        block_count = d.pop("block_count", UNSET)

        tx_count = d.pop("tx_count", UNSET)

        output = d.pop("output", UNSET)

        fees = d.pop("fees", UNSET)

        epoch_content = cls(
            epoch=epoch,
            first_block_time=first_block_time,
            last_block_time=last_block_time,
            block_count=block_count,
            tx_count=tx_count,
            output=output,
            fees=fees,
        )

        epoch_content.additional_properties = d
        return epoch_content

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
