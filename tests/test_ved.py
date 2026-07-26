import builtins

import pytest

import ved


def fake_input(monkeypatch, *answers):
    values = iter(answers)

    def _input(*args):
        value = next(values)
        if isinstance(value, BaseException):
            raise value
        return value

    monkeypatch.setattr(builtins, "input", _input)


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
        (0.5, 0.25, "+", 0.75),
    ],
)
def test_calculate_supported_operators(a, b, operator, expected):
    assert ved.calculate(a, b, operator) == expected


@pytest.mark.parametrize("operator", ["", "%", "**", "add", "+-", " "])
def test_calculate_unknown_operator_raises(operator):
    with pytest.raises(ValueError, match="invalid operator"):
        ved.calculate(1, 2, operator)


def test_calculate_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        ved.calculate(1, 0, "/")


def test_read_number_parses_float(monkeypatch):
    fake_input(monkeypatch, "2.5")
    assert ved.read_number("n: ") == 2.5


def test_read_number_reprompts_until_valid(monkeypatch, capsys):
    fake_input(monkeypatch, "abc", "", "7")

    assert ved.read_number("n: ") == 7.0
    err = capsys.readouterr().err
    assert "'abc' is not a number, try again" in err
    assert err.count("is not a number") == 2


@pytest.mark.parametrize(
    "error, message",
    [(EOFError(), "no input available"), (KeyboardInterrupt(), "cancelled by user")],
)
def test_read_number_exits_when_input_unavailable(monkeypatch, error, message):
    fake_input(monkeypatch, error)
    with pytest.raises(SystemExit, match=message):
        ved.read_number("n: ")


def test_read_text_returns_input(monkeypatch):
    fake_input(monkeypatch, "vedant")
    assert ved.read_text("name: ") == "vedant"


@pytest.mark.parametrize(
    "error, message",
    [(EOFError(), "no input available"), (KeyboardInterrupt(), "cancelled by user")],
)
def test_read_text_exits_when_input_unavailable(monkeypatch, error, message):
    fake_input(monkeypatch, error)
    with pytest.raises(SystemExit, match=message):
        ved.read_text("name: ")


def test_main_happy_path(monkeypatch, capsys):
    fake_input(monkeypatch, "vedant", "7", "3", "-")

    assert ved.main() == 0

    out = capsys.readouterr().out
    assert "4.0" in out
    assert "this is my calculator" in out


def test_main_reprompts_on_non_numeric_input(monkeypatch, capsys):
    fake_input(monkeypatch, "vedant", "abc", "7", "3", "+")

    assert ved.main() == 0

    captured = capsys.readouterr()
    assert "is not a number, try again" in captured.err
    assert "10.0" in captured.out


def test_main_invalid_operator_returns_error_code(monkeypatch, capsys):
    fake_input(monkeypatch, "vedant", "7", "3", "^")

    assert ved.main() == 1

    captured = capsys.readouterr()
    assert "invalid operator" in captured.err
    assert "this is my calculator" not in captured.out


def test_main_divide_by_zero_returns_error_code(monkeypatch, capsys):
    fake_input(monkeypatch, "vedant", "7", "0", "/")

    assert ved.main() == 1
    assert "cannot divide by zero" in capsys.readouterr().err
