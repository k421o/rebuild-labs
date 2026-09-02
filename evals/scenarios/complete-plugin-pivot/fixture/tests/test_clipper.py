import json
import sys

from src.clipper import run


def test_cli_normalizes_host_and_trailing_slash(tmp_path, monkeypatch, capsys) -> None:
    config = tmp_path / "bookmark.json"
    config.write_text(json.dumps({"url": "https://EXAMPLE.com/path/"}))
    monkeypatch.setattr(sys, "argv", ["clipper", str(config)])

    run()

    assert capsys.readouterr().out == "https://example.com/path\n"
