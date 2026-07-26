import builtins

import pytest

import ved


@pytest.mark.parametrize(
    "a, b, operator, expected",
    [
        (2, 3, "+", 5),
        (-2, 3, "+", 1),
        (5, 3, "-", 2),
        (3, 5, "-", -2),
        (4, 3, "*", 12),
        (4, 0, "*", 0),
        (10, 4, "/", 2.5),
        (-9, 3, "/", -3.0),
    ],
)
def test_calculate_supported_operators(a, b, operator, expected):
    assert ved.calculate(a, b, operator) == expected


@pytest.mark.parametrize("operator", ["", "%", "**", "add", "+-", " "])
def test_calculate_unknown_operator_returns_none(operator):
    assert ved.calculate(1, 2, operator) is None


def test_calculate_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        ved.calculate(1, 0, "/")


def test_calculate_supports_floats_and_strings():
    assert ved.calculate(0.5, 0.25, "+") == 0.75
    assert ved.calculate("ab", 2, "*") == "abab"


def test_format_result_returns_string():
    assert ved.format_result(2, 3, "+") == "5"
    assert ved.format_result(10, 4, "/") == "2.5"


def test_format_result_invalid_operator():
    assert ved.format_result(2, 3, "?") == "invalid operator"


def test_main_reads_inputs_and_prints_result(monkeypatch, capsys):
    answers = iter(["vedant", "7", "3", "-"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    ved.main()

    out = capsys.readouterr().out
    assert "im the boss" in out
    assert "4" in out
    assert "this is my calculator" in out
    assert "vedant" in out


def test_main_with_invalid_operator(monkeypatch, capsys):
    answers = iter(["vedant", "7", "3", "^"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    ved.main()

    assert "invalid operator" in capsys.readouterr().out


def test_main_rejects_non_numeric_input(monkeypatch):
    answers = iter(["vedant", "abc"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    with pytest.raises(ValueError):
        ved.main()
