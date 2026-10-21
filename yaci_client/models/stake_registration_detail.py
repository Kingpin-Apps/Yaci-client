import builtins
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stake_registration_detail_type import StakeRegistrationDetailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StakeRegistrationDetail")


@_attrs_define
class StakeRegistrationDetail:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        credential (Union[Unset, str]):
        address (Union[Unset, str]):
        tx_hash (Union[Unset, str]):
        cert_index (Union[Unset, int]):
        type (Union[Unset, StakeRegistrationDetailType]):
        epoch (Union[Unset, int]):
        slot (Union[Unset, int]):
        block_hash (Union[Unset, str]):
    """

    block_number: Unset | int = UNSET
    block_time: Unset | int = UNSET
    credential: Unset | str = UNSET
    address: Unset | str = UNSET
    tx_hash: Unset | str = UNSET
    cert_index: Unset | int = UNSET
    type: Unset | StakeRegistrationDetailType = UNSET
    epoch: Unset | int = UNSET
    slot: Unset | int = UNSET
    block_hash: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        credential = self.credential

        address = self.address

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

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
        if type is not UNSET:
            field_dict["type"] = type
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if slot is not UNSET:
            field_dict["slot"] = slot
        if block_hash is not UNSET:
            field_dict["block_hash"] = block_hash

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        credential = d.pop("credential", UNSET)

        address = d.pop("address", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        _type = d.pop("type", UNSET)
        type: Unset | StakeRegistrationDetailType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = StakeRegistrationDetailType(_type)

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
            type=type,
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
