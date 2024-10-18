from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relay import Relay


T = TypeVar("T", bound="PoolRegistration")


@_attrs_define
class PoolRegistration:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        tx_hash (Union[Unset, str]):
        cert_index (Union[Unset, int]):
        pool_id (Union[Unset, str]):
        vrf_key_hash (Union[Unset, str]):
        pledge (Union[Unset, int]):
        cost (Union[Unset, int]):
        margin (Union[Unset, float]):
        reward_account (Union[Unset, str]):
        pool_owners (Union[Unset, List[str]]):
        relays (Union[Unset, List['Relay']]):
        metadata_url (Union[Unset, str]):
        metadata_hash (Union[Unset, str]):
        epoch (Union[Unset, int]):
        slot (Union[Unset, int]):
        block_hash (Union[Unset, str]):
        reward_account_bech32 (Union[Unset, str]):
        pool_id_bech32 (Union[Unset, str]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    cert_index: Union[Unset, int] = UNSET
    pool_id: Union[Unset, str] = UNSET
    vrf_key_hash: Union[Unset, str] = UNSET
    pledge: Union[Unset, int] = UNSET
    cost: Union[Unset, int] = UNSET
    margin: Union[Unset, float] = UNSET
    reward_account: Union[Unset, str] = UNSET
    pool_owners: Union[Unset, List[str]] = UNSET
    relays: Union[Unset, List["Relay"]] = UNSET
    metadata_url: Union[Unset, str] = UNSET
    metadata_hash: Union[Unset, str] = UNSET
    epoch: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    block_hash: Union[Unset, str] = UNSET
    reward_account_bech32: Union[Unset, str] = UNSET
    pool_id_bech32: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        cert_index = self.cert_index

        pool_id = self.pool_id

        vrf_key_hash = self.vrf_key_hash

        pledge = self.pledge

        cost = self.cost

        margin = self.margin

        reward_account = self.reward_account

        pool_owners: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pool_owners, Unset):
            pool_owners = self.pool_owners

        relays: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relays, Unset):
            relays = []
            for relays_item_data in self.relays:
                relays_item = relays_item_data.to_dict()
                relays.append(relays_item)

        metadata_url = self.metadata_url

        metadata_hash = self.metadata_hash

        epoch = self.epoch

        slot = self.slot

        block_hash = self.block_hash

        reward_account_bech32 = self.reward_account_bech32

        pool_id_bech32 = self.pool_id_bech32

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
        if pool_id is not UNSET:
            field_dict["pool_id"] = pool_id
        if vrf_key_hash is not UNSET:
            field_dict["vrf_key_hash"] = vrf_key_hash
        if pledge is not UNSET:
            field_dict["pledge"] = pledge
        if cost is not UNSET:
            field_dict["cost"] = cost
        if margin is not UNSET:
            field_dict["margin"] = margin
        if reward_account is not UNSET:
            field_dict["reward_account"] = reward_account
        if pool_owners is not UNSET:
            field_dict["pool_owners"] = pool_owners
        if relays is not UNSET:
            field_dict["relays"] = relays
        if metadata_url is not UNSET:
            field_dict["metadata_url"] = metadata_url
        if metadata_hash is not UNSET:
            field_dict["metadata_hash"] = metadata_hash
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if slot is not UNSET:
            field_dict["slot"] = slot
        if block_hash is not UNSET:
            field_dict["block_hash"] = block_hash
        if reward_account_bech32 is not UNSET:
            field_dict["reward_account_bech32"] = reward_account_bech32
        if pool_id_bech32 is not UNSET:
            field_dict["pool_id_bech32"] = pool_id_bech32

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relay import Relay

        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        cert_index = d.pop("cert_index", UNSET)

        pool_id = d.pop("pool_id", UNSET)

        vrf_key_hash = d.pop("vrf_key_hash", UNSET)

        pledge = d.pop("pledge", UNSET)

        cost = d.pop("cost", UNSET)

        margin = d.pop("margin", UNSET)

        reward_account = d.pop("reward_account", UNSET)

        pool_owners = cast(List[str], d.pop("pool_owners", UNSET))

        relays = []
        _relays = d.pop("relays", UNSET)
        for relays_item_data in _relays or []:
            relays_item = Relay.from_dict(relays_item_data)

            relays.append(relays_item)

        metadata_url = d.pop("metadata_url", UNSET)

        metadata_hash = d.pop("metadata_hash", UNSET)

        epoch = d.pop("epoch", UNSET)

        slot = d.pop("slot", UNSET)

        block_hash = d.pop("block_hash", UNSET)

        reward_account_bech32 = d.pop("reward_account_bech32", UNSET)

        pool_id_bech32 = d.pop("pool_id_bech32", UNSET)

        pool_registration = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            cert_index=cert_index,
            pool_id=pool_id,
            vrf_key_hash=vrf_key_hash,
            pledge=pledge,
            cost=cost,
            margin=margin,
            reward_account=reward_account,
            pool_owners=pool_owners,
            relays=relays,
            metadata_url=metadata_url,
            metadata_hash=metadata_hash,
            epoch=epoch,
            slot=slot,
            block_hash=block_hash,
            reward_account_bech32=reward_account_bech32,
            pool_id_bech32=pool_id_bech32,
        )

        pool_registration.additional_properties = d
        return pool_registration

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
