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
    from ..models.transaction_summary import TransactionSummary


T = TypeVar("T", bound="TransactionPage")


@_attrs_define
class TransactionPage:
    """
    Attributes:
        total (Union[Unset, int]):
        total_pages (Union[Unset, int]):
        transaction_summaries (Union[Unset, List['TransactionSummary']]):
    """

    total: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    transaction_summaries: Union[Unset, List["TransactionSummary"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        total = self.total

        total_pages = self.total_pages

        transaction_summaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transaction_summaries, Unset):
            transaction_summaries = []
            for transaction_summaries_item_data in self.transaction_summaries:
                transaction_summaries_item = transaction_summaries_item_data.to_dict()
                transaction_summaries.append(transaction_summaries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if transaction_summaries is not UNSET:
            field_dict["transaction_summaries"] = transaction_summaries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transaction_summary import TransactionSummary

        d = src_dict.copy()
        total = d.pop("total", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        transaction_summaries = []
        _transaction_summaries = d.pop("transaction_summaries", UNSET)
        for transaction_summaries_item_data in _transaction_summaries or []:
            transaction_summaries_item = TransactionSummary.from_dict(
                transaction_summaries_item_data
            )

            transaction_summaries.append(transaction_summaries_item)

        transaction_page = cls(
            total=total,
            total_pages=total_pages,
            transaction_summaries=transaction_summaries,
        )

        transaction_page.additional_properties = d
        return transaction_page

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
