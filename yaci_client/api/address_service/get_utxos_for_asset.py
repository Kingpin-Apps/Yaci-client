from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_utxos_for_asset_order import GetUtxosForAssetOrder
from ...models.utxo import Utxo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    address: str,
    asset: str,
    *,
    count: int | Unset = 10,
    page: int | Unset = 0,
    order: GetUtxosForAssetOrder | Unset = GetUtxosForAssetOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["count"] = count

    params["page"] = page

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/addresses/{address}/utxos/{asset}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Utxo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Utxo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Utxo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    asset: str,
    *,
    client: AuthenticatedClient | Client,
    count: int | Unset = 10,
    page: int | Unset = 0,
    order: GetUtxosForAssetOrder | Unset = GetUtxosForAssetOrder.ASC,
) -> Response[list[Utxo]]:
    """Get UTxOs for an address or address verification key hash (addr_vkh) for a specific asset. If the
    address is a stake address, it will return UTXOs for all base addresses associated with the stake
    address

    Args:
        address (str):
        asset (str):
        count (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        order (GetUtxosForAssetOrder | Unset):  Default: GetUtxosForAssetOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Utxo]]
    """

    kwargs = _get_kwargs(
        address=address,
        asset=asset,
        count=count,
        page=page,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    asset: str,
    *,
    client: AuthenticatedClient | Client,
    count: int | Unset = 10,
    page: int | Unset = 0,
    order: GetUtxosForAssetOrder | Unset = GetUtxosForAssetOrder.ASC,
) -> list[Utxo] | None:
    """Get UTxOs for an address or address verification key hash (addr_vkh) for a specific asset. If the
    address is a stake address, it will return UTXOs for all base addresses associated with the stake
    address

    Args:
        address (str):
        asset (str):
        count (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        order (GetUtxosForAssetOrder | Unset):  Default: GetUtxosForAssetOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Utxo]
    """

    return sync_detailed(
        address=address,
        asset=asset,
        client=client,
        count=count,
        page=page,
        order=order,
    ).parsed


async def asyncio_detailed(
    address: str,
    asset: str,
    *,
    client: AuthenticatedClient | Client,
    count: int | Unset = 10,
    page: int | Unset = 0,
    order: GetUtxosForAssetOrder | Unset = GetUtxosForAssetOrder.ASC,
) -> Response[list[Utxo]]:
    """Get UTxOs for an address or address verification key hash (addr_vkh) for a specific asset. If the
    address is a stake address, it will return UTXOs for all base addresses associated with the stake
    address

    Args:
        address (str):
        asset (str):
        count (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        order (GetUtxosForAssetOrder | Unset):  Default: GetUtxosForAssetOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Utxo]]
    """

    kwargs = _get_kwargs(
        address=address,
        asset=asset,
        count=count,
        page=page,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    asset: str,
    *,
    client: AuthenticatedClient | Client,
    count: int | Unset = 10,
    page: int | Unset = 0,
    order: GetUtxosForAssetOrder | Unset = GetUtxosForAssetOrder.ASC,
) -> list[Utxo] | None:
    """Get UTxOs for an address or address verification key hash (addr_vkh) for a specific asset. If the
    address is a stake address, it will return UTXOs for all base addresses associated with the stake
    address

    Args:
        address (str):
        asset (str):
        count (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        order (GetUtxosForAssetOrder | Unset):  Default: GetUtxosForAssetOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Utxo]
    """

    return (
        await asyncio_detailed(
            address=address,
            asset=asset,
            client=client,
            count=count,
            page=page,
            order=order,
        )
    ).parsed
