from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protocol_params_dto_cost_models import ProtocolParamsDtoCostModels


T = TypeVar("T", bound="ProtocolParamsDto")


@_attrs_define
class ProtocolParamsDto:
    """
    Attributes:
        min_fee_a (int | Unset):
        min_fee_b (int | Unset):
        max_block_size (int | Unset):
        max_tx_size (int | Unset):
        max_block_header_size (int | Unset):
        key_deposit (str | Unset):
        pool_deposit (str | Unset):
        a0 (float | Unset):
        rho (float | Unset):
        tau (float | Unset):
        decentralisation_param (float | Unset):
        extra_entropy (str | Unset):
        protocol_major_ver (int | Unset):
        protocol_minor_ver (int | Unset):
        min_utxo (str | Unset):
        min_pool_cost (str | Unset):
        nonce (str | Unset):
        cost_models (ProtocolParamsDtoCostModels | Unset):
        price_mem (float | Unset):
        price_step (float | Unset):
        max_tx_ex_mem (str | Unset):
        max_tx_ex_steps (str | Unset):
        max_block_ex_mem (str | Unset):
        max_block_ex_steps (str | Unset):
        max_val_size (str | Unset):
        collateral_percent (float | Unset):
        max_collateral_inputs (int | Unset):
        coins_per_utxo_size (str | Unset):
        coins_per_utxo_word (str | Unset):
        pvt_motion_no_confidence (float | Unset):
        pvt_committee_normal (float | Unset):
        pvt_committee_no_confidence (float | Unset):
        pvt_hard_fork_initiation (float | Unset):
        dvt_motion_no_confidence (float | Unset):
        dvt_committee_normal (float | Unset):
        dvt_committee_no_confidence (float | Unset):
        dvt_update_to_constitution (float | Unset):
        dvt_hard_fork_initiation (float | Unset):
        dvt_ppnetwork_group (float | Unset):
        dvt_ppeconomic_group (float | Unset):
        dvt_pptechnical_group (float | Unset):
        dvt_ppgov_group (float | Unset):
        dvt_treasury_withdrawal (float | Unset):
        committee_min_size (int | Unset):
        committee_max_term_length (int | Unset):
        gov_action_lifetime (int | Unset):
        gov_action_deposit (int | Unset):
        drep_deposit (int | Unset):
        drep_activity (int | Unset):
        min_fee_ref_script_cost_per_byte (float | Unset):
        e_max (int | Unset):
        n_opt (int | Unset):
    """

    min_fee_a: int | Unset = UNSET
    min_fee_b: int | Unset = UNSET
    max_block_size: int | Unset = UNSET
    max_tx_size: int | Unset = UNSET
    max_block_header_size: int | Unset = UNSET
    key_deposit: str | Unset = UNSET
    pool_deposit: str | Unset = UNSET
    a0: float | Unset = UNSET
    rho: float | Unset = UNSET
    tau: float | Unset = UNSET
    decentralisation_param: float | Unset = UNSET
    extra_entropy: str | Unset = UNSET
    protocol_major_ver: int | Unset = UNSET
    protocol_minor_ver: int | Unset = UNSET
    min_utxo: str | Unset = UNSET
    min_pool_cost: str | Unset = UNSET
    nonce: str | Unset = UNSET
    cost_models: ProtocolParamsDtoCostModels | Unset = UNSET
    price_mem: float | Unset = UNSET
    price_step: float | Unset = UNSET
    max_tx_ex_mem: str | Unset = UNSET
    max_tx_ex_steps: str | Unset = UNSET
    max_block_ex_mem: str | Unset = UNSET
    max_block_ex_steps: str | Unset = UNSET
    max_val_size: str | Unset = UNSET
    collateral_percent: float | Unset = UNSET
    max_collateral_inputs: int | Unset = UNSET
    coins_per_utxo_size: str | Unset = UNSET
    coins_per_utxo_word: str | Unset = UNSET
    pvt_motion_no_confidence: float | Unset = UNSET
    pvt_committee_normal: float | Unset = UNSET
    pvt_committee_no_confidence: float | Unset = UNSET
    pvt_hard_fork_initiation: float | Unset = UNSET
    dvt_motion_no_confidence: float | Unset = UNSET
    dvt_committee_normal: float | Unset = UNSET
    dvt_committee_no_confidence: float | Unset = UNSET
    dvt_update_to_constitution: float | Unset = UNSET
    dvt_hard_fork_initiation: float | Unset = UNSET
    dvt_ppnetwork_group: float | Unset = UNSET
    dvt_ppeconomic_group: float | Unset = UNSET
    dvt_pptechnical_group: float | Unset = UNSET
    dvt_ppgov_group: float | Unset = UNSET
    dvt_treasury_withdrawal: float | Unset = UNSET
    committee_min_size: int | Unset = UNSET
    committee_max_term_length: int | Unset = UNSET
    gov_action_lifetime: int | Unset = UNSET
    gov_action_deposit: int | Unset = UNSET
    drep_deposit: int | Unset = UNSET
    drep_activity: int | Unset = UNSET
    min_fee_ref_script_cost_per_byte: float | Unset = UNSET
    e_max: int | Unset = UNSET
    n_opt: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_fee_a = self.min_fee_a

        min_fee_b = self.min_fee_b

        max_block_size = self.max_block_size

        max_tx_size = self.max_tx_size

        max_block_header_size = self.max_block_header_size

        key_deposit = self.key_deposit

        pool_deposit = self.pool_deposit

        a0 = self.a0

        rho = self.rho

        tau = self.tau

        decentralisation_param = self.decentralisation_param

        extra_entropy = self.extra_entropy

        protocol_major_ver = self.protocol_major_ver

        protocol_minor_ver = self.protocol_minor_ver

        min_utxo = self.min_utxo

        min_pool_cost = self.min_pool_cost

        nonce = self.nonce

        cost_models: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost_models, Unset):
            cost_models = self.cost_models.to_dict()

        price_mem = self.price_mem

        price_step = self.price_step

        max_tx_ex_mem = self.max_tx_ex_mem

        max_tx_ex_steps = self.max_tx_ex_steps

        max_block_ex_mem = self.max_block_ex_mem

        max_block_ex_steps = self.max_block_ex_steps

        max_val_size = self.max_val_size

        collateral_percent = self.collateral_percent

        max_collateral_inputs = self.max_collateral_inputs

        coins_per_utxo_size = self.coins_per_utxo_size

        coins_per_utxo_word = self.coins_per_utxo_word

        pvt_motion_no_confidence = self.pvt_motion_no_confidence

        pvt_committee_normal = self.pvt_committee_normal

        pvt_committee_no_confidence = self.pvt_committee_no_confidence

        pvt_hard_fork_initiation = self.pvt_hard_fork_initiation

        dvt_motion_no_confidence = self.dvt_motion_no_confidence

        dvt_committee_normal = self.dvt_committee_normal

        dvt_committee_no_confidence = self.dvt_committee_no_confidence

        dvt_update_to_constitution = self.dvt_update_to_constitution

        dvt_hard_fork_initiation = self.dvt_hard_fork_initiation

        dvt_ppnetwork_group = self.dvt_ppnetwork_group

        dvt_ppeconomic_group = self.dvt_ppeconomic_group

        dvt_pptechnical_group = self.dvt_pptechnical_group

        dvt_ppgov_group = self.dvt_ppgov_group

        dvt_treasury_withdrawal = self.dvt_treasury_withdrawal

        committee_min_size = self.committee_min_size

        committee_max_term_length = self.committee_max_term_length

        gov_action_lifetime = self.gov_action_lifetime

        gov_action_deposit = self.gov_action_deposit

        drep_deposit = self.drep_deposit

        drep_activity = self.drep_activity

        min_fee_ref_script_cost_per_byte = self.min_fee_ref_script_cost_per_byte

        e_max = self.e_max

        n_opt = self.n_opt

        field_dict: dict[str, Any] = {}
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
        if a0 is not UNSET:
            field_dict["a0"] = a0
        if rho is not UNSET:
            field_dict["rho"] = rho
        if tau is not UNSET:
            field_dict["tau"] = tau
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
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if cost_models is not UNSET:
            field_dict["cost_models"] = cost_models
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
        if coins_per_utxo_size is not UNSET:
            field_dict["coins_per_utxo_size"] = coins_per_utxo_size
        if coins_per_utxo_word is not UNSET:
            field_dict["coins_per_utxo_word"] = coins_per_utxo_word
        if pvt_motion_no_confidence is not UNSET:
            field_dict["pvt_motion_no_confidence"] = pvt_motion_no_confidence
        if pvt_committee_normal is not UNSET:
            field_dict["pvt_committee_normal"] = pvt_committee_normal
        if pvt_committee_no_confidence is not UNSET:
            field_dict["pvt_committee_no_confidence"] = pvt_committee_no_confidence
        if pvt_hard_fork_initiation is not UNSET:
            field_dict["pvt_hard_fork_initiation"] = pvt_hard_fork_initiation
        if dvt_motion_no_confidence is not UNSET:
            field_dict["dvt_motion_no_confidence"] = dvt_motion_no_confidence
        if dvt_committee_normal is not UNSET:
            field_dict["dvt_committee_normal"] = dvt_committee_normal
        if dvt_committee_no_confidence is not UNSET:
            field_dict["dvt_committee_no_confidence"] = dvt_committee_no_confidence
        if dvt_update_to_constitution is not UNSET:
            field_dict["dvt_update_to_constitution"] = dvt_update_to_constitution
        if dvt_hard_fork_initiation is not UNSET:
            field_dict["dvt_hard_fork_initiation"] = dvt_hard_fork_initiation
        if dvt_ppnetwork_group is not UNSET:
            field_dict["dvt_ppnetwork_group"] = dvt_ppnetwork_group
        if dvt_ppeconomic_group is not UNSET:
            field_dict["dvt_ppeconomic_group"] = dvt_ppeconomic_group
        if dvt_pptechnical_group is not UNSET:
            field_dict["dvt_pptechnical_group"] = dvt_pptechnical_group
        if dvt_ppgov_group is not UNSET:
            field_dict["dvt_ppgov_group"] = dvt_ppgov_group
        if dvt_treasury_withdrawal is not UNSET:
            field_dict["dvt_treasury_withdrawal"] = dvt_treasury_withdrawal
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
            field_dict["min_fee_ref_script_cost_per_byte"] = min_fee_ref_script_cost_per_byte
        if e_max is not UNSET:
            field_dict["e_max"] = e_max
        if n_opt is not UNSET:
            field_dict["n_opt"] = n_opt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protocol_params_dto_cost_models import ProtocolParamsDtoCostModels

        d = dict(src_dict)
        min_fee_a = d.pop("min_fee_a", UNSET)

        min_fee_b = d.pop("min_fee_b", UNSET)

        max_block_size = d.pop("max_block_size", UNSET)

        max_tx_size = d.pop("max_tx_size", UNSET)

        max_block_header_size = d.pop("max_block_header_size", UNSET)

        key_deposit = d.pop("key_deposit", UNSET)

        pool_deposit = d.pop("pool_deposit", UNSET)

        a0 = d.pop("a0", UNSET)

        rho = d.pop("rho", UNSET)

        tau = d.pop("tau", UNSET)

        decentralisation_param = d.pop("decentralisation_param", UNSET)

        extra_entropy = d.pop("extra_entropy", UNSET)

        protocol_major_ver = d.pop("protocol_major_ver", UNSET)

        protocol_minor_ver = d.pop("protocol_minor_ver", UNSET)

        min_utxo = d.pop("min_utxo", UNSET)

        min_pool_cost = d.pop("min_pool_cost", UNSET)

        nonce = d.pop("nonce", UNSET)

        _cost_models = d.pop("cost_models", UNSET)
        cost_models: ProtocolParamsDtoCostModels | Unset
        if isinstance(_cost_models, Unset):
            cost_models = UNSET
        else:
            cost_models = ProtocolParamsDtoCostModels.from_dict(_cost_models)

        price_mem = d.pop("price_mem", UNSET)

        price_step = d.pop("price_step", UNSET)

        max_tx_ex_mem = d.pop("max_tx_ex_mem", UNSET)

        max_tx_ex_steps = d.pop("max_tx_ex_steps", UNSET)

        max_block_ex_mem = d.pop("max_block_ex_mem", UNSET)

        max_block_ex_steps = d.pop("max_block_ex_steps", UNSET)

        max_val_size = d.pop("max_val_size", UNSET)

        collateral_percent = d.pop("collateral_percent", UNSET)

        max_collateral_inputs = d.pop("max_collateral_inputs", UNSET)

        coins_per_utxo_size = d.pop("coins_per_utxo_size", UNSET)

        coins_per_utxo_word = d.pop("coins_per_utxo_word", UNSET)

        pvt_motion_no_confidence = d.pop("pvt_motion_no_confidence", UNSET)

        pvt_committee_normal = d.pop("pvt_committee_normal", UNSET)

        pvt_committee_no_confidence = d.pop("pvt_committee_no_confidence", UNSET)

        pvt_hard_fork_initiation = d.pop("pvt_hard_fork_initiation", UNSET)

        dvt_motion_no_confidence = d.pop("dvt_motion_no_confidence", UNSET)

        dvt_committee_normal = d.pop("dvt_committee_normal", UNSET)

        dvt_committee_no_confidence = d.pop("dvt_committee_no_confidence", UNSET)

        dvt_update_to_constitution = d.pop("dvt_update_to_constitution", UNSET)

        dvt_hard_fork_initiation = d.pop("dvt_hard_fork_initiation", UNSET)

        dvt_ppnetwork_group = d.pop("dvt_ppnetwork_group", UNSET)

        dvt_ppeconomic_group = d.pop("dvt_ppeconomic_group", UNSET)

        dvt_pptechnical_group = d.pop("dvt_pptechnical_group", UNSET)

        dvt_ppgov_group = d.pop("dvt_ppgov_group", UNSET)

        dvt_treasury_withdrawal = d.pop("dvt_treasury_withdrawal", UNSET)

        committee_min_size = d.pop("committee_min_size", UNSET)

        committee_max_term_length = d.pop("committee_max_term_length", UNSET)

        gov_action_lifetime = d.pop("gov_action_lifetime", UNSET)

        gov_action_deposit = d.pop("gov_action_deposit", UNSET)

        drep_deposit = d.pop("drep_deposit", UNSET)

        drep_activity = d.pop("drep_activity", UNSET)

        min_fee_ref_script_cost_per_byte = d.pop("min_fee_ref_script_cost_per_byte", UNSET)

        e_max = d.pop("e_max", UNSET)

        n_opt = d.pop("n_opt", UNSET)

        protocol_params_dto = cls(
            min_fee_a=min_fee_a,
            min_fee_b=min_fee_b,
            max_block_size=max_block_size,
            max_tx_size=max_tx_size,
            max_block_header_size=max_block_header_size,
            key_deposit=key_deposit,
            pool_deposit=pool_deposit,
            a0=a0,
            rho=rho,
            tau=tau,
            decentralisation_param=decentralisation_param,
            extra_entropy=extra_entropy,
            protocol_major_ver=protocol_major_ver,
            protocol_minor_ver=protocol_minor_ver,
            min_utxo=min_utxo,
            min_pool_cost=min_pool_cost,
            nonce=nonce,
            cost_models=cost_models,
            price_mem=price_mem,
            price_step=price_step,
            max_tx_ex_mem=max_tx_ex_mem,
            max_tx_ex_steps=max_tx_ex_steps,
            max_block_ex_mem=max_block_ex_mem,
            max_block_ex_steps=max_block_ex_steps,
            max_val_size=max_val_size,
            collateral_percent=collateral_percent,
            max_collateral_inputs=max_collateral_inputs,
            coins_per_utxo_size=coins_per_utxo_size,
            coins_per_utxo_word=coins_per_utxo_word,
            pvt_motion_no_confidence=pvt_motion_no_confidence,
            pvt_committee_normal=pvt_committee_normal,
            pvt_committee_no_confidence=pvt_committee_no_confidence,
            pvt_hard_fork_initiation=pvt_hard_fork_initiation,
            dvt_motion_no_confidence=dvt_motion_no_confidence,
            dvt_committee_normal=dvt_committee_normal,
            dvt_committee_no_confidence=dvt_committee_no_confidence,
            dvt_update_to_constitution=dvt_update_to_constitution,
            dvt_hard_fork_initiation=dvt_hard_fork_initiation,
            dvt_ppnetwork_group=dvt_ppnetwork_group,
            dvt_ppeconomic_group=dvt_ppeconomic_group,
            dvt_pptechnical_group=dvt_pptechnical_group,
            dvt_ppgov_group=dvt_ppgov_group,
            dvt_treasury_withdrawal=dvt_treasury_withdrawal,
            committee_min_size=committee_min_size,
            committee_max_term_length=committee_max_term_length,
            gov_action_lifetime=gov_action_lifetime,
            gov_action_deposit=gov_action_deposit,
            drep_deposit=drep_deposit,
            drep_activity=drep_activity,
            min_fee_ref_script_cost_per_byte=min_fee_ref_script_cost_per_byte,
            e_max=e_max,
            n_opt=n_opt,
        )

        protocol_params_dto.additional_properties = d
        return protocol_params_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
