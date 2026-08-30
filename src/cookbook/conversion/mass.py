from cookbook.domain.unit.mass import MetricMassUnit, CustomaryMassUnit


MassUnit = MetricMassUnit | CustomaryMassUnit

GRAMS_PER_OUNCE = 28.349523125


def _convert_within_system(
        quantity: float,
        from_unit: MassUnit,
        to_unit: MassUnit,
) -> float:
    return quantity * from_unit.value.scale / to_unit.value.scale


def _convert_between_systems(
        quantity: float,
        from_unit: MassUnit,
        to_unit: MassUnit,
) -> float:
    if isinstance(from_unit, MetricMassUnit):
        grams = quantity * from_unit.value.scale
        ounces = grams / GRAMS_PER_OUNCE
        return ounces / to_unit.value.scale

    if isinstance(to_unit, MetricMassUnit):
        ounces = quantity * from_unit.value.scale
        grams = GRAMS_PER_OUNCE * ounces
        return grams / to_unit.value.scale


def convert_mass(
        quantity: float,
        from_unit: MassUnit,
        to_unit: MassUnit,
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
