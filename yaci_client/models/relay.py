from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Relay")


@_attrs_define
class Relay:
    """
    Attributes:
        port (int | Unset):
        ipv4 (str | Unset):
        ipv6 (str | Unset):
        dns_name (str | Unset):
    """

    port: int | Unset = UNSET
    ipv4: str | Unset = UNSET
    ipv6: str | Unset = UNSET
    dns_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        ipv4 = self.ipv4

        ipv6 = self.ipv6

        dns_name = self.dns_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if ipv4 is not UNSET:
            field_dict["ipv4"] = ipv4
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if dns_name is not UNSET:
            field_dict["dnsName"] = dns_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        ipv4 = d.pop("ipv4", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        dns_name = d.pop("dnsName", UNSET)

        relay = cls(
            port=port,
            ipv4=ipv4,
            ipv6=ipv6,
            dns_name=dns_name,
        )

        relay.additional_properties = d
        return relay

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
