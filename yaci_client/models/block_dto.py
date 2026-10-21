from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vrf import Vrf


T = TypeVar("T", bound="BlockDto")


@_attrs_define
class BlockDto:
    """
    Attributes:
        time (int | Unset):
        height (int | Unset):
        number (int | Unset):
        hash_ (str | Unset):
        slot (int | Unset):
        epoch (int | Unset):
        era (int | Unset):
        epoch_slot (int | Unset):
        slot_leader (str | Unset):
        size (int | Unset):
        tx_count (int | Unset):
        output (int | Unset):
        fees (int | Unset):
        block_vrf (str | Unset):
        op_cert (str | Unset):
        op_cert_counter (int | Unset):
        op_cert_kes_period (int | Unset):
        op_cert_sigma (str | Unset):
        previous_block (str | Unset):
        issuer_vkey (str | Unset):
        nonce_vrf (Vrf | Unset):
        leader_vrf (Vrf | Unset):
        vrf_result (Vrf | Unset):
        block_body_hash (str | Unset):
        protocol_version (str | Unset):
    """

    time: int | Unset = UNSET
    height: int | Unset = UNSET
    number: int | Unset = UNSET
    hash_: str | Unset = UNSET
    slot: int | Unset = UNSET
    epoch: int | Unset = UNSET
    era: int | Unset = UNSET
    epoch_slot: int | Unset = UNSET
    slot_leader: str | Unset = UNSET
    size: int | Unset = UNSET
    tx_count: int | Unset = UNSET
    output: int | Unset = UNSET
    fees: int | Unset = UNSET
    block_vrf: str | Unset = UNSET
    op_cert: str | Unset = UNSET
    op_cert_counter: int | Unset = UNSET
    op_cert_kes_period: int | Unset = UNSET
    op_cert_sigma: str | Unset = UNSET
    previous_block: str | Unset = UNSET
    issuer_vkey: str | Unset = UNSET
    nonce_vrf: Vrf | Unset = UNSET
    leader_vrf: Vrf | Unset = UNSET
    vrf_result: Vrf | Unset = UNSET
    block_body_hash: str | Unset = UNSET
    protocol_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        height = self.height

        number = self.number

        hash_ = self.hash_

        slot = self.slot

        epoch = self.epoch

        era = self.era

        epoch_slot = self.epoch_slot

        slot_leader = self.slot_leader

        size = self.size

        tx_count = self.tx_count

        output = self.output

        fees = self.fees

        block_vrf = self.block_vrf

        op_cert = self.op_cert

        op_cert_counter = self.op_cert_counter

        op_cert_kes_period = self.op_cert_kes_period

        op_cert_sigma = self.op_cert_sigma

        previous_block = self.previous_block

        issuer_vkey = self.issuer_vkey

        nonce_vrf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nonce_vrf, Unset):
            nonce_vrf = self.nonce_vrf.to_dict()

        leader_vrf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.leader_vrf, Unset):
            leader_vrf = self.leader_vrf.to_dict()

        vrf_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vrf_result, Unset):
            vrf_result = self.vrf_result.to_dict()

        block_body_hash = self.block_body_hash

        protocol_version = self.protocol_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if height is not UNSET:
            field_dict["height"] = height
        if number is not UNSET:
            field_dict["number"] = number
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if slot is not UNSET:
            field_dict["slot"] = slot
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if era is not UNSET:
            field_dict["era"] = era
        if epoch_slot is not UNSET:
            field_dict["epoch_slot"] = epoch_slot
        if slot_leader is not UNSET:
            field_dict["slot_leader"] = slot_leader
        if size is not UNSET:
            field_dict["size"] = size
        if tx_count is not UNSET:
            field_dict["tx_count"] = tx_count
        if output is not UNSET:
            field_dict["output"] = output
        if fees is not UNSET:
            field_dict["fees"] = fees
        if block_vrf is not UNSET:
            field_dict["block_vrf"] = block_vrf
        if op_cert is not UNSET:
            field_dict["op_cert"] = op_cert
        if op_cert_counter is not UNSET:
            field_dict["op_cert_counter"] = op_cert_counter
        if op_cert_kes_period is not UNSET:
            field_dict["op_cert_kes_period"] = op_cert_kes_period
        if op_cert_sigma is not UNSET:
            field_dict["op_cert_sigma"] = op_cert_sigma
        if previous_block is not UNSET:
            field_dict["previous_block"] = previous_block
        if issuer_vkey is not UNSET:
            field_dict["issuer_vkey"] = issuer_vkey
        if nonce_vrf is not UNSET:
            field_dict["nonce_vrf"] = nonce_vrf
        if leader_vrf is not UNSET:
            field_dict["leader_vrf"] = leader_vrf
        if vrf_result is not UNSET:
            field_dict["vrf_result"] = vrf_result
        if block_body_hash is not UNSET:
            field_dict["block_body_hash"] = block_body_hash
        if protocol_version is not UNSET:
            field_dict["protocol_version"] = protocol_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vrf import Vrf

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        height = d.pop("height", UNSET)

        number = d.pop("number", UNSET)

        hash_ = d.pop("hash", UNSET)

        slot = d.pop("slot", UNSET)

        epoch = d.pop("epoch", UNSET)

        era = d.pop("era", UNSET)

        epoch_slot = d.pop("epoch_slot", UNSET)

        slot_leader = d.pop("slot_leader", UNSET)

        size = d.pop("size", UNSET)

        tx_count = d.pop("tx_count", UNSET)

        output = d.pop("output", UNSET)

        fees = d.pop("fees", UNSET)

        block_vrf = d.pop("block_vrf", UNSET)

        op_cert = d.pop("op_cert", UNSET)

        op_cert_counter = d.pop("op_cert_counter", UNSET)

        op_cert_kes_period = d.pop("op_cert_kes_period", UNSET)

        op_cert_sigma = d.pop("op_cert_sigma", UNSET)

        previous_block = d.pop("previous_block", UNSET)

        issuer_vkey = d.pop("issuer_vkey", UNSET)

        _nonce_vrf = d.pop("nonce_vrf", UNSET)
        nonce_vrf: Vrf | Unset
        if isinstance(_nonce_vrf, Unset):
            nonce_vrf = UNSET
        else:
            nonce_vrf = Vrf.from_dict(_nonce_vrf)

        _leader_vrf = d.pop("leader_vrf", UNSET)
        leader_vrf: Vrf | Unset
        if isinstance(_leader_vrf, Unset):
            leader_vrf = UNSET
        else:
            leader_vrf = Vrf.from_dict(_leader_vrf)

        _vrf_result = d.pop("vrf_result", UNSET)
        vrf_result: Vrf | Unset
        if isinstance(_vrf_result, Unset):
            vrf_result = UNSET
        else:
            vrf_result = Vrf.from_dict(_vrf_result)

        block_body_hash = d.pop("block_body_hash", UNSET)

        protocol_version = d.pop("protocol_version", UNSET)

        block_dto = cls(
            time=time,
            height=height,
            number=number,
            hash_=hash_,
            slot=slot,
            epoch=epoch,
            era=era,
            epoch_slot=epoch_slot,
            slot_leader=slot_leader,
            size=size,
            tx_count=tx_count,
            output=output,
            fees=fees,
            block_vrf=block_vrf,
            op_cert=op_cert,
            op_cert_counter=op_cert_counter,
            op_cert_kes_period=op_cert_kes_period,
            op_cert_sigma=op_cert_sigma,
            previous_block=previous_block,
            issuer_vkey=issuer_vkey,
            nonce_vrf=nonce_vrf,
            leader_vrf=leader_vrf,
            vrf_result=vrf_result,
            block_body_hash=block_body_hash,
            protocol_version=protocol_version,
        )

        block_dto.additional_properties = d
        return block_dto

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
