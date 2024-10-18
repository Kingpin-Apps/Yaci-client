from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.script_dto import ScriptDto
from ...types import Response


def _get_kwargs(
    script_hash: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/scripts/{script_hash}".format(
            script_hash=script_hash,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScriptDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ScriptDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScriptDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    script_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ScriptDto]:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScriptDto]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[ScriptDto]:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScriptDto
    """

    return sync_detailed(
        script_hash=script_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    script_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ScriptDto]:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScriptDto]
    """

    kwargs = _get_kwargs(
        script_hash=script_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    script_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ScriptDto]:
    """
    Args:
        script_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScriptDto
    """

    return (
        await asyncio_detailed(
            script_hash=script_hash,
            client=client,
        )
    ).parsed
