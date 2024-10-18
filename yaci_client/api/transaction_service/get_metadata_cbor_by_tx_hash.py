from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tx_metadata_label_cbor_dto import TxMetadataLabelCBORDto
from ...types import Response


def _get_kwargs(
    tx_hash: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/txs/{tx_hash}/metadata/cbor".format(
            tx_hash=tx_hash,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["TxMetadataLabelCBORDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TxMetadataLabelCBORDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["TxMetadataLabelCBORDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["TxMetadataLabelCBORDto"]]:
    """Transaction Metadata CBOR

     Get a list of metadata CBOR included in a specific transaction.

    Args:
        tx_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TxMetadataLabelCBORDto']]
    """

    kwargs = _get_kwargs(
        tx_hash=tx_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["TxMetadataLabelCBORDto"]]:
    """Transaction Metadata CBOR

     Get a list of metadata CBOR included in a specific transaction.

    Args:
        tx_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['TxMetadataLabelCBORDto']
    """

    return sync_detailed(
        tx_hash=tx_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["TxMetadataLabelCBORDto"]]:
    """Transaction Metadata CBOR

     Get a list of metadata CBOR included in a specific transaction.

    Args:
        tx_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TxMetadataLabelCBORDto']]
    """

    kwargs = _get_kwargs(
        tx_hash=tx_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["TxMetadataLabelCBORDto"]]:
    """Transaction Metadata CBOR

     Get a list of metadata CBOR included in a specific transaction.

    Args:
        tx_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['TxMetadataLabelCBORDto']
    """

    return (
        await asyncio_detailed(
            tx_hash=tx_hash,
            client=client,
        )
    ).parsed
