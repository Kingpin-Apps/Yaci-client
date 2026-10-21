from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_asset_balance_dto import AddressAssetBalanceDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    unit: str,
    *,
    page: int | Unset = 0,
    count: int | Unset = 10,
    sort: str | Unset = "asc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/assets/{unit}/addresses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[AddressAssetBalanceDto] | None:
    if response.status_code == 200:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[AddressAssetBalanceDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    unit: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    sort: str | Unset = "asc",
) -> Response[list[AddressAssetBalanceDto]]:
    """Get addresses by asset

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        sort (str | Unset):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AddressAssetBalanceDto]]
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
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    sort: str | Unset = "asc",
) -> list[AddressAssetBalanceDto] | None:
    """Get addresses by asset

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        sort (str | Unset):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AddressAssetBalanceDto]
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
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    sort: str | Unset = "asc",
) -> Response[list[AddressAssetBalanceDto]]:
    """Get addresses by asset

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        sort (str | Unset):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AddressAssetBalanceDto]]
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
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    sort: str | Unset = "asc",
) -> list[AddressAssetBalanceDto] | None:
    """Get addresses by asset

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        sort (str | Unset):  Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AddressAssetBalanceDto]
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
