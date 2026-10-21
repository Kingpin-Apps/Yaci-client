from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fingerprint_supply import FingerprintSupply
from ...types import Response


def _get_kwargs(
    fingerprint: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/assets/supply/fingerprint/{fingerprint}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FingerprintSupply | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = FingerprintSupply.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FingerprintSupply]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FingerprintSupply]:
    """Assets Supply by Fingerprint

     Returns the entire supply of a specific asset by fingerprint.

    Args:
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FingerprintSupply]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
) -> FingerprintSupply | None:
    """Assets Supply by Fingerprint

     Returns the entire supply of a specific asset by fingerprint.

    Args:
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FingerprintSupply
    """

    return sync_detailed(
        fingerprint=fingerprint,
        client=client,
    ).parsed


async def asyncio_detailed(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FingerprintSupply]:
    """Assets Supply by Fingerprint

     Returns the entire supply of a specific asset by fingerprint.

    Args:
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FingerprintSupply]
    """

    kwargs = _get_kwargs(
        fingerprint=fingerprint,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fingerprint: str,
    *,
    client: AuthenticatedClient | Client,
) -> FingerprintSupply | None:
    """Assets Supply by Fingerprint

     Returns the entire supply of a specific asset by fingerprint.

    Args:
        fingerprint (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FingerprintSupply
    """

    return (
        await asyncio_detailed(
            fingerprint=fingerprint,
            client=client,
        )
    ).parsed
