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
    from ..models.epoch import Epoch


T = TypeVar("T", bound="EpochsPage")


@_attrs_define
class EpochsPage:
    """
    Attributes:
        total (Union[Unset, int]):
        total_pages (Union[Unset, int]):
        epochs (Union[Unset, List['Epoch']]):
    """

    total: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    epochs: Union[Unset, List["Epoch"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        total = self.total

        total_pages = self.total_pages

        epochs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.epochs, Unset):
            epochs = []
            for epochs_item_data in self.epochs:
                epochs_item = epochs_item_data.to_dict()
                epochs.append(epochs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if epochs is not UNSET:
            field_dict["epochs"] = epochs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.epoch import Epoch

        d = src_dict.copy()
        total = d.pop("total", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        epochs = []
        _epochs = d.pop("epochs", UNSET)
        for epochs_item_data in _epochs or []:
            epochs_item = Epoch.from_dict(epochs_item_data)

            epochs.append(epochs_item)

        epochs_page = cls(
            total=total,
            total_pages=total_pages,
            epochs=epochs,
        )

        epochs_page.additional_properties = d
        return epochs_page

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
