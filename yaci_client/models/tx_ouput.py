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


T = TypeVar("T", bound="TxOuput")


@_attrs_define
class TxOuput:
    """
    Attributes:
        address (Union[Unset, str]):
        amounts (Union[Unset, List['Amt']]):
        data_hash (Union[Unset, str]):
        inline_datum (Union[Unset, str]):
        reference_script_hash (Union[Unset, str]):
    """

    address: Union[Unset, str] = UNSET
    amounts: Union[Unset, List["Amt"]] = UNSET
    data_hash: Union[Unset, str] = UNSET
    inline_datum: Union[Unset, str] = UNSET
    reference_script_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        address = self.address

        amounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = []
            for amounts_item_data in self.amounts:
                amounts_item = amounts_item_data.to_dict()
                amounts.append(amounts_item)

        data_hash = self.data_hash

        inline_datum = self.inline_datum

        reference_script_hash = self.reference_script_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if data_hash is not UNSET:
            field_dict["dataHash"] = data_hash
        if inline_datum is not UNSET:
            field_dict["inlineDatum"] = inline_datum
        if reference_script_hash is not UNSET:
            field_dict["referenceScriptHash"] = reference_script_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amt import Amt

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        amounts = []
        _amounts = d.pop("amounts", UNSET)
        for amounts_item_data in _amounts or []:
            amounts_item = Amt.from_dict(amounts_item_data)

            amounts.append(amounts_item)

        data_hash = d.pop("dataHash", UNSET)

        inline_datum = d.pop("inlineDatum", UNSET)

        reference_script_hash = d.pop("referenceScriptHash", UNSET)

        tx_ouput = cls(
            address=address,
            amounts=amounts,
            data_hash=data_hash,
            inline_datum=inline_datum,
            reference_script_hash=reference_script_hash,
        )

        tx_ouput.additional_properties = d
        return tx_ouput

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
