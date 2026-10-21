"""Query a running Yaci Store (for example a Yaci DevKit devnet) with yaci-client.

Run it against a local DevKit::

    uv run python example.py

Set ``YACI_STORE_URL`` to point it at another Yaci Store (the default is http://localhost:8080).
"""

import os

from yaci_client import Client
from yaci_client.api.account_api import get_stake_account_details
from yaci_client.api.address_service import get_utxos_1
from yaci_client.api.local_epoch_service import get_latest_epoch, get_latest_protocol_params
from yaci_client.api.utilities import evaluate_tx
from yaci_client.errors import UnexpectedStatus

YACI_STORE_URL = os.environ.get("YACI_STORE_URL", "http://localhost:8080")

ADDRESS = "addr_test1qrh3nrahcd0pj6ps3g9htnlw2jjxuylgdhfn2s5rxqyrr43yzewr2766qsfeq6stl65t546cwvclpqm2rpkkxtksgxuq90xn5f"
STAKE_ADDRESS = "stake_test1uruw6wswag80sd0l57alehj47llf6tx96402vt8vks46k0q0e2ne6"
# A signed transaction to evaluate. Yaci Store answers with an error when its inputs are not on the devnet.
TX_CBOR = (
    "84a50081825820823048cecd15e2be0025e46dade7fc4b8de6e7f741f9416be17befff3c697605010181a20058390"
    "0a4d26c8ba86e72dd63ab83482d7096c9858988bf103995de9e89ee5186a92ab773796a0c2d225743eaa2d92aeba8"
    "0648cb02cbc83bff9341011b0000000236000d0e021a0002f31d031a07e62d9204818a03581ced46e6f1e325befc"
    "d4e1c333e912cf570babee373fd8a3274bd318d758203462c9f48bfb342994b18ec7c932c0cce12fb6e2c374dd788"
    "28b9bc3c54721de1a3b9aca001a1443fd00d81e82010a581de086a92ab773796a0c2d225743eaa2d92aeba80648c"
    "b02cbc83bff934181581c86a92ab773796a0c2d225743eaa2d92aeba80648cb02cbc83bff9341818400190bb94422"
    "8af79bf682781d68747470733a2f2f74696e7975726c2e636f6d2f6b696e672d706f6f6c5820911aa9d13a763cf3"
    "545e9e41006a7af932e90f8731f595e0675d31ba99511ec9a0f5f6"
)


def main() -> None:
    # raise_on_unexpected_status makes an undocumented status raise UnexpectedStatus instead of
    # returning None.
    with Client(base_url=YACI_STORE_URL, raise_on_unexpected_status=True) as client:
        # `sync` returns the parsed model, or None.
        params = get_latest_protocol_params.sync(client=client)
        if params is not None:
            print("Fee parameters: a =", params.min_fee_a, "b =", params.min_fee_b)

        # `sync_detailed` also returns the status code, headers and raw body.
        response = get_latest_protocol_params.sync_detailed(client=client)
        print("Status:", response.status_code, "parsed:", response.parsed is not None)

        epoch = get_latest_epoch.sync(client=client)
        if epoch is not None:
            print("Latest epoch:", epoch.epoch)

        for utxo in get_utxos_1.sync(ADDRESS, client=client, count=5) or []:
            print("UTxO:", utxo.tx_hash, utxo.output_index, utxo.amount)

        try:
            account = get_stake_account_details.sync(STAKE_ADDRESS, client=client)
            print("Stake account:", account)
        except UnexpectedStatus as error:
            print("Stake account lookup failed:", error.status_code, error.content.decode(errors="replace"))

        try:
            evaluation = evaluate_tx.sync(client=client, body=TX_CBOR)
            print("Evaluation:", evaluation)
        except UnexpectedStatus as error:
            print("Evaluation failed:", error.status_code, error.content.decode(errors="replace"))


if __name__ == "__main__":
    main()
