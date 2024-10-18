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

T = TypeVar("T", bound="DrepVoteThresholds")


@_attrs_define
class DrepVoteThresholds:
    """
    Attributes:
        dvt_motion_no_confidence (Union[Unset, float]):
        dvt_committee_normal (Union[Unset, float]):
        dvt_committee_no_confidence (Union[Unset, float]):
        dvt_update_to_constitution (Union[Unset, float]):
        dvt_hard_fork_initiation (Union[Unset, float]):
        dvt_ppnetwork_group (Union[Unset, float]):
        dvt_ppeconomic_group (Union[Unset, float]):
        dvt_pptechnical_group (Union[Unset, float]):
        dvt_ppgov_group (Union[Unset, float]):
        dvt_treasury_withdrawal (Union[Unset, float]):
    """

    dvt_motion_no_confidence: Union[Unset, float] = UNSET
    dvt_committee_normal: Union[Unset, float] = UNSET
    dvt_committee_no_confidence: Union[Unset, float] = UNSET
    dvt_update_to_constitution: Union[Unset, float] = UNSET
    dvt_hard_fork_initiation: Union[Unset, float] = UNSET
    dvt_ppnetwork_group: Union[Unset, float] = UNSET
    dvt_ppeconomic_group: Union[Unset, float] = UNSET
    dvt_pptechnical_group: Union[Unset, float] = UNSET
    dvt_ppgov_group: Union[Unset, float] = UNSET
    dvt_treasury_withdrawal: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dvt_motion_no_confidence = self.dvt_motion_no_confidence

        dvt_committee_normal = self.dvt_committee_normal

        dvt_committee_no_confidence = self.dvt_committee_no_confidence

        dvt_update_to_constitution = self.dvt_update_to_constitution

        dvt_hard_fork_initiation = self.dvt_hard_fork_initiation

        dvt_ppnetwork_group = self.dvt_ppnetwork_group

        dvt_ppeconomic_group = self.dvt_ppeconomic_group

        dvt_pptechnical_group = self.dvt_pptechnical_group

        dvt_ppgov_group = self.dvt_ppgov_group

        dvt_treasury_withdrawal = self.dvt_treasury_withdrawal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dvt_motion_no_confidence is not UNSET:
            field_dict["dvt_motion_no_confidence"] = dvt_motion_no_confidence
        if dvt_committee_normal is not UNSET:
            field_dict["dvt_committee_normal"] = dvt_committee_normal
        if dvt_committee_no_confidence is not UNSET:
            field_dict["dvt_committee_no_confidence"] = dvt_committee_no_confidence
        if dvt_update_to_constitution is not UNSET:
            field_dict["dvt_update_to_constitution"] = dvt_update_to_constitution
        if dvt_hard_fork_initiation is not UNSET:
            field_dict["dvt_hard_fork_initiation"] = dvt_hard_fork_initiation
        if dvt_ppnetwork_group is not UNSET:
            field_dict["dvt_ppnetwork_group"] = dvt_ppnetwork_group
        if dvt_ppeconomic_group is not UNSET:
            field_dict["dvt_ppeconomic_group"] = dvt_ppeconomic_group
        if dvt_pptechnical_group is not UNSET:
            field_dict["dvt_pptechnical_group"] = dvt_pptechnical_group
        if dvt_ppgov_group is not UNSET:
            field_dict["dvt_ppgov_group"] = dvt_ppgov_group
        if dvt_treasury_withdrawal is not UNSET:
            field_dict["dvt_treasury_withdrawal"] = dvt_treasury_withdrawal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dvt_motion_no_confidence = d.pop("dvt_motion_no_confidence", UNSET)

        dvt_committee_normal = d.pop("dvt_committee_normal", UNSET)

        dvt_committee_no_confidence = d.pop("dvt_committee_no_confidence", UNSET)

        dvt_update_to_constitution = d.pop("dvt_update_to_constitution", UNSET)

        dvt_hard_fork_initiation = d.pop("dvt_hard_fork_initiation", UNSET)

        dvt_ppnetwork_group = d.pop("dvt_ppnetwork_group", UNSET)

        dvt_ppeconomic_group = d.pop("dvt_ppeconomic_group", UNSET)

        dvt_pptechnical_group = d.pop("dvt_pptechnical_group", UNSET)

        dvt_ppgov_group = d.pop("dvt_ppgov_group", UNSET)

        dvt_treasury_withdrawal = d.pop("dvt_treasury_withdrawal", UNSET)

        drep_vote_thresholds = cls(
            dvt_motion_no_confidence=dvt_motion_no_confidence,
            dvt_committee_normal=dvt_committee_normal,
            dvt_committee_no_confidence=dvt_committee_no_confidence,
            dvt_update_to_constitution=dvt_update_to_constitution,
            dvt_hard_fork_initiation=dvt_hard_fork_initiation,
            dvt_ppnetwork_group=dvt_ppnetwork_group,
            dvt_ppeconomic_group=dvt_ppeconomic_group,
            dvt_pptechnical_group=dvt_pptechnical_group,
            dvt_ppgov_group=dvt_ppgov_group,
            dvt_treasury_withdrawal=dvt_treasury_withdrawal,
        )

        drep_vote_thresholds.additional_properties = d
        return drep_vote_thresholds

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
