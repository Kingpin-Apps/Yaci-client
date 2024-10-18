from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.amount import Amount
from ...types import Response


def _get_kwargs(
    address: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/addresses/{address}/amounts".format(
            address=address,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Amount"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Amount.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Amount"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["Amount"]]:
    """Get amounts at an address. For stake address, only lovelace is returned.It calculates the current
    balance at the address by aggregating all currrent utxos for the stake address. It may be slow for
    addresses with too many utxos.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Amount']]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["Amount"]]:
    """Get amounts at an address. For stake address, only lovelace is returned.It calculates the current
    balance at the address by aggregating all currrent utxos for the stake address. It may be slow for
    addresses with too many utxos.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Amount']
    """

    return sync_detailed(
        address=address,
        client=client,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["Amount"]]:
    """Get amounts at an address. For stake address, only lovelace is returned.It calculates the current
    balance at the address by aggregating all currrent utxos for the stake address. It may be slow for
    addresses with too many utxos.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Amount']]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["Amount"]]:
    """Get amounts at an address. For stake address, only lovelace is returned.It calculates the current
    balance at the address by aggregating all currrent utxos for the stake address. It may be slow for
    addresses with too many utxos.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Amount']
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
        )
    ).parsed
