from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_label_dto import MetadataLabelDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    label: str,
    *,
    page: int | Unset = 0,
    count: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/txs/metadata/labels/{label}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[MetadataLabelDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MetadataLabelDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[MetadataLabelDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    label: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
) -> Response[list[MetadataLabelDto]]:
    """Metadata Labels

     Get a list of metadata Label included by a specific label.

    Args:
        label (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[MetadataLabelDto]]
    """

    kwargs = _get_kwargs(
        label=label,
        page=page,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
) -> list[MetadataLabelDto] | None:
    """Metadata Labels

     Get a list of metadata Label included by a specific label.

    Args:
        label (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[MetadataLabelDto]
    """

    return sync_detailed(
        label=label,
        client=client,
        page=page,
        count=count,
    ).parsed


async def asyncio_detailed(
    label: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
) -> Response[list[MetadataLabelDto]]:
    """Metadata Labels

     Get a list of metadata Label included by a specific label.

    Args:
        label (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[MetadataLabelDto]]
    """

    kwargs = _get_kwargs(
        label=label,
        page=page,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    count: int | Unset = 10,
) -> list[MetadataLabelDto] | None:
    """Metadata Labels

     Get a list of metadata Label included by a specific label.

    Args:
        label (str):
        page (int | Unset):  Default: 0.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[MetadataLabelDto]
    """

    return (
        await asyncio_detailed(
            label=label,
            client=client,
            page=page,
            count=count,
        )
    ).parsed
