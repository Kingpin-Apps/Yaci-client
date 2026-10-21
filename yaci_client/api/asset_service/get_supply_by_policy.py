from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy_supply import PolicySupply
from ...types import Response


def _get_kwargs(
    policy: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/assets/supply/policy/{policy}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PolicySupply | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = PolicySupply.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PolicySupply]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PolicySupply]:
    """Assets Supply by Policy

     Returns the entire assets supply of a specific policy.

    Args:
        policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicySupply]
    """

    kwargs = _get_kwargs(
        policy=policy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> PolicySupply | None:
    """Assets Supply by Policy

     Returns the entire assets supply of a specific policy.

    Args:
        policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicySupply
    """

    return sync_detailed(
        policy=policy,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PolicySupply]:
    """Assets Supply by Policy

     Returns the entire assets supply of a specific policy.

    Args:
        policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicySupply]
    """

    kwargs = _get_kwargs(
        policy=policy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy: str,
    *,
    client: AuthenticatedClient | Client,
) -> PolicySupply | None:
    """Assets Supply by Policy

     Returns the entire assets supply of a specific policy.

    Args:
        policy (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicySupply
    """

    return (
        await asyncio_detailed(
            policy=policy,
            client=client,
        )
    ).parsed
