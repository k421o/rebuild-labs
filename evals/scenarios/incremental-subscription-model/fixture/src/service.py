from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: str
    subscription_id: str | None = None


CUSTOMERS: dict[str, Customer] = {}


def put_subscription(customer_id: str, subscription_id: str) -> None:
    customer = CUSTOMERS.setdefault(customer_id, Customer(customer_id))
    customer.subscription_id = subscription_id


def customer_v1(customer_id: str) -> dict[str, str | None]:
    customer = CUSTOMERS[customer_id]
    return {
        "id": customer.customer_id,
        "subscription_id": customer.subscription_id,
    }
