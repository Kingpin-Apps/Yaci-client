from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tx_asset import TxAsset
from ...types import UNSET, Response, Unset


def _get_kwargs(
    policy_id: str,
    *,
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/assets/policy/{policy_id}".format(
            policy_id=policy_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["TxAsset"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TxAsset.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["TxAsset"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Response[List["TxAsset"]]:
    """Asset History by Policy

     Returns the Mint / Burn History for all assets included in a policy.

    Args:
        policy_id (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TxAsset']]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        page=page,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Optional[List["TxAsset"]]:
    """Asset History by Policy

     Returns the Mint / Burn History for all assets included in a policy.

    Args:
        policy_id (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['TxAsset']
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        page=page,
        count=count,
    ).parsed


async def asyncio_detailed(
    policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Response[List["TxAsset"]]:
    """Asset History by Policy

     Returns the Mint / Burn History for all assets included in a policy.

    Args:
        policy_id (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TxAsset']]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        page=page,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Optional[List["TxAsset"]]:
    """Asset History by Policy

     Returns the Mint / Burn History for all assets included in a policy.

    Args:
        policy_id (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['TxAsset']
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            page=page,
            count=count,
        )
    ).parsed
