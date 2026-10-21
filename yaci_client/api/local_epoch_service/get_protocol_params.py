from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.protocol_params_dto import ProtocolParamsDto
from ...types import Response


def _get_kwargs(
    number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/epochs/{number}/parameters",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProtocolParamsDto | None:
    if response.status_code == 200:
        response_200 = ProtocolParamsDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProtocolParamsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    number: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProtocolParamsDto]:
    """Get protocol parameters for an epoch if exists. It fetches the protocol parameters from the local
    node through n2c local query. If the protocol param doesn't exist for an old epoch, it return status
    code 404.

    Args:
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProtocolParamsDto]
    """

    kwargs = _get_kwargs(
        number=number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    number: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProtocolParamsDto | None:
    """Get protocol parameters for an epoch if exists. It fetches the protocol parameters from the local
    node through n2c local query. If the protocol param doesn't exist for an old epoch, it return status
    code 404.

    Args:
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProtocolParamsDto
    """

    return sync_detailed(
        number=number,
        client=client,
    ).parsed


async def asyncio_detailed(
    number: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProtocolParamsDto]:
    """Get protocol parameters for an epoch if exists. It fetches the protocol parameters from the local
    node through n2c local query. If the protocol param doesn't exist for an old epoch, it return status
    code 404.

    Args:
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProtocolParamsDto]
    """

    kwargs = _get_kwargs(
        number=number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    number: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProtocolParamsDto | None:
    """Get protocol parameters for an epoch if exists. It fetches the protocol parameters from the local
    node through n2c local query. If the protocol param doesn't exist for an old epoch, it return status
    code 404.

    Args:
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProtocolParamsDto
    """

    return (
        await asyncio_detailed(
            number=number,
            client=client,
        )
    ).parsed
