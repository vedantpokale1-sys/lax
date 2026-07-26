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


def test_format_result_divide_by_zero_is_guarded():
    assert ved.format_result(1, 0, "/") == "cannot divide by zero"
    assert ved.format_result(1, 0, "+") == "1"


def test_read_number_parses_float(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda *args: "2.5")
    assert ved.read_number("n: ") == 2.5


def test_read_number_reprompts_until_valid(monkeypatch, capsys):
    answers = iter(["abc", "", "7"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    assert ved.read_number("n: ") == 7.0
    assert capsys.readouterr().out.count("that is not a number, try again") == 2


def test_main_reads_inputs_and_prints_result(monkeypatch, capsys):
    answers = iter(["vedant", "7", "3", "-"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    ved.main()

    out = capsys.readouterr().out
    assert "im the boss" in out
    assert "4.0" in out
    assert "this is my calculator" in out
    assert "vedant" in out


def test_main_with_invalid_operator(monkeypatch, capsys):
    answers = iter(["vedant", "7", "3", "^"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    ved.main()

    assert "invalid operator" in capsys.readouterr().out


def test_main_reprompts_on_non_numeric_input(monkeypatch, capsys):
    answers = iter(["vedant", "abc", "7", "3", "+"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    ved.main()

    out = capsys.readouterr().out
    assert "that is not a number, try again" in out
    assert "10.0" in out


def test_main_divide_by_zero(monkeypatch, capsys):
    answers = iter(["vedant", "7", "0", "/"])
    monkeypatch.setattr(builtins, "input", lambda *args: next(answers))

    ved.main()

    assert "cannot divide by zero" in capsys.readouterr().out
