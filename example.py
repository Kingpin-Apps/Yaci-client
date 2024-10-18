import json
from typing import Optional

from yaci_client import Client
from yaci_client.api.account_api import get_stake_account_details
from yaci_client.api.address_service import get_utxos_1
from yaci_client.api.local_epoch_service import (
    get_latest_epoch,
    get_latest_protocol_params,
)
from yaci_client.api.utilities import evaluate_tx
from yaci_client.errors import UnexpectedStatus
from yaci_client.models import (
    EpochNo,
    ProtocolParams,
    ProtocolParamsDto,
    StakeAccountInfo,
    Utxo,
)
from yaci_client.types import Response


def main():
    """
    Get the protocol parameters from yaci-store-api
    """
    client = Client(base_url="http://localhost:8080", raise_on_unexpected_status=True)

    with client as client:
        params: ProtocolParamsDto = get_latest_protocol_params.sync(client=client)
        print(params)
        response: Response[ProtocolParamsDto] = (
            get_latest_protocol_params.sync_detailed(client=client)
        )
        protocol_params_json = json.loads(response.content)
        print(protocol_params_json)
        protocol_params = ProtocolParams.from_dict(protocol_params_json)
        print(protocol_params)

        response: Response[EpochNo] = get_latest_epoch.sync_detailed(client=client)
        epoch_json = json.loads(response.content)
        print(epoch_json)
        epoch = EpochNo.from_dict(epoch_json)
        print(epoch)

        utxos: list[Utxo] = get_utxos_1.sync(
            address="addr_test1qrh3nrahcd0pj6ps3g9htnlw2jjxuylgdhfn2s5rxqyrr43yzewr2766qsfeq6stl65t546cwvclpqm2rpkkxtksgxuq90xn5f",
            client=client,
        )
        print(utxos)
        response: Response[list[Utxo]] = get_utxos_1.sync_detailed(
            address="addr_test1qrh3nrahcd0pj6ps3g9htnlw2jjxuylgdhfn2s5rxqyrr43yzewr2766qsfeq6stl65t546cwvclpqm2rpkkxtksgxuq90xn5f",
            client=client,
        )
        utxos_json = json.loads(response.content)
        print(utxos_json)
        utxos = [Utxo(**utxo) for utxo in utxos_json]
        print(utxos)

        tx_cbor = "84a50081825820823048cecd15e2be0025e46dade7fc4b8de6e7f741f9416be17befff3c697605010181a200583900a4d26c8ba86e72dd63ab83482d7096c9858988bf103995de9e89ee5186a92ab773796a0c2d225743eaa2d92aeba80648cb02cbc83bff9341011b0000000236000d0e021a0002f31d031a07e62d9204818a03581ced46e6f1e325befcd4e1c333e912cf570babee373fd8a3274bd318d758203462c9f48bfb342994b18ec7c932c0cce12fb6e2c374dd78828b9bc3c54721de1a3b9aca001a1443fd00d81e82010a581de086a92ab773796a0c2d225743eaa2d92aeba80648cb02cbc83bff934181581c86a92ab773796a0c2d225743eaa2d92aeba80648cb02cbc83bff9341818400190bb944228af79bf682781d68747470733a2f2f74696e7975726c2e636f6d2f6b696e672d706f6f6c5820911aa9d13a763cf3545e9e41006a7af932e90f8731f595e0675d31ba99511ec9a0f5f6"
        stake_addr = "stake_test1uruw6wswag80sd0l57alehj47llf6tx96402vt8vks46k0q0e2ne6"
        # response: Optional[str] = submit_tx_1.sync(body="grgrege", client=client)
        # print(response)

        try:
            response: Optional[str] = evaluate_tx.sync(body=tx_cbor, client=client)
            print(response)
        except UnexpectedStatus as e:
            print(e)

        try:
            response: Optional[StakeAccountInfo] = get_stake_account_details.sync(
                stake_address=stake_addr, client=client
            )
            print(response)
        except UnexpectedStatus as e:
            print(e)

        # response: Response[EpochContent] = get_latest_epoch_1.sync_detailed(client=client)
        # epoch_json = json.loads(response.content)
        # print(epoch_json)
        # epoch = EpochContent.from_dict(epoch_json)
        # print(epoch)
        #
        # response: Response[EpochContent] = get_latest_epoch_1.sync_detailed(client=client)
        # epoch_json = json.loads(response.content)
        # print(epoch_json)
        # epoch = EpochContent.from_dict(epoch_json)
        # print(epoch)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
