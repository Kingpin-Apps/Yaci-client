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

T = TypeVar("T", bound="PoolVotingThresholds")


@_attrs_define
class PoolVotingThresholds:
    """
    Attributes:
        pvt_motion_no_confidence (Union[Unset, float]):
        pvt_committee_normal (Union[Unset, float]):
        pvt_committee_no_confidence (Union[Unset, float]):
        pvt_hard_fork_initiation (Union[Unset, float]):
        pvt_ppsecurity_group (Union[Unset, float]):
    """

    pvt_motion_no_confidence: Union[Unset, float] = UNSET
    pvt_committee_normal: Union[Unset, float] = UNSET
    pvt_committee_no_confidence: Union[Unset, float] = UNSET
    pvt_hard_fork_initiation: Union[Unset, float] = UNSET
    pvt_ppsecurity_group: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pvt_motion_no_confidence = self.pvt_motion_no_confidence

        pvt_committee_normal = self.pvt_committee_normal

        pvt_committee_no_confidence = self.pvt_committee_no_confidence

        pvt_hard_fork_initiation = self.pvt_hard_fork_initiation

        pvt_ppsecurity_group = self.pvt_ppsecurity_group

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pvt_motion_no_confidence is not UNSET:
            field_dict["pvt_motion_no_confidence"] = pvt_motion_no_confidence
        if pvt_committee_normal is not UNSET:
            field_dict["pvt_committee_normal"] = pvt_committee_normal
        if pvt_committee_no_confidence is not UNSET:
            field_dict["pvt_committee_no_confidence"] = pvt_committee_no_confidence
        if pvt_hard_fork_initiation is not UNSET:
            field_dict["pvt_hard_fork_initiation"] = pvt_hard_fork_initiation
        if pvt_ppsecurity_group is not UNSET:
            field_dict["pvt_ppsecurity_group"] = pvt_ppsecurity_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pvt_motion_no_confidence = d.pop("pvt_motion_no_confidence", UNSET)

        pvt_committee_normal = d.pop("pvt_committee_normal", UNSET)

        pvt_committee_no_confidence = d.pop("pvt_committee_no_confidence", UNSET)

        pvt_hard_fork_initiation = d.pop("pvt_hard_fork_initiation", UNSET)

        pvt_ppsecurity_group = d.pop("pvt_ppsecurity_group", UNSET)

        pool_voting_thresholds = cls(
            pvt_motion_no_confidence=pvt_motion_no_confidence,
            pvt_committee_normal=pvt_committee_normal,
            pvt_committee_no_confidence=pvt_committee_no_confidence,
            pvt_hard_fork_initiation=pvt_hard_fork_initiation,
            pvt_ppsecurity_group=pvt_ppsecurity_group,
        )

        pool_voting_thresholds.additional_properties = d
        return pool_voting_thresholds

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
