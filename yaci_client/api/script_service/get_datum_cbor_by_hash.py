from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.json_node import JsonNode
from ...types import Response


def _get_kwargs(
    datum_hash: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/scripts/datum/{datum_hash}/cbor",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> JsonNode | None:
    if response.status_code == 200:
        response_200 = JsonNode.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[JsonNode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datum_hash: str,
    *,
    client: AuthenticatedClient | Client,
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
    client: AuthenticatedClient | Client,
) -> JsonNode | None:
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
    client: AuthenticatedClient | Client,
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
    client: AuthenticatedClient | Client,
) -> JsonNode | None:
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
