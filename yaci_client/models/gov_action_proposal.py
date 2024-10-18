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

from ..models.gov_action_proposal_type import GovActionProposalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="GovActionProposal")


@_attrs_define
class GovActionProposal:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        tx_hash (Union[Unset, str]):
        index (Union[Unset, int]):
        slot (Union[Unset, int]):
        deposit (Union[Unset, int]):
        return_address (Union[Unset, str]):
        type (Union[Unset, GovActionProposalType]):
        details (Union[Unset, JsonNode]):
        anchor_url (Union[Unset, str]):
        anchor_hash (Union[Unset, str]):
        epoch (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    deposit: Union[Unset, int] = UNSET
    return_address: Union[Unset, str] = UNSET
    type: Union[Unset, GovActionProposalType] = UNSET
    details: Union[Unset, "JsonNode"] = UNSET
    anchor_url: Union[Unset, str] = UNSET
    anchor_hash: Union[Unset, str] = UNSET
    epoch: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        index = self.index

        slot = self.slot

        deposit = self.deposit

        return_address = self.return_address

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        anchor_url = self.anchor_url

        anchor_hash = self.anchor_hash

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
        if index is not UNSET:
            field_dict["index"] = index
        if slot is not UNSET:
            field_dict["slot"] = slot
        if deposit is not UNSET:
            field_dict["deposit"] = deposit
        if return_address is not UNSET:
            field_dict["return_address"] = return_address
        if type is not UNSET:
            field_dict["type"] = type
        if details is not UNSET:
            field_dict["details"] = details
        if anchor_url is not UNSET:
            field_dict["anchor_url"] = anchor_url
        if anchor_hash is not UNSET:
            field_dict["anchor_hash"] = anchor_hash
        if epoch is not UNSET:
            field_dict["epoch"] = epoch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.json_node import JsonNode

        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        index = d.pop("index", UNSET)

        slot = d.pop("slot", UNSET)

        deposit = d.pop("deposit", UNSET)

        return_address = d.pop("return_address", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GovActionProposalType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GovActionProposalType(_type)

        _details = d.pop("details", UNSET)
        details: Union[Unset, JsonNode]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = JsonNode.from_dict(_details)

        anchor_url = d.pop("anchor_url", UNSET)

        anchor_hash = d.pop("anchor_hash", UNSET)

        epoch = d.pop("epoch", UNSET)

        gov_action_proposal = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            index=index,
            slot=slot,
            deposit=deposit,
            return_address=return_address,
            type=type,
            details=details,
            anchor_url=anchor_url,
            anchor_hash=anchor_hash,
            epoch=epoch,
        )

        gov_action_proposal.additional_properties = d
        return gov_action_proposal

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
