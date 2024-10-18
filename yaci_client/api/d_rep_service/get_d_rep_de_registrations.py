from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.d_rep_registration import DRepRegistration
from ...models.get_d_rep_de_registrations_order import GetDRepDeRegistrationsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[Unset, GetDRepDeRegistrationsOrder] = GetDRepDeRegistrationsOrder.DESC,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/governance/dreps/deregistrations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DRepRegistration"]]:
    if response.status_code == HTTPStatus.OK:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DRepRegistration"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[Unset, GetDRepDeRegistrationsOrder] = GetDRepDeRegistrationsOrder.DESC,
) -> Response[List["DRepRegistration"]]:
    """Get dRep de-registrations by page number and count

    Args:
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetDRepDeRegistrationsOrder]):  Default:
            GetDRepDeRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DRepRegistration']]
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
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[Unset, GetDRepDeRegistrationsOrder] = GetDRepDeRegistrationsOrder.DESC,
) -> Optional[List["DRepRegistration"]]:
    """Get dRep de-registrations by page number and count

    Args:
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetDRepDeRegistrationsOrder]):  Default:
            GetDRepDeRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DRepRegistration']
    """

    return sync_detailed(
        client=client,
        page=page,
        count=count,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[Unset, GetDRepDeRegistrationsOrder] = GetDRepDeRegistrationsOrder.DESC,
) -> Response[List["DRepRegistration"]]:
    """Get dRep de-registrations by page number and count

    Args:
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetDRepDeRegistrationsOrder]):  Default:
            GetDRepDeRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DRepRegistration']]
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
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[Unset, GetDRepDeRegistrationsOrder] = GetDRepDeRegistrationsOrder.DESC,
) -> Optional[List["DRepRegistration"]]:
    """Get dRep de-registrations by page number and count

    Args:
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetDRepDeRegistrationsOrder]):  Default:
            GetDRepDeRegistrationsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DRepRegistration']
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            count=count,
            order=order,
        )
    ).parsed
