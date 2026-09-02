from decimal import Decimal

from src.tax import calculate_tax


def test_released_boundary_uses_legacy_supplier_by_default() -> None:
    assert calculate_tax(Decimal("12.00")) == Decimal("1.2000")
