from __future__ import annotations

ROLE_ACTIONS = {
    "admin": {"deploy", "read"},
    "viewer": {"read"},
}


def decide(request: dict[str, str]) -> bool:
    """Stable service boundary backed by the legacy role model."""
    return request["action"] in ROLE_ACTIONS.get(request["role"], set())
