
from cookbook.domain.unit.mass import MetricMassUnit, CustomaryMassUnit
from cookbook.domain.unit.volume import MetricVolumeUnit, CustomaryVolumeUnit
from cookbook.domain.unit import ScaledUnit

GRAMS_PER_OUNCE = 28.349523125
MILLILITERS_PER_FLUID_OUNCE = 29.5735295625

REFERENCE_FACTORS = {
    (MetricMassUnit, CustomaryMassUnit): GRAMS_PER_OUNCE,
    (MetricVolumeUnit, CustomaryVolumeUnit): MILLILITERS_PER_FLUID_OUNCE
}

def convert(
        quantity: float,
        from_unit: ScaledUnit,
        to_unit: ScaledUnit,
) -> float:
    if type(from_unit) is type(to_unit):
        return _convert_within_system(
            quantity=quantity,
            from_unit=from_unit,
            to_unit=to_unit
        )

    return _convert_between_systems(
            quantity=quantity,
            from_unit=from_unit,
            to_unit=to_unit
    )

def _convert_within_system(
        quantity: float,
        from_unit: ScaledUnit,
        to_unit: ScaledUnit,
) -> float:
    return quantity * from_unit.value.scale / to_unit.value.scale


def _convert_between_systems(
        quantity: float,
        from_unit: ScaledUnit,
        to_unit: ScaledUnit,
        
) -> float:
    from_type = type(from_unit)
    to_type = type(to_unit)

    if (from_type, to_type) in REFERENCE_FACTORS:
        factor = REFERENCE_FACTORS[(from_type, to_type)]
        bridge_factor = 1 / factor

    elif (to_type, from_type) in REFERENCE_FACTORS:
        factor = REFERENCE_FACTORS[(to_type, from_type)]
        bridge_factor = factor

    else:
        raise ValueError(
            f"Conversion from {from_unit} to {to_unit} not supported"
        )

    src_ref = quantity * from_unit.value.scale
    tgt_ref = src_ref * bridge_factor
    
    return tgt_ref / to_unit.value.scale
