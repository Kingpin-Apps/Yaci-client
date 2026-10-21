from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.script_detail_dto import ScriptDetailDto
from ...types import Response


def _get_kwargs(
    script_hash: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/scripts/{script_hash}/details",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ScriptDetailDto | None:
    if response.status_code == 200:
        response_200 = ScriptDetailDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ScriptDetailDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    script_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ScriptDetailDto]:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScriptDetailDto]
    """

    kwargs = _get_kwargs(
        script_hash=script_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    script_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> ScriptDetailDto | None:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScriptDetailDto
    """

    return sync_detailed(
        script_hash=script_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    script_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ScriptDetailDto]:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScriptDetailDto]
    """

    kwargs = _get_kwargs(
        script_hash=script_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    script_hash: str,
    *,
    client: AuthenticatedClient | Client,
) -> ScriptDetailDto | None:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScriptDetailDto
    """

    return (
        await asyncio_detailed(
            script_hash=script_hash,
            client=client,
        )
    ).parsed
