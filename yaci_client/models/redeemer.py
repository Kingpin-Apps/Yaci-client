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

from ..models.redeemer_tag import RedeemerTag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ex_units import ExUnits


T = TypeVar("T", bound="Redeemer")


@_attrs_define
class Redeemer:
    """
    Attributes:
        tag (Union[Unset, RedeemerTag]):
        index (Union[Unset, int]):
        data (Union[Unset, str]):
        ex_units (Union[Unset, ExUnits]):
    """

    tag: Union[Unset, RedeemerTag] = UNSET
    index: Union[Unset, int] = UNSET
    data: Union[Unset, str] = UNSET
    ex_units: Union[Unset, "ExUnits"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        tag: Union[Unset, str] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.value

        index = self.index

        data = self.data

        ex_units: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ex_units, Unset):
            ex_units = self.ex_units.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag
        if index is not UNSET:
            field_dict["index"] = index
        if data is not UNSET:
            field_dict["data"] = data
        if ex_units is not UNSET:
            field_dict["ex_units"] = ex_units

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ex_units import ExUnits

        d = src_dict.copy()
        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, RedeemerTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = RedeemerTag(_tag)

        index = d.pop("index", UNSET)

        data = d.pop("data", UNSET)

        _ex_units = d.pop("ex_units", UNSET)
        ex_units: Union[Unset, ExUnits]
        if isinstance(_ex_units, Unset):
            ex_units = UNSET
        else:
            ex_units = ExUnits.from_dict(_ex_units)

        redeemer = cls(
            tag=tag,
            index=index,
            data=data,
            ex_units=ex_units,
        )

        redeemer.additional_properties = d
        return redeemer

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
