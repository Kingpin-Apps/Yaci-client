from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stake_registration_detail_type import StakeRegistrationDetailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StakeRegistrationDetail")


@_attrs_define
class StakeRegistrationDetail:
    """
    Attributes:
        block_number (int | Unset):
        block_time (int | Unset):
        credential (str | Unset):
        address (str | Unset):
        tx_hash (str | Unset):
        cert_index (int | Unset):
        type_ (StakeRegistrationDetailType | Unset):
        epoch (int | Unset):
        slot (int | Unset):
        block_hash (str | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    credential: str | Unset = UNSET
    address: str | Unset = UNSET
    tx_hash: str | Unset = UNSET
    cert_index: int | Unset = UNSET
    type_: StakeRegistrationDetailType | Unset = UNSET
    epoch: int | Unset = UNSET
    slot: int | Unset = UNSET
    block_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        credential = self.credential

        address = self.address

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        epoch = self.epoch

        slot = self.slot

        block_hash = self.block_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if credential is not UNSET:
            field_dict["credential"] = credential
        if address is not UNSET:
            field_dict["address"] = address
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if cert_index is not UNSET:
            field_dict["cert_index"] = cert_index
        if type_ is not UNSET:
            field_dict["type"] = type_
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if slot is not UNSET:
            field_dict["slot"] = slot
        if block_hash is not UNSET:
            field_dict["block_hash"] = block_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        credential = d.pop("credential", UNSET)

        address = d.pop("address", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: StakeRegistrationDetailType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = StakeRegistrationDetailType(_type_)

        epoch = d.pop("epoch", UNSET)

        slot = d.pop("slot", UNSET)

        block_hash = d.pop("block_hash", UNSET)

        stake_registration_detail = cls(
            block_number=block_number,
            block_time=block_time,
            credential=credential,
            address=address,
            tx_hash=tx_hash,
            cert_index=cert_index,
            type_=type_,
            epoch=epoch,
            slot=slot,
            block_hash=block_hash,
        )

        stake_registration_detail.additional_properties = d
        return stake_registration_detail

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
