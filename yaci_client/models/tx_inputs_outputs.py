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
    from ..models.tx_utxo import TxUtxo


T = TypeVar("T", bound="TxInputsOutputs")


@_attrs_define
class TxInputsOutputs:
    """
    Attributes:
        hash_ (Union[Unset, str]):
        inputs (Union[Unset, List['TxUtxo']]):
        outputs (Union[Unset, List['TxUtxo']]):
    """

    hash_: Union[Unset, str] = UNSET
    inputs: Union[Unset, List["TxUtxo"]] = UNSET
    outputs: Union[Unset, List["TxUtxo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        hash_ = self.hash_

        inputs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)

        outputs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = []
            for outputs_item_data in self.outputs:
                outputs_item = outputs_item_data.to_dict()
                outputs.append(outputs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if outputs is not UNSET:
            field_dict["outputs"] = outputs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tx_utxo import TxUtxo

        d = src_dict.copy()
        hash_ = d.pop("hash", UNSET)

        inputs = []
        _inputs = d.pop("inputs", UNSET)
        for inputs_item_data in _inputs or []:
            inputs_item = TxUtxo.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        outputs = []
        _outputs = d.pop("outputs", UNSET)
        for outputs_item_data in _outputs or []:
            outputs_item = TxUtxo.from_dict(outputs_item_data)

            outputs.append(outputs_item)

        tx_inputs_outputs = cls(
            hash_=hash_,
            inputs=inputs,
            outputs=outputs,
        )

        tx_inputs_outputs.additional_properties = d
        return tx_inputs_outputs

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
