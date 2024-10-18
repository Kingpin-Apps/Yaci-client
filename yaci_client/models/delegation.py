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

T = TypeVar("T", bound="Delegation")


@_attrs_define
class Delegation:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        credential (Union[Unset, str]):
        address (Union[Unset, str]):
        pool_id (Union[Unset, str]):
        tx_hash (Union[Unset, str]):
        cert_index (Union[Unset, int]):
        epoch (Union[Unset, int]):
        slot (Union[Unset, int]):
        block_hash (Union[Unset, str]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    credential: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    pool_id: Union[Unset, str] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    cert_index: Union[Unset, int] = UNSET
    epoch: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    block_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        credential = self.credential

        address = self.address

        pool_id = self.pool_id

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        epoch = self.epoch

        slot = self.slot

        block_hash = self.block_hash

        field_dict: Dict[str, Any] = {}
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
        if pool_id is not UNSET:
            field_dict["pool_id"] = pool_id
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if cert_index is not UNSET:
            field_dict["cert_index"] = cert_index
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if slot is not UNSET:
            field_dict["slot"] = slot
        if block_hash is not UNSET:
            field_dict["block_hash"] = block_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        credential = d.pop("credential", UNSET)

        address = d.pop("address", UNSET)

        pool_id = d.pop("pool_id", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        epoch = d.pop("epoch", UNSET)

        slot = d.pop("slot", UNSET)

        block_hash = d.pop("block_hash", UNSET)

        delegation = cls(
            block_number=block_number,
            block_time=block_time,
            credential=credential,
            address=address,
            pool_id=pool_id,
            tx_hash=tx_hash,
            cert_index=cert_index,
            epoch=epoch,
            slot=slot,
            block_hash=block_hash,
        )

        delegation.additional_properties = d
        return delegation

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
