from http import HTTPStatus
from typing import Any

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
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetVotingProceduresByGovActionProposalTxOrder | Unset = GetVotingProceduresByGovActionProposalTxOrder.DESC,
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
        "url": f"/api/v1/governance/proposals/{tx_hash}/votes",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[VotingProcedure] | None:
    if response.status_code == 200:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[VotingProcedure]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tx_hash: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetVotingProceduresByGovActionProposalTxOrder | Unset = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> Response[list[VotingProcedure]]:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetVotingProceduresByGovActionProposalTxOrder | Unset):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[VotingProcedure]]
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
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetVotingProceduresByGovActionProposalTxOrder | Unset = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> list[VotingProcedure] | None:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetVotingProceduresByGovActionProposalTxOrder | Unset):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[VotingProcedure]
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
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetVotingProceduresByGovActionProposalTxOrder | Unset = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> Response[list[VotingProcedure]]:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetVotingProceduresByGovActionProposalTxOrder | Unset):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[VotingProcedure]]
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
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
    order: GetVotingProceduresByGovActionProposalTxOrder | Unset = GetVotingProceduresByGovActionProposalTxOrder.DESC,
) -> list[VotingProcedure] | None:
    """Get voting procedure list by transaction hash of governance action proposal

    Args:
        tx_hash (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.
        order (GetVotingProceduresByGovActionProposalTxOrder | Unset):  Default:
            GetVotingProceduresByGovActionProposalTxOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[VotingProcedure]
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
