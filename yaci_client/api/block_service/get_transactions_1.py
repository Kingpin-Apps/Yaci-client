from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transaction_summary import TransactionSummary
from ...types import Response


def _get_kwargs(
    block: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/blocks/{block}/txs",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[TransactionSummary] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TransactionSummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TransactionSummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    block: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[TransactionSummary]]:
    """Block Transactions

     Get a list of all transactions included in the provided block.

    Args:
        block (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TransactionSummary]]
    """

    kwargs = _get_kwargs(
        block=block,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    block: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[TransactionSummary] | None:
    """Block Transactions

     Get a list of all transactions included in the provided block.

    Args:
        block (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TransactionSummary]
    """

    return sync_detailed(
        block=block,
        client=client,
    ).parsed


async def asyncio_detailed(
    block: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[TransactionSummary]]:
    """Block Transactions

     Get a list of all transactions included in the provided block.

    Args:
        block (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TransactionSummary]]
    """

    kwargs = _get_kwargs(
        block=block,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    block: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[TransactionSummary] | None:
    """Block Transactions

     Get a list of all transactions included in the provided block.

    Args:
        block (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TransactionSummary]
    """

    return (
        await asyncio_detailed(
            block=block,
            client=client,
        )
    ).parsed
