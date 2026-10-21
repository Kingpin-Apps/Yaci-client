from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        block_number (int | Unset):
        block_time (int | Unset):
        tx_hash (str | Unset):
        output_index (int | Unset):
        slot (int | Unset):
        block_hash (str | Unset):
        epoch (int | Unset):
        owner_addr (str | Unset):
        owner_stake_addr (str | Unset):
        owner_payment_credential (str | Unset):
        owner_stake_credential (str | Unset):
        lovelace_amount (int | Unset):
        amounts (list[Amt] | Unset):
        data_hash (str | Unset):
        inline_datum (str | Unset):
        script_ref (str | Unset):
        reference_script_hash (str | Unset):
        is_collateral_return (bool | Unset):
    """

    block_number: int | Unset = UNSET
    block_time: int | Unset = UNSET
    tx_hash: str | Unset = UNSET
    output_index: int | Unset = UNSET
    slot: int | Unset = UNSET
    block_hash: str | Unset = UNSET
    epoch: int | Unset = UNSET
    owner_addr: str | Unset = UNSET
    owner_stake_addr: str | Unset = UNSET
    owner_payment_credential: str | Unset = UNSET
    owner_stake_credential: str | Unset = UNSET
    lovelace_amount: int | Unset = UNSET
    amounts: list[Amt] | Unset = UNSET
    data_hash: str | Unset = UNSET
    inline_datum: str | Unset = UNSET
    script_ref: str | Unset = UNSET
    reference_script_hash: str | Unset = UNSET
    is_collateral_return: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        amounts: list[dict[str, Any]] | Unset = UNSET
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

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amt import Amt

        d = dict(src_dict)
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

        _amounts = d.pop("amounts", UNSET)
        amounts: list[Amt] | Unset = UNSET
        if _amounts is not UNSET:
            amounts = []
            for amounts_item_data in _amounts:
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
