from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tx_asset_mint_type import TxAssetMintType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TxAsset")


@_attrs_define
class TxAsset:
    """
    Attributes:
        block_number (Union[Unset, int]):
        block_time (Union[Unset, int]):
        slot (Union[Unset, int]):
        tx_hash (Union[Unset, str]):
        policy (Union[Unset, str]):
        asset_name (Union[Unset, str]):
        unit (Union[Unset, str]):
        fingerprint (Union[Unset, str]):
        quantity (Union[Unset, int]):
        mint_type (Union[Unset, TxAssetMintType]):
    """

    block_number: Union[Unset, int] = UNSET
    block_time: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    policy: Union[Unset, str] = UNSET
    asset_name: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    mint_type: Union[Unset, TxAssetMintType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_number = self.block_number

        block_time = self.block_time

        slot = self.slot

        tx_hash = self.tx_hash

        policy = self.policy

        asset_name = self.asset_name

        unit = self.unit

        fingerprint = self.fingerprint

        quantity = self.quantity

        mint_type: Union[Unset, str] = UNSET
        if not isinstance(self.mint_type, Unset):
            mint_type = self.mint_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_number is not UNSET:
            field_dict["block_number"] = block_number
        if block_time is not UNSET:
            field_dict["block_time"] = block_time
        if slot is not UNSET:
            field_dict["slot"] = slot
        if tx_hash is not UNSET:
            field_dict["tx_hash"] = tx_hash
        if policy is not UNSET:
            field_dict["policy"] = policy
        if asset_name is not UNSET:
            field_dict["asset_name"] = asset_name
        if unit is not UNSET:
            field_dict["unit"] = unit
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if mint_type is not UNSET:
            field_dict["mint_type"] = mint_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        block_number = d.pop("block_number", UNSET)

        block_time = d.pop("block_time", UNSET)

        slot = d.pop("slot", UNSET)

        tx_hash = d.pop("tx_hash", UNSET)

        policy = d.pop("policy", UNSET)

        asset_name = d.pop("asset_name", UNSET)

        unit = d.pop("unit", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        quantity = d.pop("quantity", UNSET)

        _mint_type = d.pop("mint_type", UNSET)
        mint_type: Union[Unset, TxAssetMintType]
        if isinstance(_mint_type, Unset):
            mint_type = UNSET
        else:
            mint_type = TxAssetMintType(_mint_type)

        tx_asset = cls(
            block_number=block_number,
            block_time=block_time,
            slot=slot,
            tx_hash=tx_hash,
            policy=policy,
            asset_name=asset_name,
            unit=unit,
            fingerprint=fingerprint,
            quantity=quantity,
            mint_type=mint_type,
        )

        tx_asset.additional_properties = d
        return tx_asset

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
