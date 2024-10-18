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
    from ..models.amount import Amount


T = TypeVar("T", bound="Utxo")


@_attrs_define
class Utxo:
    """
    Attributes:
        tx_hash (Union[Unset, str]):
        output_index (Union[Unset, int]):
        address (Union[Unset, str]):
        amount (Union[Unset, List['Amount']]):
        data_hash (Union[Unset, str]):
        inline_datum (Union[Unset, str]):
        reference_script_hash (Union[Unset, str]):
        epoch (Union[Unset, int]):
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
    """

    tx_hash: Union[Unset, str] = UNSET
    output_index: Union[Unset, int] = UNSET
    address: Union[Unset, str] = UNSET
    amount: Union[Unset, List["Amount"]] = UNSET
    data_hash: Union[Unset, str] = UNSET
    inline_datum: Union[Unset, str] = UNSET
    reference_script_hash: Union[Unset, str] = UNSET
    epoch: Union[Unset, int] = UNSET
    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        tx_hash = self.tx_hash

        output_index = self.output_index

        address = self.address

        amount: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = []
            for amount_item_data in self.amount:
                amount_item = amount_item_data.to_dict()
                amount.append(amount_item)

        data_hash = self.data_hash

        inline_datum = self.inline_datum

        reference_script_hash = self.reference_script_hash

        epoch = self.epoch

        block_number = self.block_number

        block_time = self.block_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if output_index is not UNSET:
            field_dict["output_index"] = output_index
        if address is not UNSET:
            field_dict["address"] = address
        if amount is not UNSET:
            field_dict["amount"] = amount
        if data_hash is not UNSET:
            field_dict["data_hash"] = data_hash
        if inline_datum is not UNSET:
            field_dict["inline_datum"] = inline_datum
        if reference_script_hash is not UNSET:
            field_dict["reference_script_hash"] = reference_script_hash
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amount import Amount

        d = src_dict.copy()
        tx_hash = d.pop("tx_hash", UNSET)

        output_index = d.pop("output_index", UNSET)

        address = d.pop("address", UNSET)

        amount = []
        _amount = d.pop("amount", UNSET)
        for amount_item_data in _amount or []:
            amount_item = Amount.from_dict(amount_item_data)

            amount.append(amount_item)

        data_hash = d.pop("data_hash", UNSET)

        inline_datum = d.pop("inline_datum", UNSET)

        reference_script_hash = d.pop("reference_script_hash", UNSET)

        epoch = d.pop("epoch", UNSET)

        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        utxo = cls(
            tx_hash=tx_hash,
            output_index=output_index,
            address=address,
            amount=amount,
            data_hash=data_hash,
            inline_datum=inline_datum,
            reference_script_hash=reference_script_hash,
            epoch=epoch,
            block_number=block_number,
            block_time=block_time,
        )

        utxo.additional_properties = d
        return utxo

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
