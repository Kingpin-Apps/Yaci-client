from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stake_address_balance import StakeAddressBalance
from ...types import Response


def _get_kwargs(
    stake_address: str,
    time_in_sec: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{stake_address}/{time_in_sec}/balance",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StakeAddressBalance | None:
    if response.status_code == 200:
        response_200 = StakeAddressBalance.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StakeAddressBalance]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stake_address: str,
    time_in_sec: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[StakeAddressBalance]:
    """Get current balance at a stake address at a specific time. This is an experimental feature.

    Args:
        stake_address (str):
        time_in_sec (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StakeAddressBalance]
    """

    kwargs = _get_kwargs(
        stake_address=stake_address,
        time_in_sec=time_in_sec,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stake_address: str,
    time_in_sec: int,
    *,
    client: AuthenticatedClient | Client,
) -> StakeAddressBalance | None:
    """Get current balance at a stake address at a specific time. This is an experimental feature.

    Args:
        stake_address (str):
        time_in_sec (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StakeAddressBalance
    """

    return sync_detailed(
        stake_address=stake_address,
        time_in_sec=time_in_sec,
        client=client,
    ).parsed


async def asyncio_detailed(
    stake_address: str,
    time_in_sec: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[StakeAddressBalance]:
    """Get current balance at a stake address at a specific time. This is an experimental feature.

    Args:
        stake_address (str):
        time_in_sec (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StakeAddressBalance]
    """

    kwargs = _get_kwargs(
        stake_address=stake_address,
        time_in_sec=time_in_sec,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stake_address: str,
    time_in_sec: int,
    *,
    client: AuthenticatedClient | Client,
) -> StakeAddressBalance | None:
    """Get current balance at a stake address at a specific time. This is an experimental feature.

    Args:
        stake_address (str):
        time_in_sec (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StakeAddressBalance
    """

    return (
        await asyncio_detailed(
            stake_address=stake_address,
            time_in_sec=time_in_sec,
            client=client,
        )
    ).parsed
