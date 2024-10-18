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

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicySupply")


@_attrs_define
class PolicySupply:
    """
    Attributes:
        policy (Union[Unset, str]):
        supply (Union[Unset, int]):
    """

    policy: Union[Unset, str] = UNSET
    supply: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        policy = self.policy

        supply = self.supply

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if supply is not UNSET:
            field_dict["supply"] = supply

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        policy = d.pop("policy", UNSET)

        supply = d.pop("supply", UNSET)

        policy_supply = cls(
            policy=policy,
            supply=supply,
        )

        policy_supply.additional_properties = d
        return policy_supply

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
