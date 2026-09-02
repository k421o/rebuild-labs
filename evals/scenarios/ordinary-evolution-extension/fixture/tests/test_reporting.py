from src.reporting import render_report


def test_registered_json_renderer_preserves_the_released_contract() -> None:
    assert render_report("json", [{"name": "Ada", "units": 3}]) == (
        '[{"name": "Ada", "units": 3}]'
    )
