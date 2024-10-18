from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unit_supply import UnitSupply
from ...types import Response


def _get_kwargs(
    unit: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/assets/supply/unit/{unit}".format(
            unit=unit,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UnitSupply]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UnitSupply.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UnitSupply]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[UnitSupply]:
    """Assets Supply by Unit

     Returns the entire supply of a specific asset by unit.

    Args:
        unit (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnitSupply]
    """

    kwargs = _get_kwargs(
        unit=unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UnitSupply]:
    """Assets Supply by Unit

     Returns the entire supply of a specific asset by unit.

    Args:
        unit (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnitSupply
    """

    return sync_detailed(
        unit=unit,
        client=client,
    ).parsed


async def asyncio_detailed(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[UnitSupply]:
    """Assets Supply by Unit

     Returns the entire supply of a specific asset by unit.

    Args:
        unit (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnitSupply]
    """

    kwargs = _get_kwargs(
        unit=unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unit: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UnitSupply]:
    """Assets Supply by Unit

     Returns the entire supply of a specific asset by unit.

    Args:
        unit (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnitSupply
    """

    return (
        await asyncio_detailed(
            unit=unit,
            client=client,
        )
    ).parsed
