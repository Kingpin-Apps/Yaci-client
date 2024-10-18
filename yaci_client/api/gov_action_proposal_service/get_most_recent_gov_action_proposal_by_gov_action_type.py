from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_most_recent_gov_action_proposal_by_gov_action_type_gov_action_type import (
    GetMostRecentGovActionProposalByGovActionTypeGovActionType,
)
from ...models.gov_action_proposal import GovActionProposal
from ...types import Response


def _get_kwargs(
    gov_action_type: GetMostRecentGovActionProposalByGovActionTypeGovActionType,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/governance/proposals/latest/gov-action-type/{gov_action_type}".format(
            gov_action_type=gov_action_type,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GovActionProposal]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GovActionProposal.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GovActionProposal]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gov_action_type: GetMostRecentGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GovActionProposal]:
    """Get most recent governance action proposal for a specific type

    Args:
        gov_action_type (GetMostRecentGovActionProposalByGovActionTypeGovActionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GovActionProposal]
    """

    kwargs = _get_kwargs(
        gov_action_type=gov_action_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gov_action_type: GetMostRecentGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GovActionProposal]:
    """Get most recent governance action proposal for a specific type

    Args:
        gov_action_type (GetMostRecentGovActionProposalByGovActionTypeGovActionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GovActionProposal
    """

    return sync_detailed(
        gov_action_type=gov_action_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    gov_action_type: GetMostRecentGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GovActionProposal]:
    """Get most recent governance action proposal for a specific type

    Args:
        gov_action_type (GetMostRecentGovActionProposalByGovActionTypeGovActionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GovActionProposal]
    """

    kwargs = _get_kwargs(
        gov_action_type=gov_action_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gov_action_type: GetMostRecentGovActionProposalByGovActionTypeGovActionType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GovActionProposal]:
    """Get most recent governance action proposal for a specific type

    Args:
        gov_action_type (GetMostRecentGovActionProposalByGovActionTypeGovActionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GovActionProposal
    """

    return (
        await asyncio_detailed(
            gov_action_type=gov_action_type,
            client=client,
        )
    ).parsed
