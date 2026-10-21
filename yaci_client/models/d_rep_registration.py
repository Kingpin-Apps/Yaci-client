from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.d_rep_registration_cred_type import DRepRegistrationCredType
from ..models.d_rep_registration_type import DRepRegistrationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DRepRegistration")


@_attrs_define
class DRepRegistration:
    """
    Attributes:
        block_number (int | Unset):
        block_time (int | Unset):
        tx_hash (str | Unset):
        cert_index (int | Unset):
        type_ (DRepRegistrationType | Unset):
        slot (int | Unset):
        deposit (int | Unset):
        drep_hash (str | Unset):
        drep_id (str | Unset):
        anchor_url (str | Unset):
        anchor_hash (str | Unset):
        cred_type (DRepRegistrationCredType | Unset):
        epoch (int | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    tx_hash: str | Unset = UNSET
    cert_index: int | Unset = UNSET
    type_: DRepRegistrationType | Unset = UNSET
    slot: int | Unset = UNSET
    deposit: int | Unset = UNSET
    drep_hash: str | Unset = UNSET
    drep_id: str | Unset = UNSET
    anchor_url: str | Unset = UNSET
    anchor_hash: str | Unset = UNSET
    cred_type: DRepRegistrationCredType | Unset = UNSET
    epoch: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        slot = self.slot

        deposit = self.deposit

        drep_hash = self.drep_hash

        drep_id = self.drep_id

        anchor_url = self.anchor_url

        anchor_hash = self.anchor_hash

        cred_type: str | Unset = UNSET
        if not isinstance(self.cred_type, Unset):
            cred_type = self.cred_type.value

        epoch = self.epoch

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if slot is not UNSET:
            field_dict["slot"] = slot
        if deposit is not UNSET:
            field_dict["deposit"] = deposit
        if drep_hash is not UNSET:
            field_dict["drep_hash"] = drep_hash
        if drep_id is not UNSET:
            field_dict["drep_id"] = drep_id
        if anchor_url is not UNSET:
            field_dict["anchor_url"] = anchor_url
        if anchor_hash is not UNSET:
            field_dict["anchor_hash"] = anchor_hash
        if cred_type is not UNSET:
            field_dict["cred_type"] = cred_type
        if epoch is not UNSET:
            field_dict["epoch"] = epoch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DRepRegistrationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DRepRegistrationType(_type_)

        slot = d.pop("slot", UNSET)

        deposit = d.pop("deposit", UNSET)

        drep_hash = d.pop("drep_hash", UNSET)

        drep_id = d.pop("drep_id", UNSET)

        anchor_url = d.pop("anchor_url", UNSET)

        anchor_hash = d.pop("anchor_hash", UNSET)

        _cred_type = d.pop("cred_type", UNSET)
        cred_type: DRepRegistrationCredType | Unset
        if isinstance(_cred_type, Unset):
            cred_type = UNSET
        else:
            cred_type = DRepRegistrationCredType(_cred_type)

        epoch = d.pop("epoch", UNSET)

        d_rep_registration = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            cert_index=cert_index,
            type_=type_,
            slot=slot,
            deposit=deposit,
            drep_hash=drep_hash,
            drep_id=drep_id,
            anchor_url=anchor_url,
            anchor_hash=anchor_hash,
            cred_type=cred_type,
            epoch=epoch,
        )

        d_rep_registration.additional_properties = d
        return d_rep_registration

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
