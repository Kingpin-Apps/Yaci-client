from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drep_vote_thresholds import DrepVoteThresholds
    from ..models.pool_voting_thresholds import PoolVotingThresholds
    from ..models.protocol_params_cost_models import ProtocolParamsCostModels


T = TypeVar("T", bound="ProtocolParams")


@_attrs_define
class ProtocolParams:
    """
    Attributes:
        min_fee_a (Union[Unset, int]):
        min_fee_b (Union[Unset, int]):
        max_block_size (Union[Unset, int]):
        max_tx_size (Union[Unset, int]):
        max_block_header_size (Union[Unset, int]):
        key_deposit (Union[Unset, int]):
        pool_deposit (Union[Unset, int]):
        max_epoch (Union[Unset, int]):
        pool_pledge_influence (Union[Unset, float]):
        expansion_rate (Union[Unset, float]):
        treasury_growth_rate (Union[Unset, float]):
        decentralisation_param (Union[Unset, float]):
        extra_entropy (Union[Unset, str]):
        protocol_major_ver (Union[Unset, int]):
        protocol_minor_ver (Union[Unset, int]):
        min_utxo (Union[Unset, int]):
        min_pool_cost (Union[Unset, int]):
        ada_per_utxo_byte (Union[Unset, int]):
        cost_models (Union[Unset, ProtocolParamsCostModels]):
        cost_models_hash (Union[Unset, str]):
        price_mem (Union[Unset, float]):
        price_step (Union[Unset, float]):
        max_tx_ex_mem (Union[Unset, int]):
        max_tx_ex_steps (Union[Unset, int]):
        max_block_ex_mem (Union[Unset, int]):
        max_block_ex_steps (Union[Unset, int]):
        max_val_size (Union[Unset, int]):
        collateral_percent (Union[Unset, int]):
        max_collateral_inputs (Union[Unset, int]):
        pool_voting_thresholds (Union[Unset, PoolVotingThresholds]):
        drep_voting_thresholds (Union[Unset, DrepVoteThresholds]):
        committee_min_size (Union[Unset, int]):
        committee_max_term_length (Union[Unset, int]):
        gov_action_lifetime (Union[Unset, int]):
        gov_action_deposit (Union[Unset, int]):
        drep_deposit (Union[Unset, int]):
        drep_activity (Union[Unset, int]):
        min_fee_ref_script_cost_per_byte (Union[Unset, float]):
        nopt (Union[Unset, int]):
    """

    min_fee_a: Union[Unset, int] = UNSET
    min_fee_b: Union[Unset, int] = UNSET
    max_block_size: Union[Unset, int] = UNSET
    max_tx_size: Union[Unset, int] = UNSET
    max_block_header_size: Union[Unset, int] = UNSET
    key_deposit: Union[Unset, int] = UNSET
    pool_deposit: Union[Unset, int] = UNSET
    max_epoch: Union[Unset, int] = UNSET
    pool_pledge_influence: Union[Unset, float] = UNSET
    expansion_rate: Union[Unset, float] = UNSET
    treasury_growth_rate: Union[Unset, float] = UNSET
    decentralisation_param: Union[Unset, float] = UNSET
    extra_entropy: Union[Unset, str] = UNSET
    protocol_major_ver: Union[Unset, int] = UNSET
    protocol_minor_ver: Union[Unset, int] = UNSET
    min_utxo: Union[Unset, int] = UNSET
    min_pool_cost: Union[Unset, int] = UNSET
    ada_per_utxo_byte: Union[Unset, int] = UNSET
    cost_models: Union[Unset, "ProtocolParamsCostModels"] = UNSET
    cost_models_hash: Union[Unset, str] = UNSET
    price_mem: Union[Unset, float] = UNSET
    price_step: Union[Unset, float] = UNSET
    max_tx_ex_mem: Union[Unset, int] = UNSET
    max_tx_ex_steps: Union[Unset, int] = UNSET
    max_block_ex_mem: Union[Unset, int] = UNSET
    max_block_ex_steps: Union[Unset, int] = UNSET
    max_val_size: Union[Unset, int] = UNSET
    collateral_percent: Union[Unset, int] = UNSET
    max_collateral_inputs: Union[Unset, int] = UNSET
    pool_voting_thresholds: Union[Unset, "PoolVotingThresholds"] = UNSET
    drep_voting_thresholds: Union[Unset, "DrepVoteThresholds"] = UNSET
    committee_min_size: Union[Unset, int] = UNSET
    committee_max_term_length: Union[Unset, int] = UNSET
    gov_action_lifetime: Union[Unset, int] = UNSET
    gov_action_deposit: Union[Unset, int] = UNSET
    drep_deposit: Union[Unset, int] = UNSET
    drep_activity: Union[Unset, int] = UNSET
    min_fee_ref_script_cost_per_byte: Union[Unset, float] = UNSET
    nopt: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        min_fee_a = self.min_fee_a

        min_fee_b = self.min_fee_b

        max_block_size = self.max_block_size

        max_tx_size = self.max_tx_size

        max_block_header_size = self.max_block_header_size

        key_deposit = self.key_deposit

        pool_deposit = self.pool_deposit

        max_epoch = self.max_epoch

        pool_pledge_influence = self.pool_pledge_influence

        expansion_rate = self.expansion_rate

        treasury_growth_rate = self.treasury_growth_rate

        decentralisation_param = self.decentralisation_param

        extra_entropy = self.extra_entropy

        protocol_major_ver = self.protocol_major_ver

        protocol_minor_ver = self.protocol_minor_ver

        min_utxo = self.min_utxo

        min_pool_cost = self.min_pool_cost

        ada_per_utxo_byte = self.ada_per_utxo_byte

        cost_models: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_models, Unset):
            cost_models = self.cost_models.to_dict()

        cost_models_hash = self.cost_models_hash

        price_mem = self.price_mem

        price_step = self.price_step

        max_tx_ex_mem = self.max_tx_ex_mem

        max_tx_ex_steps = self.max_tx_ex_steps

        max_block_ex_mem = self.max_block_ex_mem

        max_block_ex_steps = self.max_block_ex_steps

        max_val_size = self.max_val_size

        collateral_percent = self.collateral_percent

        max_collateral_inputs = self.max_collateral_inputs

        pool_voting_thresholds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pool_voting_thresholds, Unset):
            pool_voting_thresholds = self.pool_voting_thresholds.to_dict()

        drep_voting_thresholds: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.drep_voting_thresholds, Unset):
            drep_voting_thresholds = self.drep_voting_thresholds.to_dict()

        committee_min_size = self.committee_min_size

        committee_max_term_length = self.committee_max_term_length

        gov_action_lifetime = self.gov_action_lifetime

        gov_action_deposit = self.gov_action_deposit

        drep_deposit = self.drep_deposit

        drep_activity = self.drep_activity

        min_fee_ref_script_cost_per_byte = self.min_fee_ref_script_cost_per_byte

        nopt = self.nopt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_fee_a is not UNSET:
            field_dict["min_fee_a"] = min_fee_a
        if min_fee_b is not UNSET:
            field_dict["min_fee_b"] = min_fee_b
        if max_block_size is not UNSET:
            field_dict["max_block_size"] = max_block_size
        if max_tx_size is not UNSET:
            field_dict["max_tx_size"] = max_tx_size
        if max_block_header_size is not UNSET:
            field_dict["max_block_header_size"] = max_block_header_size
        if key_deposit is not UNSET:
            field_dict["key_deposit"] = key_deposit
        if pool_deposit is not UNSET:
            field_dict["pool_deposit"] = pool_deposit
        if max_epoch is not UNSET:
            field_dict["max_epoch"] = max_epoch
        if pool_pledge_influence is not UNSET:
            field_dict["pool_pledge_influence"] = pool_pledge_influence
        if expansion_rate is not UNSET:
            field_dict["expansion_rate"] = expansion_rate
        if treasury_growth_rate is not UNSET:
            field_dict["treasury_growth_rate"] = treasury_growth_rate
        if decentralisation_param is not UNSET:
            field_dict["decentralisation_param"] = decentralisation_param
        if extra_entropy is not UNSET:
            field_dict["extra_entropy"] = extra_entropy
        if protocol_major_ver is not UNSET:
            field_dict["protocol_major_ver"] = protocol_major_ver
        if protocol_minor_ver is not UNSET:
            field_dict["protocol_minor_ver"] = protocol_minor_ver
        if min_utxo is not UNSET:
            field_dict["min_utxo"] = min_utxo
        if min_pool_cost is not UNSET:
            field_dict["min_pool_cost"] = min_pool_cost
        if ada_per_utxo_byte is not UNSET:
            field_dict["ada_per_utxo_byte"] = ada_per_utxo_byte
        if cost_models is not UNSET:
            field_dict["cost_models"] = cost_models
        if cost_models_hash is not UNSET:
            field_dict["cost_models_hash"] = cost_models_hash
        if price_mem is not UNSET:
            field_dict["price_mem"] = price_mem
        if price_step is not UNSET:
            field_dict["price_step"] = price_step
        if max_tx_ex_mem is not UNSET:
            field_dict["max_tx_ex_mem"] = max_tx_ex_mem
        if max_tx_ex_steps is not UNSET:
            field_dict["max_tx_ex_steps"] = max_tx_ex_steps
        if max_block_ex_mem is not UNSET:
            field_dict["max_block_ex_mem"] = max_block_ex_mem
        if max_block_ex_steps is not UNSET:
            field_dict["max_block_ex_steps"] = max_block_ex_steps
        if max_val_size is not UNSET:
            field_dict["max_val_size"] = max_val_size
        if collateral_percent is not UNSET:
            field_dict["collateral_percent"] = collateral_percent
        if max_collateral_inputs is not UNSET:
            field_dict["max_collateral_inputs"] = max_collateral_inputs
        if pool_voting_thresholds is not UNSET:
            field_dict["pool_voting_thresholds"] = pool_voting_thresholds
        if drep_voting_thresholds is not UNSET:
            field_dict["drep_voting_thresholds"] = drep_voting_thresholds
        if committee_min_size is not UNSET:
            field_dict["committee_min_size"] = committee_min_size
        if committee_max_term_length is not UNSET:
            field_dict["committee_max_term_length"] = committee_max_term_length
        if gov_action_lifetime is not UNSET:
            field_dict["gov_action_lifetime"] = gov_action_lifetime
        if gov_action_deposit is not UNSET:
            field_dict["gov_action_deposit"] = gov_action_deposit
        if drep_deposit is not UNSET:
            field_dict["drep_deposit"] = drep_deposit
        if drep_activity is not UNSET:
            field_dict["drep_activity"] = drep_activity
        if min_fee_ref_script_cost_per_byte is not UNSET:
            field_dict["min_fee_ref_script_cost_per_byte"] = (
                min_fee_ref_script_cost_per_byte
            )
        if nopt is not UNSET:
            field_dict["nopt"] = nopt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.drep_vote_thresholds import DrepVoteThresholds
        from ..models.pool_voting_thresholds import PoolVotingThresholds
        from ..models.protocol_params_cost_models import ProtocolParamsCostModels

        d = src_dict.copy()
        min_fee_a = d.pop("min_fee_a", UNSET)

        min_fee_b = d.pop("min_fee_b", UNSET)

        max_block_size = d.pop("max_block_size", UNSET)

        max_tx_size = d.pop("max_tx_size", UNSET)

        max_block_header_size = d.pop("max_block_header_size", UNSET)

        key_deposit = d.pop("key_deposit", UNSET)

        pool_deposit = d.pop("pool_deposit", UNSET)

        max_epoch = d.pop("max_epoch", UNSET)

        pool_pledge_influence = d.pop("pool_pledge_influence", UNSET)

        expansion_rate = d.pop("expansion_rate", UNSET)

        treasury_growth_rate = d.pop("treasury_growth_rate", UNSET)

        decentralisation_param = d.pop("decentralisation_param", UNSET)

        extra_entropy = d.pop("extra_entropy", UNSET)

        protocol_major_ver = d.pop("protocol_major_ver", UNSET)

        protocol_minor_ver = d.pop("protocol_minor_ver", UNSET)

        min_utxo = d.pop("min_utxo", UNSET)

        min_pool_cost = d.pop("min_pool_cost", UNSET)

        ada_per_utxo_byte = d.pop("ada_per_utxo_byte", UNSET)

        _cost_models = d.pop("cost_models", UNSET)
        cost_models: Union[Unset, ProtocolParamsCostModels]
        if isinstance(_cost_models, Unset):
            cost_models = UNSET
        else:
            cost_models = ProtocolParamsCostModels.from_dict(_cost_models)

        cost_models_hash = d.pop("cost_models_hash", UNSET)

        price_mem = d.pop("price_mem", UNSET)

        price_step = d.pop("price_step", UNSET)

        max_tx_ex_mem = d.pop("max_tx_ex_mem", UNSET)

        max_tx_ex_steps = d.pop("max_tx_ex_steps", UNSET)

        max_block_ex_mem = d.pop("max_block_ex_mem", UNSET)

        max_block_ex_steps = d.pop("max_block_ex_steps", UNSET)

        max_val_size = d.pop("max_val_size", UNSET)

        collateral_percent = d.pop("collateral_percent", UNSET)

        max_collateral_inputs = d.pop("max_collateral_inputs", UNSET)

        _pool_voting_thresholds = d.pop("pool_voting_thresholds", UNSET)
        pool_voting_thresholds: Union[Unset, PoolVotingThresholds]
        if isinstance(_pool_voting_thresholds, Unset):
            pool_voting_thresholds = UNSET
        else:
            pool_voting_thresholds = PoolVotingThresholds.from_dict(
                _pool_voting_thresholds
            )

        _drep_voting_thresholds = d.pop("drep_voting_thresholds", UNSET)
        drep_voting_thresholds: Union[Unset, DrepVoteThresholds]
        if isinstance(_drep_voting_thresholds, Unset):
            drep_voting_thresholds = UNSET
        else:
            drep_voting_thresholds = DrepVoteThresholds.from_dict(
                _drep_voting_thresholds
            )

        committee_min_size = d.pop("committee_min_size", UNSET)

        committee_max_term_length = d.pop("committee_max_term_length", UNSET)

        gov_action_lifetime = d.pop("gov_action_lifetime", UNSET)

        gov_action_deposit = d.pop("gov_action_deposit", UNSET)

        drep_deposit = d.pop("drep_deposit", UNSET)

        drep_activity = d.pop("drep_activity", UNSET)

        min_fee_ref_script_cost_per_byte = d.pop(
            "min_fee_ref_script_cost_per_byte", UNSET
        )

        nopt = d.pop("nopt", UNSET)

        protocol_params = cls(
            min_fee_a=min_fee_a,
            min_fee_b=min_fee_b,
            max_block_size=max_block_size,
            max_tx_size=max_tx_size,
            max_block_header_size=max_block_header_size,
            key_deposit=key_deposit,
            pool_deposit=pool_deposit,
            max_epoch=max_epoch,
            pool_pledge_influence=pool_pledge_influence,
            expansion_rate=expansion_rate,
            treasury_growth_rate=treasury_growth_rate,
            decentralisation_param=decentralisation_param,
            extra_entropy=extra_entropy,
            protocol_major_ver=protocol_major_ver,
            protocol_minor_ver=protocol_minor_ver,
            min_utxo=min_utxo,
            min_pool_cost=min_pool_cost,
            ada_per_utxo_byte=ada_per_utxo_byte,
            cost_models=cost_models,
            cost_models_hash=cost_models_hash,
            price_mem=price_mem,
            price_step=price_step,
            max_tx_ex_mem=max_tx_ex_mem,
            max_tx_ex_steps=max_tx_ex_steps,
            max_block_ex_mem=max_block_ex_mem,
            max_block_ex_steps=max_block_ex_steps,
            max_val_size=max_val_size,
            collateral_percent=collateral_percent,
            max_collateral_inputs=max_collateral_inputs,
            pool_voting_thresholds=pool_voting_thresholds,
            drep_voting_thresholds=drep_voting_thresholds,
            committee_min_size=committee_min_size,
            committee_max_term_length=committee_max_term_length,
            gov_action_lifetime=gov_action_lifetime,
            gov_action_deposit=gov_action_deposit,
            drep_deposit=drep_deposit,
            drep_activity=drep_activity,
            min_fee_ref_script_cost_per_byte=min_fee_ref_script_cost_per_byte,
            nopt=nopt,
        )

        protocol_params.additional_properties = d
        return protocol_params

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
