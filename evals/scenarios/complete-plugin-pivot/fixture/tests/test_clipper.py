from src.clipper import normalize_url


def test_normalizes_host_and_trailing_slash() -> None:
    assert normalize_url("https://EXAMPLE.com/path/") == "https://example.com/path"
