from src.service import CUSTOMERS, customer_v1, put_subscription


def test_v1_customer_contains_subscription_identifier() -> None:
    CUSTOMERS.clear()
    put_subscription("customer-1", "subscription-9")
    assert customer_v1("customer-1") == {
        "id": "customer-1",
        "subscription_id": "subscription-9",
    }
