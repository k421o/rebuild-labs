from src.report import run


def test_prints_total(tmp_path, capsys) -> None:
    source = tmp_path / "input.csv"
    source.write_text("name,units\na,2\nb,3\n")
    run(str(source))
    assert capsys.readouterr().out == "Total units: 5\n"
