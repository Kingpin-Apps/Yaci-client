"""The generated client against a stand-in server (httpx.MockTransport)."""

import importlib
import importlib.metadata
import pkgutil
import ssl

import attrs
import httpx
import pytest

import yaci_client
from yaci_client import AuthenticatedClient, Client
from yaci_client.api.committee_service import get_committee_de_registrations
from yaci_client.api.local_epoch_service import get_latest_epoch
from yaci_client.errors import UnexpectedStatus

BASE_URL = "http://yaci.test"

MODULES = sorted(m.name for m in pkgutil.walk_packages(yaci_client.__path__, "yaci_client."))
ENDPOINTS = [name for name in MODULES if name.count(".") == 3 and name.startswith("yaci_client.api.")]


class FakeYaciStore:
    """Answers each request from ``responses``, by path, and records it."""

    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []
        self.responses: dict[str, httpx.Response] = {
            "/api/v1/epochs/latest": httpx.Response(200, json={"epoch": 1457}),
        }

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.responses.get(request.url.path, httpx.Response(200, json=[]))

    @property
    def transport(self) -> httpx.MockTransport:
        return httpx.MockTransport(self)


@pytest.fixture
def store() -> FakeYaciStore:
    return FakeYaciStore()


def test_version_matches_the_package_metadata() -> None:
    assert importlib.metadata.version("yaci-client") == yaci_client.__version__


@pytest.mark.parametrize("name", MODULES)
def test_every_module_imports(name: str) -> None:
    importlib.import_module(name)


@pytest.mark.parametrize("name", ENDPOINTS)
def test_every_endpoint_has_sync_and_async_calls(name: str) -> None:
    module = importlib.import_module(name)
    for function in ("sync", "sync_detailed", "asyncio", "asyncio_detailed"):
        assert callable(getattr(module, function)), f"{name}.{function}"


def test_sync_call(store: FakeYaciStore) -> None:
    client = Client(base_url=BASE_URL, httpx_args={"transport": store.transport})

    epoch = get_latest_epoch.sync(client=client)

    assert epoch is not None
    assert epoch.epoch == 1457
    assert store.requests[0].method == "GET"
    assert str(store.requests[0].url) == f"{BASE_URL}/api/v1/epochs/latest"


async def test_async_call(store: FakeYaciStore) -> None:
    client = Client(base_url=BASE_URL, httpx_args={"transport": store.transport})

    epoch = await get_latest_epoch.asyncio(client=client)

    assert epoch is not None
    assert epoch.epoch == 1457


def test_query_parameters(store: FakeYaciStore) -> None:
    client = Client(base_url=BASE_URL, httpx_args={"transport": store.transport})

    response = get_committee_de_registrations.sync_detailed(client=client, page=2, count=5)

    assert response.status_code == 200
    assert store.requests[0].url.params == httpx.QueryParams({"page": "2", "count": "5", "order": "desc"})


async def test_authenticated_client_sends_the_token(store: FakeYaciStore) -> None:
    client = AuthenticatedClient(base_url=BASE_URL, token="secret", httpx_args={"transport": store.transport})

    await get_latest_epoch.asyncio(client=client)

    assert store.requests[0].headers["authorization"] == "Bearer secret"


@pytest.mark.parametrize("verify_ssl", [True, False, ssl.create_default_context()])
def test_verify_ssl_settings_reach_httpx(store: FakeYaciStore, verify_ssl: bool | ssl.SSLContext) -> None:
    client = Client(base_url=BASE_URL, verify_ssl=verify_ssl, httpx_args={"transport": store.transport})

    assert get_latest_epoch.sync(client=client) is not None


def test_unexpected_status_raises_when_asked(store: FakeYaciStore) -> None:
    store.responses["/api/v1/epochs/latest"] = httpx.Response(503, text="down")
    client = Client(base_url=BASE_URL, raise_on_unexpected_status=True, httpx_args={"transport": store.transport})

    with pytest.raises(UnexpectedStatus) as error:
        get_latest_epoch.sync(client=client)

    assert error.value.status_code == 503


def test_unexpected_status_is_none_by_default(store: FakeYaciStore) -> None:
    store.responses["/api/v1/epochs/latest"] = httpx.Response(503, text="down")
    client = Client(base_url=BASE_URL, httpx_args={"transport": store.transport})

    assert get_latest_epoch.sync(client=client) is None


@pytest.mark.parametrize(
    ("model", "field"),
    [
        ("yaci_client.models.gov_action_proposal.GovActionProposal", "type"),
        ("yaci_client.models.d_rep_registration.DRepRegistration", "type"),
        ("yaci_client.models.block_dto.BlockDto", "hash_"),
    ],
)
def test_public_field_names_are_stable(model: str, field: str) -> None:
    """Newer generators rename fields that shadow builtins; that would break callers."""
    module_name, class_name = model.rsplit(".", 1)
    cls = getattr(importlib.import_module(module_name), class_name)
    assert field in {attribute.name for attribute in attrs.fields(cls)}
