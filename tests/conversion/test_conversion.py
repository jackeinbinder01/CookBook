from cookbook.domain.unit.mass import MetricMassUnit, CustomaryMassUnit
from cookbook.conversion.mass import convert_mass


def test_mass_conversion():
    g = MetricMassUnit.GRAM
    kg = MetricMassUnit.KILOGRAM

    oz = CustomaryMassUnit.OUNCE
    lb = CustomaryMassUnit.POUND

    # Metric -> Metric
    assert convert_mass(quantity=1000, from_unit=g, to_unit=kg) == 1

    # Customary -> Customary
    assert convert_mass(quantity=1, from_unit=lb, to_unit=oz) == 16

    # Metric -> Customary
    assert convert_mass(quantity=28.349523125, from_unit=g, to_unit=oz) == 1

    # Customary -> Metric
    assert convert_mass(quantity=1, from_unit=oz, to_unit=g) == 28.349523125 
