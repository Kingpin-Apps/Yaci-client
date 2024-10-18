from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_balance_dto import AddressBalanceDto
from ...types import Response


def _get_kwargs(
    address: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/addresses/{address}/balance".format(
            address=address,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddressBalanceDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AddressBalanceDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddressBalanceDto]:
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
) -> Response[AddressBalanceDto]:
    """Get current balance at an address

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressBalanceDto]
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
) -> Optional[AddressBalanceDto]:
    """Get current balance at an address

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressBalanceDto
    """

    return sync_detailed(
        address=address,
        client=client,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AddressBalanceDto]:
    """Get current balance at an address

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressBalanceDto]
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
) -> Optional[AddressBalanceDto]:
    """Get current balance at an address

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressBalanceDto
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
        )
    ).parsed
