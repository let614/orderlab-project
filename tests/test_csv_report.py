import pytest

from orderlab.csv_report import revenue_from_csv


def test_fixture_revenue(sample_csv):
    assert revenue_from_csv(sample_csv) == 35_000


def test_empty_csv(tmp_path):
    path = tmp_path / "empty.csv"
    path.write_text("price,quantity\n", encoding="utf-8")
    assert revenue_from_csv(path) == 0


def test_missing_csv(tmp_path):
    with pytest.raises(FileNotFoundError):
        revenue_from_csv(tmp_path / "missing.csv")


def test_invalid_csv(tmp_path):
    path = tmp_path / "invalid.csv"
    path.write_text("price,quantity\nnot_a_number,2\n", encoding="utf-8")
    with pytest.raises(ValueError):
        revenue_from_csv(path)
