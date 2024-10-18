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
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="TxUtxo")


@_attrs_define
class TxUtxo:
    """
    Attributes:
        tx_hash (Union[Unset, str]):
        output_index (Union[Unset, int]):
        address (Union[Unset, str]):
        stake_address (Union[Unset, str]):
        amount (Union[Unset, List['Amt']]):
        data_hash (Union[Unset, str]):
        inline_datum (Union[Unset, str]):
        script_ref (Union[Unset, str]):
        reference_script_hash (Union[Unset, str]):
        inline_datum_json (Union[Unset, JsonNode]):
    """

    tx_hash: Union[Unset, str] = UNSET
    output_index: Union[Unset, int] = UNSET
    address: Union[Unset, str] = UNSET
    stake_address: Union[Unset, str] = UNSET
    amount: Union[Unset, List["Amt"]] = UNSET
    data_hash: Union[Unset, str] = UNSET
    inline_datum: Union[Unset, str] = UNSET
    script_ref: Union[Unset, str] = UNSET
    reference_script_hash: Union[Unset, str] = UNSET
    inline_datum_json: Union[Unset, "JsonNode"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        tx_hash = self.tx_hash

        output_index = self.output_index

        address = self.address

        stake_address = self.stake_address

        amount: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amount, Unset):
            amount = []
            for amount_item_data in self.amount:
                amount_item = amount_item_data.to_dict()
                amount.append(amount_item)

        data_hash = self.data_hash

        inline_datum = self.inline_datum

        script_ref = self.script_ref

        reference_script_hash = self.reference_script_hash

        inline_datum_json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inline_datum_json, Unset):
            inline_datum_json = self.inline_datum_json.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if output_index is not UNSET:
            field_dict["output_index"] = output_index
        if address is not UNSET:
            field_dict["address"] = address
        if stake_address is not UNSET:
            field_dict["stake_address"] = stake_address
        if amount is not UNSET:
            field_dict["amount"] = amount
        if data_hash is not UNSET:
            field_dict["data_hash"] = data_hash
        if inline_datum is not UNSET:
            field_dict["inline_datum"] = inline_datum
        if script_ref is not UNSET:
            field_dict["script_ref"] = script_ref
        if reference_script_hash is not UNSET:
            field_dict["reference_script_hash"] = reference_script_hash
        if inline_datum_json is not UNSET:
            field_dict["inline_datum_json"] = inline_datum_json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amt import Amt
        from ..models.json_node import JsonNode

        d = src_dict.copy()
        tx_hash = d.pop("tx_hash", UNSET)

        output_index = d.pop("output_index", UNSET)

        address = d.pop("address", UNSET)

        stake_address = d.pop("stake_address", UNSET)

        amount = []
        _amount = d.pop("amount", UNSET)
        for amount_item_data in _amount or []:
            amount_item = Amt.from_dict(amount_item_data)

            amount.append(amount_item)

        data_hash = d.pop("data_hash", UNSET)

        inline_datum = d.pop("inline_datum", UNSET)

        script_ref = d.pop("script_ref", UNSET)

        reference_script_hash = d.pop("reference_script_hash", UNSET)

        _inline_datum_json = d.pop("inline_datum_json", UNSET)
        inline_datum_json: Union[Unset, JsonNode]
        if isinstance(_inline_datum_json, Unset):
            inline_datum_json = UNSET
        else:
            inline_datum_json = JsonNode.from_dict(_inline_datum_json)

        tx_utxo = cls(
            tx_hash=tx_hash,
            output_index=output_index,
            address=address,
            stake_address=stake_address,
            amount=amount,
            data_hash=data_hash,
            inline_datum=inline_datum,
            script_ref=script_ref,
            reference_script_hash=reference_script_hash,
            inline_datum_json=inline_datum_json,
        )

        tx_utxo.additional_properties = d
        return tx_utxo

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
