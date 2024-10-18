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


T = TypeVar("T", bound="AddressUtxo")


@_attrs_define
class AddressUtxo:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        tx_hash (Union[Unset, str]):
        output_index (Union[Unset, int]):
        slot (Union[Unset, int]):
        block_hash (Union[Unset, str]):
        epoch (Union[Unset, int]):
        owner_addr (Union[Unset, str]):
        owner_stake_addr (Union[Unset, str]):
        owner_payment_credential (Union[Unset, str]):
        owner_stake_credential (Union[Unset, str]):
        lovelace_amount (Union[Unset, int]):
        amounts (Union[Unset, List['Amt']]):
        data_hash (Union[Unset, str]):
        inline_datum (Union[Unset, str]):
        script_ref (Union[Unset, str]):
        reference_script_hash (Union[Unset, str]):
        is_collateral_return (Union[Unset, bool]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    output_index: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    block_hash: Union[Unset, str] = UNSET
    epoch: Union[Unset, int] = UNSET
    owner_addr: Union[Unset, str] = UNSET
    owner_stake_addr: Union[Unset, str] = UNSET
    owner_payment_credential: Union[Unset, str] = UNSET
    owner_stake_credential: Union[Unset, str] = UNSET
    lovelace_amount: Union[Unset, int] = UNSET
    amounts: Union[Unset, List["Amt"]] = UNSET
    data_hash: Union[Unset, str] = UNSET
    inline_datum: Union[Unset, str] = UNSET
    script_ref: Union[Unset, str] = UNSET
    reference_script_hash: Union[Unset, str] = UNSET
    is_collateral_return: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        block_number = self.block_number

        block_time = self.block_time

        tx_hash = self.tx_hash

        output_index = self.output_index

        slot = self.slot

        block_hash = self.block_hash

        epoch = self.epoch

        owner_addr = self.owner_addr

        owner_stake_addr = self.owner_stake_addr

        owner_payment_credential = self.owner_payment_credential

        owner_stake_credential = self.owner_stake_credential

        lovelace_amount = self.lovelace_amount

        amounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = []
            for amounts_item_data in self.amounts:
                amounts_item = amounts_item_data.to_dict()
                amounts.append(amounts_item)

        data_hash = self.data_hash

        inline_datum = self.inline_datum

        script_ref = self.script_ref

        reference_script_hash = self.reference_script_hash

        is_collateral_return = self.is_collateral_return

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if output_index is not UNSET:
            field_dict["output_index"] = output_index
        if slot is not UNSET:
            field_dict["slot"] = slot
        if block_hash is not UNSET:
            field_dict["block_hash"] = block_hash
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if owner_addr is not UNSET:
            field_dict["owner_addr"] = owner_addr
        if owner_stake_addr is not UNSET:
            field_dict["owner_stake_addr"] = owner_stake_addr
        if owner_payment_credential is not UNSET:
            field_dict["owner_payment_credential"] = owner_payment_credential
        if owner_stake_credential is not UNSET:
            field_dict["owner_stake_credential"] = owner_stake_credential
        if lovelace_amount is not UNSET:
            field_dict["lovelace_amount"] = lovelace_amount
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if data_hash is not UNSET:
            field_dict["data_hash"] = data_hash
        if inline_datum is not UNSET:
            field_dict["inline_datum"] = inline_datum
        if script_ref is not UNSET:
            field_dict["script_ref"] = script_ref
        if reference_script_hash is not UNSET:
            field_dict["reference_script_hash"] = reference_script_hash
        if is_collateral_return is not UNSET:
            field_dict["is_collateral_return"] = is_collateral_return

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amt import Amt

        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        output_index = d.pop("output_index", UNSET)

        slot = d.pop("slot", UNSET)

        block_hash = d.pop("block_hash", UNSET)

        epoch = d.pop("epoch", UNSET)

        owner_addr = d.pop("owner_addr", UNSET)

        owner_stake_addr = d.pop("owner_stake_addr", UNSET)

        owner_payment_credential = d.pop("owner_payment_credential", UNSET)

        owner_stake_credential = d.pop("owner_stake_credential", UNSET)

        lovelace_amount = d.pop("lovelace_amount", UNSET)

        amounts = []
        _amounts = d.pop("amounts", UNSET)
        for amounts_item_data in _amounts or []:
            amounts_item = Amt.from_dict(amounts_item_data)

            amounts.append(amounts_item)

        data_hash = d.pop("data_hash", UNSET)

        inline_datum = d.pop("inline_datum", UNSET)

        script_ref = d.pop("script_ref", UNSET)

        reference_script_hash = d.pop("reference_script_hash", UNSET)

        is_collateral_return = d.pop("is_collateral_return", UNSET)

        address_utxo = cls(
            block_number=block_number,
            block_time=block_time,
            tx_hash=tx_hash,
            output_index=output_index,
            slot=slot,
            block_hash=block_hash,
            epoch=epoch,
            owner_addr=owner_addr,
            owner_stake_addr=owner_stake_addr,
            owner_payment_credential=owner_payment_credential,
            owner_stake_credential=owner_stake_credential,
            lovelace_amount=lovelace_amount,
            amounts=amounts,
            data_hash=data_hash,
            inline_datum=inline_datum,
            script_ref=script_ref,
            reference_script_hash=reference_script_hash,
            is_collateral_return=is_collateral_return,
        )

        address_utxo.additional_properties = d
        return address_utxo

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
