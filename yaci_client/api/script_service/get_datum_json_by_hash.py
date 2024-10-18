from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.json_node import JsonNode
from ...types import Response


def _get_kwargs(
    datum_hash: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/scripts/datum/{datum_hash}".format(
            datum_hash=datum_hash,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[JsonNode]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JsonNode.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[JsonNode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datum_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[JsonNode]:
    """
    Args:
        datum_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonNode]
    """

    kwargs = _get_kwargs(
        datum_hash=datum_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datum_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[JsonNode]:
    """
    Args:
        datum_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsonNode
    """

    return sync_detailed(
        datum_hash=datum_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    datum_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[JsonNode]:
    """
    Args:
        datum_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonNode]
    """

    kwargs = _get_kwargs(
        datum_hash=datum_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datum_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[JsonNode]:
    """
    Args:
        datum_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsonNode
    """

    return (
        await asyncio_detailed(
            datum_hash=datum_hash,
            client=client,
        )
    ).parsed
