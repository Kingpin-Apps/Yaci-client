from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gov_action_proposal_by_return_address_order import (
    GetGovActionProposalByReturnAddressOrder,
)
from ...models.gov_action_proposal import GovActionProposal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    address: str,
    *,
    page: Unset | int = 0,
    count: Unset | int = 10,
    order: Unset | GetGovActionProposalByReturnAddressOrder = GetGovActionProposalByReturnAddressOrder.DESC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/governance/proposals/return-address/{address}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list["GovActionProposal"] | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GovActionProposal.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list["GovActionProposal"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    *,
    client: AuthenticatedClient | Client,
    page: Unset | int = 0,
    count: Unset | int = 10,
    order: Unset | GetGovActionProposalByReturnAddressOrder = GetGovActionProposalByReturnAddressOrder.DESC,
) -> Response[list["GovActionProposal"]]:
    """Get governance action proposal list by return address

    Args:
        address (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByReturnAddressOrder]):  Default:
            GetGovActionProposalByReturnAddressOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GovActionProposal']]
    """

    kwargs = _get_kwargs(
        address=address,
        page=page,
        count=count,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: AuthenticatedClient | Client,
    page: Unset | int = 0,
    count: Unset | int = 10,
    order: Unset | GetGovActionProposalByReturnAddressOrder = GetGovActionProposalByReturnAddressOrder.DESC,
) -> list["GovActionProposal"] | None:
    """Get governance action proposal list by return address

    Args:
        address (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByReturnAddressOrder]):  Default:
            GetGovActionProposalByReturnAddressOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GovActionProposal']
    """

    return sync_detailed(
        address=address,
        client=client,
        page=page,
        count=count,
        order=order,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: AuthenticatedClient | Client,
    page: Unset | int = 0,
    count: Unset | int = 10,
    order: Unset | GetGovActionProposalByReturnAddressOrder = GetGovActionProposalByReturnAddressOrder.DESC,
) -> Response[list["GovActionProposal"]]:
    """Get governance action proposal list by return address

    Args:
        address (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByReturnAddressOrder]):  Default:
            GetGovActionProposalByReturnAddressOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GovActionProposal']]
    """

    kwargs = _get_kwargs(
        address=address,
        page=page,
        count=count,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: AuthenticatedClient | Client,
    page: Unset | int = 0,
    count: Unset | int = 10,
    order: Unset | GetGovActionProposalByReturnAddressOrder = GetGovActionProposalByReturnAddressOrder.DESC,
) -> list["GovActionProposal"] | None:
    """Get governance action proposal list by return address

    Args:
        address (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByReturnAddressOrder]):  Default:
            GetGovActionProposalByReturnAddressOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GovActionProposal']
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
            page=page,
            count=count,
            order=order,
        )
    ).parsed
