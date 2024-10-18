from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gov_action_proposal_by_gov_action_type_gov_action_type import (
    GetGovActionProposalByGovActionTypeGovActionType,
)
from ...models.get_gov_action_proposal_by_gov_action_type_order import (
    GetGovActionProposalByGovActionTypeOrder,
)
from ...models.gov_action_proposal import GovActionProposal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    gov_action_type: GetGovActionProposalByGovActionTypeGovActionType,
    *,
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetGovActionProposalByGovActionTypeOrder
    ] = GetGovActionProposalByGovActionTypeOrder.DESC,
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
        "url": "/api/v1/governance/proposals/gov-action-type/{gov_action_type}".format(
            gov_action_type=gov_action_type,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["GovActionProposal"]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["GovActionProposal"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gov_action_type: GetGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetGovActionProposalByGovActionTypeOrder
    ] = GetGovActionProposalByGovActionTypeOrder.DESC,
) -> Response[List["GovActionProposal"]]:
    """Get governance action proposal list by governance action type

    Args:
        gov_action_type (GetGovActionProposalByGovActionTypeGovActionType):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByGovActionTypeOrder]):  Default:
            GetGovActionProposalByGovActionTypeOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GovActionProposal']]
    """

    kwargs = _get_kwargs(
        gov_action_type=gov_action_type,
        page=page,
        count=count,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gov_action_type: GetGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetGovActionProposalByGovActionTypeOrder
    ] = GetGovActionProposalByGovActionTypeOrder.DESC,
) -> Optional[List["GovActionProposal"]]:
    """Get governance action proposal list by governance action type

    Args:
        gov_action_type (GetGovActionProposalByGovActionTypeGovActionType):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByGovActionTypeOrder]):  Default:
            GetGovActionProposalByGovActionTypeOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GovActionProposal']
    """

    return sync_detailed(
        gov_action_type=gov_action_type,
        client=client,
        page=page,
        count=count,
        order=order,
    ).parsed


async def asyncio_detailed(
    gov_action_type: GetGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetGovActionProposalByGovActionTypeOrder
    ] = GetGovActionProposalByGovActionTypeOrder.DESC,
) -> Response[List["GovActionProposal"]]:
    """Get governance action proposal list by governance action type

    Args:
        gov_action_type (GetGovActionProposalByGovActionTypeGovActionType):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByGovActionTypeOrder]):  Default:
            GetGovActionProposalByGovActionTypeOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GovActionProposal']]
    """

    kwargs = _get_kwargs(
        gov_action_type=gov_action_type,
        page=page,
        count=count,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gov_action_type: GetGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetGovActionProposalByGovActionTypeOrder
    ] = GetGovActionProposalByGovActionTypeOrder.DESC,
) -> Optional[List["GovActionProposal"]]:
    """Get governance action proposal list by governance action type

    Args:
        gov_action_type (GetGovActionProposalByGovActionTypeGovActionType):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetGovActionProposalByGovActionTypeOrder]):  Default:
            GetGovActionProposalByGovActionTypeOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GovActionProposal']
    """

    return (
        await asyncio_detailed(
            gov_action_type=gov_action_type,
            client=client,
            page=page,
            count=count,
            order=order,
        )
    ).parsed
