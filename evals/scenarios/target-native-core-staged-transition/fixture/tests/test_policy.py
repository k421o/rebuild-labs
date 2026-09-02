from src.policy import decide


def test_released_decision_boundary_returns_a_boolean() -> None:
    request = {
        "tenant_id": "tenant-1",
        "actor_id": "user-7",
        "resource_id": "service-2",
        "role": "admin",
        "action": "deploy",
    }
    assert decide(request) is True
