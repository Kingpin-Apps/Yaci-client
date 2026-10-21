from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tx_ouput import TxOuput
    from ..models.tx_utxo import TxUtxo


T = TypeVar("T", bound="TransactionDetails")


@_attrs_define
class TransactionDetails:
    """
    Attributes:
        hash_ (str | Unset):
        block_height (int | Unset):
        slot (int | Unset):
        inputs (list[TxUtxo] | Unset):
        outputs (list[TxUtxo] | Unset):
        utxo_count (int | Unset):
        total_output (int | Unset):
        fees (int | Unset):
        ttl (int | Unset):
        auxiliary_data_hash (str | Unset):
        validity_interval_start (int | Unset):
        script_data_hash (str | Unset):
        collateral_inputs (list[TxUtxo] | Unset):
        required_signers (list[str] | Unset):
        netowrk_id (int | Unset):
        collateral_return (TxOuput | Unset):
        total_collateral (int | Unset):
        reference_inputs (list[TxUtxo] | Unset):
        invalid (bool | Unset):
    """

    hash_: str | Unset = UNSET
    block_height: int | Unset = UNSET
    slot: int | Unset = UNSET
    inputs: list[TxUtxo] | Unset = UNSET
    outputs: list[TxUtxo] | Unset = UNSET
    utxo_count: int | Unset = UNSET
    total_output: int | Unset = UNSET
    fees: int | Unset = UNSET
    ttl: int | Unset = UNSET
    auxiliary_data_hash: str | Unset = UNSET
    validity_interval_start: int | Unset = UNSET
    script_data_hash: str | Unset = UNSET
    collateral_inputs: list[TxUtxo] | Unset = UNSET
    required_signers: list[str] | Unset = UNSET
    netowrk_id: int | Unset = UNSET
    collateral_return: TxOuput | Unset = UNSET
    total_collateral: int | Unset = UNSET
    reference_inputs: list[TxUtxo] | Unset = UNSET
    invalid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        block_height = self.block_height

        slot = self.slot

        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)

        outputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = []
            for outputs_item_data in self.outputs:
                outputs_item = outputs_item_data.to_dict()
                outputs.append(outputs_item)

        utxo_count = self.utxo_count

        total_output = self.total_output

        fees = self.fees

        ttl = self.ttl

        auxiliary_data_hash = self.auxiliary_data_hash

        validity_interval_start = self.validity_interval_start

        script_data_hash = self.script_data_hash

        collateral_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collateral_inputs, Unset):
            collateral_inputs = []
            for collateral_inputs_item_data in self.collateral_inputs:
                collateral_inputs_item = collateral_inputs_item_data.to_dict()
                collateral_inputs.append(collateral_inputs_item)

        required_signers: list[str] | Unset = UNSET
        if not isinstance(self.required_signers, Unset):
            required_signers = self.required_signers

        netowrk_id = self.netowrk_id

        collateral_return: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collateral_return, Unset):
            collateral_return = self.collateral_return.to_dict()

        total_collateral = self.total_collateral

        reference_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reference_inputs, Unset):
            reference_inputs = []
            for reference_inputs_item_data in self.reference_inputs:
                reference_inputs_item = reference_inputs_item_data.to_dict()
                reference_inputs.append(reference_inputs_item)

        invalid = self.invalid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if block_height is not UNSET:
            field_dict["block_height"] = block_height
        if slot is not UNSET:
            field_dict["slot"] = slot
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if utxo_count is not UNSET:
            field_dict["utxo_count"] = utxo_count
        if total_output is not UNSET:
            field_dict["total_output"] = total_output
        if fees is not UNSET:
            field_dict["fees"] = fees
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if auxiliary_data_hash is not UNSET:
            field_dict["auxiliary_data_hash"] = auxiliary_data_hash
        if validity_interval_start is not UNSET:
            field_dict["validity_interval_start"] = validity_interval_start
        if script_data_hash is not UNSET:
            field_dict["script_data_hash"] = script_data_hash
        if collateral_inputs is not UNSET:
            field_dict["collateral_inputs"] = collateral_inputs
        if required_signers is not UNSET:
            field_dict["required_signers"] = required_signers
        if netowrk_id is not UNSET:
            field_dict["netowrk_id"] = netowrk_id
        if collateral_return is not UNSET:
            field_dict["collateral_return"] = collateral_return
        if total_collateral is not UNSET:
            field_dict["total_collateral"] = total_collateral
        if reference_inputs is not UNSET:
            field_dict["reference_inputs"] = reference_inputs
        if invalid is not UNSET:
            field_dict["invalid"] = invalid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tx_ouput import TxOuput
        from ..models.tx_utxo import TxUtxo

        d = dict(src_dict)
        hash_ = d.pop("hash", UNSET)

        block_height = d.pop("block_height", UNSET)

        slot = d.pop("slot", UNSET)

        _inputs = d.pop("inputs", UNSET)
        inputs: list[TxUtxo] | Unset = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:
                inputs_item = TxUtxo.from_dict(inputs_item_data)

                inputs.append(inputs_item)

        _outputs = d.pop("outputs", UNSET)
        outputs: list[TxUtxo] | Unset = UNSET
        if _outputs is not UNSET:
            outputs = []
            for outputs_item_data in _outputs:
                outputs_item = TxUtxo.from_dict(outputs_item_data)

                outputs.append(outputs_item)

        utxo_count = d.pop("utxo_count", UNSET)

        total_output = d.pop("total_output", UNSET)

        fees = d.pop("fees", UNSET)

        ttl = d.pop("ttl", UNSET)

        auxiliary_data_hash = d.pop("auxiliary_data_hash", UNSET)

        validity_interval_start = d.pop("validity_interval_start", UNSET)

        script_data_hash = d.pop("script_data_hash", UNSET)

        _collateral_inputs = d.pop("collateral_inputs", UNSET)
        collateral_inputs: list[TxUtxo] | Unset = UNSET
        if _collateral_inputs is not UNSET:
            collateral_inputs = []
            for collateral_inputs_item_data in _collateral_inputs:
                collateral_inputs_item = TxUtxo.from_dict(collateral_inputs_item_data)

                collateral_inputs.append(collateral_inputs_item)

        required_signers = cast(list[str], d.pop("required_signers", UNSET))

        netowrk_id = d.pop("netowrk_id", UNSET)

        _collateral_return = d.pop("collateral_return", UNSET)
        collateral_return: TxOuput | Unset
        if isinstance(_collateral_return, Unset):
            collateral_return = UNSET
        else:
            collateral_return = TxOuput.from_dict(_collateral_return)

        total_collateral = d.pop("total_collateral", UNSET)

        _reference_inputs = d.pop("reference_inputs", UNSET)
        reference_inputs: list[TxUtxo] | Unset = UNSET
        if _reference_inputs is not UNSET:
            reference_inputs = []
            for reference_inputs_item_data in _reference_inputs:
                reference_inputs_item = TxUtxo.from_dict(reference_inputs_item_data)

                reference_inputs.append(reference_inputs_item)

        invalid = d.pop("invalid", UNSET)

        transaction_details = cls(
            hash_=hash_,
            block_height=block_height,
            slot=slot,
            inputs=inputs,
            outputs=outputs,
            utxo_count=utxo_count,
            total_output=total_output,
            fees=fees,
            ttl=ttl,
            auxiliary_data_hash=auxiliary_data_hash,
            validity_interval_start=validity_interval_start,
            script_data_hash=script_data_hash,
            collateral_inputs=collateral_inputs,
            required_signers=required_signers,
            netowrk_id=netowrk_id,
            collateral_return=collateral_return,
            total_collateral=total_collateral,
            reference_inputs=reference_inputs,
            invalid=invalid,
        )

        transaction_details.additional_properties = d
        return transaction_details

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
