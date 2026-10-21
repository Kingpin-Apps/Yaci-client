from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolRetirement")


@_attrs_define
class PoolRetirement:
    """
    Attributes:
        block_number (int | Unset):
        block_time (int | Unset):
        tx_hash (str | Unset):
        cert_index (int | Unset):
        pool_id (str | Unset):
        retirement_epoch (int | Unset):
        epoch (int | Unset):
        slot (int | Unset):
        block_hash (str | Unset):
        pool_id_bech32 (str | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    tx_hash: str | Unset = UNSET
    cert_index: int | Unset = UNSET
    pool_id: str | Unset = UNSET
    retirement_epoch: int | Unset = UNSET
    epoch: int | Unset = UNSET
    slot: int | Unset = UNSET
    block_hash: str | Unset = UNSET
    pool_id_bech32: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        pool_id = self.pool_id

        retirement_epoch = self.retirement_epoch

        epoch = self.epoch

        slot = self.slot

        block_hash = self.block_hash

        pool_id_bech32 = self.pool_id_bech32

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if cert_index is not UNSET:
            field_dict["cert_index"] = cert_index
        if pool_id is not UNSET:
            field_dict["pool_id"] = pool_id
        if retirement_epoch is not UNSET:
            field_dict["retirement_epoch"] = retirement_epoch
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if slot is not UNSET:
            field_dict["slot"] = slot
        if block_hash is not UNSET:
            field_dict["block_hash"] = block_hash
        if pool_id_bech32 is not UNSET:
            field_dict["pool_id_bech32"] = pool_id_bech32

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        pool_id = d.pop("pool_id", UNSET)

        retirement_epoch = d.pop("retirement_epoch", UNSET)

        epoch = d.pop("epoch", UNSET)

        slot = d.pop("slot", UNSET)

        block_hash = d.pop("block_hash", UNSET)

        pool_id_bech32 = d.pop("pool_id_bech32", UNSET)

        pool_retirement = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            cert_index=cert_index,
            pool_id=pool_id,
            retirement_epoch=retirement_epoch,
            epoch=epoch,
            slot=slot,
            block_hash=block_hash,
            pool_id_bech32=pool_id_bech32,
        )

        pool_retirement.additional_properties = d
        return pool_retirement

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
