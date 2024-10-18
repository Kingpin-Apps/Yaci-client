from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.protocol_params_proposal_era import ProtocolParamsProposalEra
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protocol_params import ProtocolParams


T = TypeVar("T", bound="ProtocolParamsProposal")


@_attrs_define
class ProtocolParamsProposal:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        tx_hash (Union[Unset, str]):
        key_hash (Union[Unset, str]):
        target_epoch (Union[Unset, int]):
        params (Union[Unset, ProtocolParams]):
        epoch (Union[Unset, int]):
        slot (Union[Unset, int]):
        era (Union[Unset, ProtocolParamsProposalEra]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    key_hash: Union[Unset, str] = UNSET
    target_epoch: Union[Unset, int] = UNSET
    params: Union[Unset, "ProtocolParams"] = UNSET
    epoch: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    era: Union[Unset, ProtocolParamsProposalEra] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        key_hash = self.key_hash

        target_epoch = self.target_epoch

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        epoch = self.epoch

        slot = self.slot

        era: Union[Unset, str] = UNSET
        if not isinstance(self.era, Unset):
            era = self.era.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if key_hash is not UNSET:
            field_dict["key_hash"] = key_hash
        if target_epoch is not UNSET:
            field_dict["target_epoch"] = target_epoch
        if params is not UNSET:
            field_dict["params"] = params
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if slot is not UNSET:
            field_dict["slot"] = slot
        if era is not UNSET:
            field_dict["era"] = era

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.protocol_params import ProtocolParams

        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        key_hash = d.pop("key_hash", UNSET)

        target_epoch = d.pop("target_epoch", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ProtocolParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ProtocolParams.from_dict(_params)

        epoch = d.pop("epoch", UNSET)

        slot = d.pop("slot", UNSET)

        _era = d.pop("era", UNSET)
        era: Union[Unset, ProtocolParamsProposalEra]
        if isinstance(_era, Unset):
            era = UNSET
        else:
            era = ProtocolParamsProposalEra(_era)

        protocol_params_proposal = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            key_hash=key_hash,
            target_epoch=target_epoch,
            params=params,
            epoch=epoch,
            slot=slot,
            era=era,
        )

        protocol_params_proposal.additional_properties = d
        return protocol_params_proposal

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
