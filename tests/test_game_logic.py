import os
import sys

# Ensure repository root is on sys.path so tests can import logic_utils from parent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess():
    ok, val, err = parse_guess("42")
    assert ok and val == 42 and err is None

    ok, val, err = parse_guess("42.0")
    assert ok and val == 42 and err is None

    ok, val, err = parse_guess("")
    assert not ok and err == "Enter a guess."

    ok, val, err = parse_guess("abc")
    assert not ok and err == "That is not a number."


def test_update_score():
    # Win on attempt 1 -> attempt_number=1 -> points = 100 - 10*(1+1) = 80
    assert update_score(0, "Win", 1) == 80

    # Too High parity: even -> +5, odd -> -5
    assert update_score(10, "Too High", 2) == 15
    assert update_score(10, "Too High", 3) == 5

    # Too Low parity: even -> -5, odd -> +5 (mirrored behavior)
    assert update_score(10, "Too Low", 2) == 5
    assert update_score(10, "Too Low", 3) == 15
