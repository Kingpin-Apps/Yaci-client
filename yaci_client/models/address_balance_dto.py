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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amt import Amt


T = TypeVar("T", bound="AddressBalanceDto")


@_attrs_define
class AddressBalanceDto:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        address (Union[Unset, str]):
        amounts (Union[Unset, List['Amt']]):
        slot (Union[Unset, int]):
        last_balance_calculation_block (Union[Unset, int]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    address: Union[Unset, str] = UNSET
    amounts: Union[Unset, List["Amt"]] = UNSET
    slot: Union[Unset, int] = UNSET
    last_balance_calculation_block: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        block_number = self.block_number

        block_time = self.block_time

        address = self.address

        amounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = []
            for amounts_item_data in self.amounts:
                amounts_item = amounts_item_data.to_dict()
                amounts.append(amounts_item)

        slot = self.slot

        last_balance_calculation_block = self.last_balance_calculation_block

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if address is not UNSET:
            field_dict["address"] = address
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if slot is not UNSET:
            field_dict["slot"] = slot
        if last_balance_calculation_block is not UNSET:
            field_dict["last_balance_calculation_block"] = (
                last_balance_calculation_block
            )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amt import Amt

        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        address = d.pop("address", UNSET)

        amounts = []
        _amounts = d.pop("amounts", UNSET)
        for amounts_item_data in _amounts or []:
            amounts_item = Amt.from_dict(amounts_item_data)

            amounts.append(amounts_item)

        slot = d.pop("slot", UNSET)

        last_balance_calculation_block = d.pop("last_balance_calculation_block", UNSET)

        address_balance_dto = cls(
            block_number=block_number,
            block_time=block_time,
            address=address,
            amounts=amounts,
            slot=slot,
            last_balance_calculation_block=last_balance_calculation_block,
        )

        address_balance_dto.additional_properties = d
        return address_balance_dto

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
