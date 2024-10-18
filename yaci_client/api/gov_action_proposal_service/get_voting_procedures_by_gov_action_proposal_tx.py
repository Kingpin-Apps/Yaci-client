from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_voting_procedures_by_gov_action_proposal_tx_order import (
    GetVotingProceduresByGovActionProposalTxOrder,
)
from ...models.voting_procedure import VotingProcedure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tx_hash: str,
    *,
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetVotingProceduresByGovActionProposalTxOrder
    ] = GetVotingProceduresByGovActionProposalTxOrder.DESC,
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
        "url": "/api/v1/governance/proposals/{tx_hash}/votes".format(
            tx_hash=tx_hash,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["VotingProcedure"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VotingProcedure.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["VotingProcedure"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetVotingProceduresByGovActionProposalTxOrder
    ] = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> Response[List["VotingProcedure"]]:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetVotingProceduresByGovActionProposalTxOrder]):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['VotingProcedure']]
    """

    kwargs = _get_kwargs(
        tx_hash=tx_hash,
        page=page,
        count=count,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetVotingProceduresByGovActionProposalTxOrder
    ] = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> Optional[List["VotingProcedure"]]:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetVotingProceduresByGovActionProposalTxOrder]):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['VotingProcedure']
    """

    return sync_detailed(
        tx_hash=tx_hash,
        client=client,
        page=page,
        count=count,
        order=order,
    ).parsed


async def asyncio_detailed(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetVotingProceduresByGovActionProposalTxOrder
    ] = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> Response[List["VotingProcedure"]]:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetVotingProceduresByGovActionProposalTxOrder]):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['VotingProcedure']]
    """

    kwargs = _get_kwargs(
        tx_hash=tx_hash,
        page=page,
        count=count,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tx_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
    order: Union[
        Unset, GetVotingProceduresByGovActionProposalTxOrder
    ] = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> Optional[List["VotingProcedure"]]:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (Union[Unset, int]):  Default: 0.
        count (Union[Unset, int]):  Default: 10.
        order (Union[Unset, GetVotingProceduresByGovActionProposalTxOrder]):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['VotingProcedure']
    """

    return (
        await asyncio_detailed(
            tx_hash=tx_hash,
            client=client,
            page=page,
            count=count,
            order=order,
        )
    ).parsed
