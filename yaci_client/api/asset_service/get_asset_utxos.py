from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_asset_utxos_order import GetAssetUtxosOrder
from ...models.utxo import Utxo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    unit: str,
    *,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetAssetUtxosOrder | Unset = GetAssetUtxosOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/assets/utxos/unit/{unit}",
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
    unit: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetAssetUtxosOrder | Unset = GetAssetUtxosOrder.ASC,
) -> Response[list[Utxo]]:
    """Asset UTxOs by Unit

     Get all UTxOs information of an asset.

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetAssetUtxosOrder | Unset):  Default: GetAssetUtxosOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Utxo]]
    """

    kwargs = _get_kwargs(
        unit=unit,
        page=page,
        count=count,
        order=order,
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
    order: GetAssetUtxosOrder | Unset = GetAssetUtxosOrder.ASC,
) -> list[Utxo] | None:
    """Asset UTxOs by Unit

     Get all UTxOs information of an asset.

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetAssetUtxosOrder | Unset):  Default: GetAssetUtxosOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Utxo]
    """

    return sync_detailed(
        unit=unit,
        client=client,
        page=page,
        count=count,
        order=order,
    ).parsed


async def asyncio_detailed(
    unit: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetAssetUtxosOrder | Unset = GetAssetUtxosOrder.ASC,
) -> Response[list[Utxo]]:
    """Asset UTxOs by Unit

     Get all UTxOs information of an asset.

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetAssetUtxosOrder | Unset):  Default: GetAssetUtxosOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Utxo]]
    """

    kwargs = _get_kwargs(
        unit=unit,
        page=page,
        count=count,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unit: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetAssetUtxosOrder | Unset = GetAssetUtxosOrder.ASC,
) -> list[Utxo] | None:
    """Asset UTxOs by Unit

     Get all UTxOs information of an asset.

    Args:
        unit (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetAssetUtxosOrder | Unset):  Default: GetAssetUtxosOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Utxo]
    """

    return (
        await asyncio_detailed(
            unit=unit,
            client=client,
            page=page,
            count=count,
            order=order,
        )
    ).parsed
