from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from netrise_turbine_sdk_graphql import input_types as inputs
from netrise_turbine_sdk_graphql import enums


_LOOKUP_DEFAULT = "exact"


@dataclass(frozen=True)
class _FilterSpec:
    filter_cls: type
    field_filter_cls: type
    field_enum: type
    operation_enum: type
    fields: dict[str, Any]
    list_value: bool = False
    enum_fields: frozenset[str] = frozenset()


_FILTER_SPECS: dict[type, _FilterSpec] = {
    inputs.AssetsFilter: _FilterSpec(
        filter_cls=inputs.AssetsFilter,
        field_filter_cls=inputs.AssetsFieldFilter,
        field_enum=enums.AssetsFilterField,
        operation_enum=enums.FieldFilterOperation,
        fields={
            "id": enums.AssetsFilterField.ID,
            "name": enums.AssetsFilterField.NAME,
            "vendor": enums.AssetsFilterField.VENDOR,
            "product": enums.AssetsFilterField.PRODUCT,
            "version": enums.AssetsFilterField.VERSION,
            "type": enums.AssetsFilterField.TYPE,
            "sha256": enums.AssetsFilterField.SHA256,
            "status": enums.AssetsFilterField.PROCESSINGSTATUS,
            "risk_category": enums.AssetsFilterField.RISKCATEGORY,
            "risk_score": enums.AssetsFilterField.RISKSCORE,
            "uploaded_by": enums.AssetsFilterField.UPLOADEDBY,
        },
        list_value=True,
        enum_fields=frozenset({"status", "risk_category"}),
    ),
    inputs.VulnerabilityFilter: _FilterSpec(
        filter_cls=inputs.VulnerabilityFilter,
        field_filter_cls=inputs.VulnerabilityFieldFilter,
        field_enum=enums.VulnerabilityField,
        operation_enum=enums.FilterFieldOperation,
        fields={
            "cve": enums.VulnerabilityField.CVE,
            "severity": enums.VulnerabilityField.SEVERITY,
            "name": enums.VulnerabilityField.NAME,
            "version": enums.VulnerabilityField.VERSION,
            "vendor": enums.VulnerabilityField.VENDOR,
            "maturity": enums.VulnerabilityField.MATURITY,
            "filepath": enums.VulnerabilityField.FILEPATH,
            "attack_vector": enums.VulnerabilityField.ATTACKVECTOR,
            "attack_complexity": enums.VulnerabilityField.ATTACKCOMPLEXITY,
            "remediation_status": enums.VulnerabilityField.VULNERABILITYREMEDIATIONSTATUS,
            "epss_score": enums.VulnerabilityField.EPSSSCORE,
            "epss_percentile": enums.VulnerabilityField.EPSSPERCENTILE,
        },
        enum_fields=frozenset(
            {"severity", "maturity", "attack_vector", "attack_complexity", "remediation_status"}
        ),
    ),
    inputs.DependencyFilter: _FilterSpec(
        filter_cls=inputs.DependencyFilter,
        field_filter_cls=inputs.DependencyFieldFilter,
        field_enum=enums.DependencyField,
        operation_enum=enums.FilterFieldOperation,
        fields={
            "name": enums.DependencyField.NAME,
            "vendor": enums.DependencyField.VENDOR,
            "type": enums.DependencyField.TYPE,
            "subtype": enums.DependencyField.SUBTYPE,
            "license": enums.DependencyField.LICENSE,
            "version": enums.DependencyField.VERSION,
            "verification": enums.DependencyField.VERIFICATION,
            "scope": enums.DependencyField.SCOPE,
            "confidence": enums.DependencyField.CONFIDENCE,
        },
        enum_fields=frozenset({"type", "subtype", "verification", "scope"}),
    ),
    inputs.MisconfigurationsFilter: _FilterSpec(
        filter_cls=inputs.MisconfigurationsFilter,
        field_filter_cls=inputs.MisconfigurationsFilterField,
        field_enum=enums.MisconfigurationsField,
        operation_enum=enums.FilterFieldOperation,
        fields={
            "name": enums.MisconfigurationsField.NAME,
            "category": enums.MisconfigurationsField.CATEGORY,
            "status": enums.MisconfigurationsField.STATUS,
            "severity": enums.MisconfigurationsField.SEVERITY,
        },
        enum_fields=frozenset({"status", "severity"}),
    ),
}


