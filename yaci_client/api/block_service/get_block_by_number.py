from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block_dto import BlockDto
from ...types import Response


def _get_kwargs(
    number_or_hash: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/blocks/{number_or_hash}".format(
            number_or_hash=number_or_hash,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BlockDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BlockDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BlockDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    number_or_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[BlockDto]:
    """Block Information by Number or Hash

     Get block information by number or hash.

    Args:
        number_or_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockDto]
    """

    kwargs = _get_kwargs(
        number_or_hash=number_or_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    number_or_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BlockDto]:
    """Block Information by Number or Hash

     Get block information by number or hash.

    Args:
        number_or_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockDto
    """

    return sync_detailed(
        number_or_hash=number_or_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    number_or_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[BlockDto]:
    """Block Information by Number or Hash

     Get block information by number or hash.

    Args:
        number_or_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockDto]
    """

    kwargs = _get_kwargs(
        number_or_hash=number_or_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    number_or_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BlockDto]:
    """Block Information by Number or Hash

     Get block information by number or hash.

    Args:
        number_or_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockDto
    """

    return (
        await asyncio_detailed(
            number_or_hash=number_or_hash,
            client=client,
        )
    ).parsed
