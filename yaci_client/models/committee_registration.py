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

from ..models.committee_registration_cred_type import CommitteeRegistrationCredType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitteeRegistration")


@_attrs_define
class CommitteeRegistration:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        tx_hash (Union[Unset, str]):
        cert_index (Union[Unset, int]):
        slot (Union[Unset, int]):
        cold_key (Union[Unset, str]):
        hot_key (Union[Unset, str]):
        cred_type (Union[Unset, CommitteeRegistrationCredType]):
        epoch (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    cert_index: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    cold_key: Union[Unset, str] = UNSET
    hot_key: Union[Unset, str] = UNSET
    cred_type: Union[Unset, CommitteeRegistrationCredType] = UNSET
    epoch: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        slot = self.slot

        cold_key = self.cold_key

        hot_key = self.hot_key

        cred_type: Union[Unset, str] = UNSET
        if not isinstance(self.cred_type, Unset):
            cred_type = self.cred_type.value

        epoch = self.epoch

        field_dict: Dict[str, Any] = {}
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
        if slot is not UNSET:
            field_dict["slot"] = slot
        if cold_key is not UNSET:
            field_dict["cold_key"] = cold_key
        if hot_key is not UNSET:
            field_dict["hot_key"] = hot_key
        if cred_type is not UNSET:
            field_dict["cred_type"] = cred_type
        if epoch is not UNSET:
            field_dict["epoch"] = epoch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        slot = d.pop("slot", UNSET)

        cold_key = d.pop("cold_key", UNSET)

        hot_key = d.pop("hot_key", UNSET)

        _cred_type = d.pop("cred_type", UNSET)
        cred_type: Union[Unset, CommitteeRegistrationCredType]
        if isinstance(_cred_type, Unset):
            cred_type = UNSET
        else:
            cred_type = CommitteeRegistrationCredType(_cred_type)

        epoch = d.pop("epoch", UNSET)

        committee_registration = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            cert_index=cert_index,
            slot=slot,
            cold_key=cold_key,
            hot_key=hot_key,
            cred_type=cred_type,
            epoch=epoch,
        )

        committee_registration.additional_properties = d
        return committee_registration

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
