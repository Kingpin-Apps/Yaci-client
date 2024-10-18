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
    from ..models.block_summary import BlockSummary


T = TypeVar("T", bound="BlocksPage")


@_attrs_define
class BlocksPage:
    """
    Attributes:
        total (Union[Unset, int]):
        total_pages (Union[Unset, int]):
        blocks (Union[Unset, List['BlockSummary']]):
    """

    total: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    blocks: Union[Unset, List["BlockSummary"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        total = self.total

        total_pages = self.total_pages

        blocks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.blocks, Unset):
            blocks = []
            for blocks_item_data in self.blocks:
                blocks_item = blocks_item_data.to_dict()
                blocks.append(blocks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if blocks is not UNSET:
            field_dict["blocks"] = blocks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.block_summary import BlockSummary

        d = src_dict.copy()
        total = d.pop("total", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        blocks = []
        _blocks = d.pop("blocks", UNSET)
        for blocks_item_data in _blocks or []:
            blocks_item = BlockSummary.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        blocks_page = cls(
            total=total,
            total_pages=total_pages,
            blocks=blocks,
        )

        blocks_page.additional_properties = d
        return blocks_page

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
