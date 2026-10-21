from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.d_rep_registration import DRepRegistration
from ...models.get_d_rep_registrations_order import GetDRepRegistrationsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetDRepRegistrationsOrder | Unset = GetDRepRegistrationsOrder.DESC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/governance/dreps/registrations",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[DRepRegistration] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DRepRegistration.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[DRepRegistration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetDRepRegistrationsOrder | Unset = GetDRepRegistrationsOrder.DESC,
) -> Response[list[DRepRegistration]]:
    """Get dRep registrations by page number and count

    Args:
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetDRepRegistrationsOrder | Unset):  Default: GetDRepRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DRepRegistration]]
    """

    kwargs = _get_kwargs(
        page=page,
        count=count,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetDRepRegistrationsOrder | Unset = GetDRepRegistrationsOrder.DESC,
) -> list[DRepRegistration] | None:
    """Get dRep registrations by page number and count

    Args:
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetDRepRegistrationsOrder | Unset):  Default: GetDRepRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DRepRegistration]
    """

    return sync_detailed(
        client=client,
        page=page,
        count=count,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetDRepRegistrationsOrder | Unset = GetDRepRegistrationsOrder.DESC,
) -> Response[list[DRepRegistration]]:
    """Get dRep registrations by page number and count

    Args:
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetDRepRegistrationsOrder | Unset):  Default: GetDRepRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DRepRegistration]]
    """

    kwargs = _get_kwargs(
        page=page,
        count=count,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetDRepRegistrationsOrder | Unset = GetDRepRegistrationsOrder.DESC,
) -> list[DRepRegistration] | None:
    """Get dRep registrations by page number and count

    Args:
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetDRepRegistrationsOrder | Unset):  Default: GetDRepRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DRepRegistration]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            count=count,
            order=order,
        )
    ).parsed
