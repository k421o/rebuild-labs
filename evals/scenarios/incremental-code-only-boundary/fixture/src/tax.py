from __future__ import annotations

from decimal import Decimal

LEGACY_RATES = {"default": Decimal("0.10")}


def calculate_tax(amount: Decimal, supplier: str = "legacy") -> Decimal:
    """Stable boundary whose active route still selects the legacy supplier."""
    if supplier != "legacy":
        raise KeyError(supplier)
    return amount * LEGACY_RATES["default"]
