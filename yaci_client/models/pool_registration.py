from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        block_number (int | Unset):
        block_time (int | Unset):
        tx_hash (str | Unset):
        cert_index (int | Unset):
        pool_id (str | Unset):
        vrf_key_hash (str | Unset):
        pledge (int | Unset):
        cost (int | Unset):
        margin (float | Unset):
        reward_account (str | Unset):
        pool_owners (list[str] | Unset):
        relays (list[Relay] | Unset):
        metadata_url (str | Unset):
        metadata_hash (str | Unset):
        epoch (int | Unset):
        slot (int | Unset):
        block_hash (str | Unset):
        reward_account_bech32 (str | Unset):
        pool_id_bech32 (str | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    tx_hash: str | Unset = UNSET
    cert_index: int | Unset = UNSET
    pool_id: str | Unset = UNSET
    vrf_key_hash: str | Unset = UNSET
    pledge: int | Unset = UNSET
    cost: int | Unset = UNSET
    margin: float | Unset = UNSET
    reward_account: str | Unset = UNSET
    pool_owners: list[str] | Unset = UNSET
    relays: list[Relay] | Unset = UNSET
    metadata_url: str | Unset = UNSET
    metadata_hash: str | Unset = UNSET
    epoch: int | Unset = UNSET
    slot: int | Unset = UNSET
    block_hash: str | Unset = UNSET
    reward_account_bech32: str | Unset = UNSET
    pool_id_bech32: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        pool_owners: list[str] | Unset = UNSET
        if not isinstance(self.pool_owners, Unset):
            pool_owners = self.pool_owners

        relays: list[dict[str, Any]] | Unset = UNSET
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relay import Relay

        d = dict(src_dict)
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

        pool_owners = cast(list[str], d.pop("pool_owners", UNSET))

        _relays = d.pop("relays", UNSET)
        relays: list[Relay] | Unset = UNSET
        if _relays is not UNSET:
            relays = []
            for relays_item_data in _relays:
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
