from cookbook.domain.unit.mass import MetricMassUnit, CustomaryMassUnit
from cookbook.domain.unit.volume import MetricVolumeUnit, CustomaryVolumeUnit
from cookbook.conversion.core import convert


def test_mass_conversion():
    g = MetricMassUnit.GRAM
    kg = MetricMassUnit.KILOGRAM

    oz = CustomaryMassUnit.OUNCE
    lb = CustomaryMassUnit.POUND

    # Metric -> Metric
    assert convert(quantity=1000, from_unit=g, to_unit=kg) == 1

    # Customary -> Customary
    assert convert(quantity=1, from_unit=lb, to_unit=oz) == 16

    # Metric -> Customary
    assert convert(quantity=28.349523125, from_unit=g, to_unit=oz) == 1

    # Customary -> Metric
    assert convert(quantity=1, from_unit=oz, to_unit=g) == 28.349523125


def test_volume_conversion():
    cup =  CustomaryVolumeUnit.CUP
    fl_oz = CustomaryVolumeUnit.FLUID_OUNCE

    ml = MetricVolumeUnit.MILLILITER
    l = MetricVolumeUnit.LITER

    assert convert(quantity=1, from_unit=cup, to_unit=fl_oz) == 8
