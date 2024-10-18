from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_asset_balance_dto import AddressAssetBalanceDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    unit: str,
    *,
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    sort: Union[Unset, str] = "asc",
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/assets/{unit}/addresses".format(
            unit=unit,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AddressAssetBalanceDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AddressAssetBalanceDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AddressAssetBalanceDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    sort: Union[Unset, str] = "asc",
) -> Response[List["AddressAssetBalanceDto"]]:
    """Get addresses by asset

    Args:
        unit (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, str]):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AddressAssetBalanceDto']]
    """

    kwargs = _get_kwargs(
        unit=unit,
        page=page,
        count=count,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    sort: Union[Unset, str] = "asc",
) -> Optional[List["AddressAssetBalanceDto"]]:
    """Get addresses by asset

    Args:
        unit (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, str]):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AddressAssetBalanceDto']
    """

    return sync_detailed(
        unit=unit,
        client=client,
        page=page,
        count=count,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    sort: Union[Unset, str] = "asc",
) -> Response[List["AddressAssetBalanceDto"]]:
    """Get addresses by asset

    Args:
        unit (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, str]):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AddressAssetBalanceDto']]
    """

    kwargs = _get_kwargs(
        unit=unit,
        page=page,
        count=count,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    sort: Union[Unset, str] = "asc",
) -> Optional[List["AddressAssetBalanceDto"]]:
    """Get addresses by asset

    Args:
        unit (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        sort (Union[Unset, str]):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AddressAssetBalanceDto']
    """

    return (
        await asyncio_detailed(
            unit=unit,
            client=client,
            page=page,
            count=count,
            sort=sort,
        )
    ).parsed
