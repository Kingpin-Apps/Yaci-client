from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pool_block import PoolBlock
from ...types import UNSET, Response


def _get_kwargs(
    pool_id: str,
    *,
    epoch: int,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["epoch"] = epoch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/blocks/pool/{pool_id}".format(
            pool_id=pool_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["PoolBlock"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PoolBlock.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["PoolBlock"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: int,
) -> Response[List["PoolBlock"]]:
    """Slot Leader Block List

     Get blocks of slot leader in a specific epoch.

    Args:
        pool_id (str):
        epoch (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PoolBlock']]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
        epoch=epoch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: int,
) -> Optional[List["PoolBlock"]]:
    """Slot Leader Block List

     Get blocks of slot leader in a specific epoch.

    Args:
        pool_id (str):
        epoch (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PoolBlock']
    """

    return sync_detailed(
        pool_id=pool_id,
        client=client,
        epoch=epoch,
    ).parsed


async def asyncio_detailed(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: int,
) -> Response[List["PoolBlock"]]:
    """Slot Leader Block List

     Get blocks of slot leader in a specific epoch.

    Args:
        pool_id (str):
        epoch (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PoolBlock']]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
        epoch=epoch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    epoch: int,
) -> Optional[List["PoolBlock"]]:
    """Slot Leader Block List

     Get blocks of slot leader in a specific epoch.

    Args:
        pool_id (str):
        epoch (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PoolBlock']
    """

    return (
        await asyncio_detailed(
            pool_id=pool_id,
            client=client,
            epoch=epoch,
        )
    ).parsed
