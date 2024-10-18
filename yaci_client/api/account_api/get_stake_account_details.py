from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stake_account_info import StakeAccountInfo
from ...types import Response


def _get_kwargs(
    stake_address: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{stake_address}".format(
            stake_address=stake_address,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[StakeAccountInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StakeAccountInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StakeAccountInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stake_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[StakeAccountInfo]:
    """Obtain information about a specific stake account.It gets stake account balance from aggregated
    stake account balance if aggregation is enabled, otherwise it calculates the current lovelace
    balance by aggregating all current utxos for the stake addressand get rewards amount directly from
    node.

    Args:
        stake_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StakeAccountInfo]
    """

    kwargs = _get_kwargs(
        stake_address=stake_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stake_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[StakeAccountInfo]:
    """Obtain information about a specific stake account.It gets stake account balance from aggregated
    stake account balance if aggregation is enabled, otherwise it calculates the current lovelace
    balance by aggregating all current utxos for the stake addressand get rewards amount directly from
    node.

    Args:
        stake_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StakeAccountInfo
    """

    return sync_detailed(
        stake_address=stake_address,
        client=client,
    ).parsed


async def asyncio_detailed(
    stake_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[StakeAccountInfo]:
    """Obtain information about a specific stake account.It gets stake account balance from aggregated
    stake account balance if aggregation is enabled, otherwise it calculates the current lovelace
    balance by aggregating all current utxos for the stake addressand get rewards amount directly from
    node.

    Args:
        stake_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StakeAccountInfo]
    """

    kwargs = _get_kwargs(
        stake_address=stake_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stake_address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[StakeAccountInfo]:
    """Obtain information about a specific stake account.It gets stake account balance from aggregated
    stake account balance if aggregation is enabled, otherwise it calculates the current lovelace
    balance by aggregating all current utxos for the stake addressand get rewards amount directly from
    node.

    Args:
        stake_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StakeAccountInfo
    """

    return (
        await asyncio_detailed(
            stake_address=stake_address,
            client=client,
        )
    ).parsed
