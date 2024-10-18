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

from ..models.move_instataneous_reward_pot import MoveInstataneousRewardPot
from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveInstataneousReward")


@_attrs_define
class MoveInstataneousReward:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        pot (Union[Unset, MoveInstataneousRewardPot]):
        tx_hash (Union[Unset, str]):
        cert_index (Union[Unset, int]):
        credential (Union[Unset, str]):
        address (Union[Unset, str]):
        amount (Union[Unset, int]):
        epoch (Union[Unset, int]):
        slot (Union[Unset, int]):
        block_hash (Union[Unset, str]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    pot: Union[Unset, MoveInstataneousRewardPot] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    cert_index: Union[Unset, int] = UNSET
    credential: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    epoch: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    block_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        pot: Union[Unset, str] = UNSET
        if not isinstance(self.pot, Unset):
            pot = self.pot.value

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        credential = self.credential

        address = self.address

        amount = self.amount

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
        if pot is not UNSET:
            field_dict["pot"] = pot
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if cert_index is not UNSET:
            field_dict["cert_index"] = cert_index
        if credential is not UNSET:
            field_dict["credential"] = credential
        if address is not UNSET:
            field_dict["address"] = address
        if amount is not UNSET:
            field_dict["amount"] = amount
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

        _pot = d.pop("pot", UNSET)
        pot: Union[Unset, MoveInstataneousRewardPot]
        if isinstance(_pot, Unset):
            pot = UNSET
        else:
            pot = MoveInstataneousRewardPot(_pot)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        credential = d.pop("credential", UNSET)

        address = d.pop("address", UNSET)

        amount = d.pop("amount", UNSET)

        epoch = d.pop("epoch", UNSET)

        slot = d.pop("slot", UNSET)

        block_hash = d.pop("block_hash", UNSET)

        move_instataneous_reward = cls(
            block_number=block_number,
            block_time=block_time,
            pot=pot,
            tx_hash=tx_hash,
            cert_index=cert_index,
            credential=credential,
            address=address,
            amount=amount,
            epoch=epoch,
            slot=slot,
            block_hash=block_hash,
        )

        move_instataneous_reward.additional_properties = d
        return move_instataneous_reward

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
