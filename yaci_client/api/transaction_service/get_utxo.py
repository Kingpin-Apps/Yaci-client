from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_utxo import AddressUtxo
from ...types import Response


def _get_kwargs(
    tx_hash: str,
    index: int,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/utxos/{tx_hash}/{index}".format(
            tx_hash=tx_hash,
            index=index,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddressUtxo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AddressUtxo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddressUtxo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tx_hash: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AddressUtxo]:
    """
    Args:
        tx_hash (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressUtxo]
    """

    kwargs = _get_kwargs(
        tx_hash=tx_hash,
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tx_hash: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AddressUtxo]:
    """
    Args:
        tx_hash (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressUtxo
    """

    return sync_detailed(
        tx_hash=tx_hash,
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    tx_hash: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AddressUtxo]:
    """
    Args:
        tx_hash (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressUtxo]
    """

    kwargs = _get_kwargs(
        tx_hash=tx_hash,
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tx_hash: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AddressUtxo]:
    """
    Args:
        tx_hash (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressUtxo
    """

    return (
        await asyncio_detailed(
            tx_hash=tx_hash,
            index=index,
            client=client,
        )
    ).parsed
