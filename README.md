# yaci-store-api-client
A client library for accessing [Yaci](https://devkit.yaci.xyz) Store API.

This library is  mostly generated using [OpenAPI Generator](https://github.com/openapi-generators/openapi-python-client/).

## Usage
First, create a client:

```python
from yaci_client import Client

client = Client(base_url="http://localhost:8080", raise_on_unexpected_status=True)
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from yaci_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://localhost:8080", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
import json
from yaci_client.api.local_epoch_service import (
    get_latest_protocol_params,
)
from yaci_client import Client
from yaci_client.models import (
    ProtocolParamsDto,
)
from yaci_client.types import Response

client = Client(base_url="http://localhost:8080", raise_on_unexpected_status=True)

with client as client:
     params: ProtocolParamsDto = get_latest_protocol_params.sync(client=client)
     print(params)
     
     response: Response[ProtocolParamsDto] = (
         get_latest_protocol_params.sync_detailed(client=client)
     )
     protocol_params_json = json.loads(response.content)
     print(protocol_params_json)
```

Or do the same thing with an async version:

```python
import json
from yaci_client.api.local_epoch_service import (
    get_latest_protocol_params,
)
from yaci_client import Client
from yaci_client.models import (
    ProtocolParamsDto,
)
from yaci_client.types import Response

client = Client(base_url="http://localhost:8080", raise_on_unexpected_status=True)

async with client as client:
    params: ProtocolParamsDto = await get_latest_protocol_params.asyncio(client=client)
    response: Response[ProtocolParamsDto] = await get_latest_protocol_params.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
from yaci_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://localhost:8080", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
from yaci_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://localhost:8080", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `yaci_store_api_client.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from yaci_client import Client


def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")


def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")


client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from yaci_client import Client

client = Client(
    base_url="https://localhost:8080",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://localhost:8080", proxies="http://localhost:8030"))
```

## Building / publishing this package
This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
