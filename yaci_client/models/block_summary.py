from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockSummary")


@_attrs_define
class BlockSummary:
    """
    Attributes:
        time (Union[Unset, int]):
        number (Union[Unset, int]):
        slot (Union[Unset, int]):
        epoch (Union[Unset, int]):
        era (Union[Unset, int]):
        output (Union[Unset, int]):
        fees (Union[Unset, int]):
        slot_leader (Union[Unset, str]):
        size (Union[Unset, int]):
        tx_count (Union[Unset, int]):
        issuer_vkey (Union[Unset, str]):
    """

    time: Unset | int = UNSET
    number: Unset | int = UNSET
    slot: Unset | int = UNSET
    epoch: Unset | int = UNSET
    era: Unset | int = UNSET
    output: Unset | int = UNSET
    fees: Unset | int = UNSET
    slot_leader: Unset | str = UNSET
    size: Unset | int = UNSET
    tx_count: Unset | int = UNSET
    issuer_vkey: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        number = self.number

        slot = self.slot

        epoch = self.epoch

        era = self.era

        output = self.output

        fees = self.fees

        slot_leader = self.slot_leader

        size = self.size

        tx_count = self.tx_count

        issuer_vkey = self.issuer_vkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if number is not UNSET:
            field_dict["number"] = number
        if slot is not UNSET:
            field_dict["slot"] = slot
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if era is not UNSET:
            field_dict["era"] = era
        if output is not UNSET:
            field_dict["output"] = output
        if fees is not UNSET:
            field_dict["fees"] = fees
        if slot_leader is not UNSET:
            field_dict["slot_leader"] = slot_leader
        if size is not UNSET:
            field_dict["size"] = size
        if tx_count is not UNSET:
            field_dict["tx_count"] = tx_count
        if issuer_vkey is not UNSET:
            field_dict["issuer_vkey"] = issuer_vkey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        number = d.pop("number", UNSET)

        slot = d.pop("slot", UNSET)

        epoch = d.pop("epoch", UNSET)

        era = d.pop("era", UNSET)

        output = d.pop("output", UNSET)

        fees = d.pop("fees", UNSET)

        slot_leader = d.pop("slot_leader", UNSET)

        size = d.pop("size", UNSET)

        tx_count = d.pop("tx_count", UNSET)

        issuer_vkey = d.pop("issuer_vkey", UNSET)

        block_summary = cls(
            time=time,
            number=number,
            slot=slot,
            epoch=epoch,
            era=era,
            output=output,
            fees=fees,
            slot_leader=slot_leader,
            size=size,
            tx_count=tx_count,
            issuer_vkey=issuer_vkey,
        )

        block_summary.additional_properties = d
        return block_summary

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