_LOOKUP_TO_OPERATION = {
    _LOOKUP_DEFAULT: "EQUAL",
    "contains": "CONTAINS",
    "in": "ENUM",
    "gt": "GREATERTHAN",
    "gte": "GREATERTHANOREQUAL",
    "lt": "LESSTHAN",
    "lte": "LESSTHANOREQUAL",
}


def where(filter_model: type, **criteria: Any) -> Any:
    """Build a generated Turbine filter model from REST-style keyword criteria.

    Examples:
        >>> where(inputs.VulnerabilityFilter, severity="CRITICAL")
        >>> where(inputs.AssetsFilter, name__contains="router")
    """
    criteria = {key: value for key, value in criteria.items() if value is not None}
    spec = _get_spec(filter_model)
    fields = [_build_field_filter(spec, key, value) for key, value in criteria.items()]
    return spec.filter_cls(fields=fields or None)


def merge_where(filter_value: Any, filter_model: type, **criteria: Any) -> Any:
    """Merge REST-style criteria into an existing generated filter or dict."""
    criteria = {key: value for key, value in criteria.items() if value is not None}
    if not criteria:
        return filter_value

    spec = _get_spec(filter_model)
    base = _coerce_filter(filter_value, spec)
    extra = where(filter_model, **criteria)

    merged_fields = [
        *(getattr(base, "fields", None) or []),
        *(getattr(extra, "fields", None) or []),
    ]
    if base is None:
        return extra
    return base.model_copy(update={"fields": merged_fields or None})


def _get_spec(filter_model: type) -> _FilterSpec:
    try:
        return _FILTER_SPECS[filter_model]
    except KeyError as exc:
        raise ValueError(f"Unsupported filter model: {getattr(filter_model, '__name__', filter_model)!r}") from exc


def _coerce_filter(filter_value: Any, spec: _FilterSpec) -> Any:
    if filter_value is None:
        return None
    if isinstance(filter_value, spec.filter_cls):
        return filter_value
    if isinstance(filter_value, dict):
        return spec.filter_cls.model_validate(filter_value)
    raise TypeError(
        f"filter must be {spec.filter_cls.__name__}, dict, or None; got {type(filter_value).__name__}"
    )


def _build_field_filter(spec: _FilterSpec, key: str, value: Any) -> Any:
    field_name, lookup = _split_lookup(key)
    if lookup not in _LOOKUP_TO_OPERATION:
        raise ValueError(f"Unsupported filter lookup: {lookup!r}")
    if field_name not in spec.fields:
        supported = ", ".join(sorted(spec.fields))
        raise ValueError(f"Unsupported filter field {field_name!r}; supported fields: {supported}")

    operation_name = _LOOKUP_TO_OPERATION[lookup]
    if lookup == _LOOKUP_DEFAULT and field_name in spec.enum_fields:
        operation_name = "ENUM"

    return spec.field_filter_cls(
        field_name=spec.fields[field_name],
        value=_normalize_value(value, list_value=spec.list_value),
        operation=getattr(spec.operation_enum, operation_name),
    )


def _split_lookup(key: str) -> tuple[str, str]:
    if "__" not in key:
        return key, _LOOKUP_DEFAULT
    field_name, lookup = key.rsplit("__", 1)
    return field_name, lookup


def _normalize_value(value: Any, *, list_value: bool) -> Any:
    if isinstance(value, enums.Severity):
        value = value.value
    elif hasattr(value, "value") and isinstance(getattr(value, "value"), str):
        value = value.value

    if list_value and not isinstance(value, list):
        return [value]
    return value


__all__ = ["where", "merge_where"]
