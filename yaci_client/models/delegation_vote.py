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

from ..models.delegation_vote_cred_type import DelegationVoteCredType
from ..models.delegation_vote_drep_type import DelegationVoteDrepType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DelegationVote")


@_attrs_define
class DelegationVote:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        tx_hash (Union[Unset, str]):
        cert_index (Union[Unset, int]):
        slot (Union[Unset, int]):
        address (Union[Unset, str]):
        drep_hash (Union[Unset, str]):
        drep_id (Union[Unset, str]):
        drep_type (Union[Unset, DelegationVoteDrepType]):
        credential (Union[Unset, str]):
        cred_type (Union[Unset, DelegationVoteCredType]):
        epoch (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    cert_index: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    address: Union[Unset, str] = UNSET
    drep_hash: Union[Unset, str] = UNSET
    drep_id: Union[Unset, str] = UNSET
    drep_type: Union[Unset, DelegationVoteDrepType] = UNSET
    credential: Union[Unset, str] = UNSET
    cred_type: Union[Unset, DelegationVoteCredType] = UNSET
    epoch: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        slot = self.slot

        address = self.address

        drep_hash = self.drep_hash

        drep_id = self.drep_id

        drep_type: Union[Unset, str] = UNSET
        if not isinstance(self.drep_type, Unset):
            drep_type = self.drep_type.value

        credential = self.credential

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
        if address is not UNSET:
            field_dict["address"] = address
        if drep_hash is not UNSET:
            field_dict["drep_hash"] = drep_hash
        if drep_id is not UNSET:
            field_dict["drep_id"] = drep_id
        if drep_type is not UNSET:
            field_dict["drep_type"] = drep_type
        if credential is not UNSET:
            field_dict["credential"] = credential
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

        address = d.pop("address", UNSET)

        drep_hash = d.pop("drep_hash", UNSET)

        drep_id = d.pop("drep_id", UNSET)

        _drep_type = d.pop("drep_type", UNSET)
        drep_type: Union[Unset, DelegationVoteDrepType]
        if isinstance(_drep_type, Unset):
            drep_type = UNSET
        else:
            drep_type = DelegationVoteDrepType(_drep_type)

        credential = d.pop("credential", UNSET)

        _cred_type = d.pop("cred_type", UNSET)
        cred_type: Union[Unset, DelegationVoteCredType]
        if isinstance(_cred_type, Unset):
            cred_type = UNSET
        else:
            cred_type = DelegationVoteCredType(_cred_type)

        epoch = d.pop("epoch", UNSET)

        delegation_vote = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            cert_index=cert_index,
            slot=slot,
            address=address,
            drep_hash=drep_hash,
            drep_id=drep_id,
            drep_type=drep_type,
            credential=credential,
            cred_type=cred_type,
            epoch=epoch,
        )

        delegation_vote.additional_properties = d
        return delegation_vote

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
